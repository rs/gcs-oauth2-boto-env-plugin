#!/usr/bin/python

import json
import os
from gcs_oauth2_boto_plugin.oauth2_client import FileSystemTokenCache, OAuth2JsonServiceAccountClient
from boto.auth_handler import AuthHandler
from boto.auth_handler import NotReadyToAuthenticate

GOOGLE_OAUTH2_PROVIDER_AUTHORIZATION_URI = (
    'https://accounts.google.com/o/oauth2/auth')
GOOGLE_OAUTH2_PROVIDER_TOKEN_URI = (
    'https://accounts.google.com/o/oauth2/token')


class OAuth2ServiceAccountEnvAuth(AuthHandler):
    capability = ['google-oauth2', 's3']

    def __init__(self, path, config, provider):
        json_key = None
        if provider.name == 'google' and os.environ.get('GOOGLE_OAUTH2_JSON_PRIVATE_KEY'):
            try:
                json_key = json.loads(os.environ.get('GOOGLE_OAUTH2_JSON_PRIVATE_KEY'))
            except ValueError:
                pass

        if json_key is None:
            raise NotReadyToAuthenticate()

        token_cache = FileSystemTokenCache()

        proxy_host = None
        proxy_port = None
        proxy_user = None
        proxy_pass = None
        if config.has_option('Boto', 'proxy') and config.has_option('Boto', 'proxy_port'):
            proxy_host = config.get('Boto', 'proxy')
            proxy_port = int(config.get('Boto', 'proxy_port'))
            proxy_user = config.get('Boto', 'proxy_user', None)
            proxy_pass = config.get('Boto', 'proxy_pass', None)

        self.oauth2_client = OAuth2JsonServiceAccountClient(
            json_key['client_id'], json_key['client_email'],
            json_key['private_key_id'], json_key['private_key'],
            access_token_cache=token_cache, auth_uri=GOOGLE_OAUTH2_PROVIDER_AUTHORIZATION_URI,
            token_uri=GOOGLE_OAUTH2_PROVIDER_TOKEN_URI,
            disable_ssl_certificate_validation=not(config.getbool('Boto', 'https_validate_certificates', True)),
            proxy_host=proxy_host, proxy_port=proxy_port, proxy_user=proxy_user, proxy_pass=proxy_pass)

    def add_auth(self, http_request):
        http_request.headers['Authorization'] = self.oauth2_client.GetAuthorizationHeader()
