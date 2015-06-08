Google Cloud Storage oAuth2 ENV Plugin
======================================

.. image:: https://img.shields.io/pypi/v/gcs-auth2-boto-env-plugin.svg
    :target: https://pypi.python.org/pypi/gcs-auth2-boto-env-plugin

gcs-oauth2-boto-env-plugin is a Python application whose purpose is to behave as an auth plugin for the boto auth plugin framework for use with OAuth 2.0 credentials for the Google Cloud Platform. This plugin is only compatible with service accounts, and it's functionality is essentially a wrapper around `gcs-oauth2-boto-plugin <https://github.com/GoogleCloudPlatform/gcs-oauth2-boto-plugin>`_, with the added capability of passing the private JSON key as an environment variable for easy deployment.

Usage
-----

Call the following program with the content of the JSON private key set as ``GOOGLE_OAUTH2_JSON_PRIVATE_KEY`` environment variable::

    import boto
    import gcs_oauth2_boto_env_plugin

    project_id = 'your-project-id'

    header_values = {"x-goog-project-id": project_id}
    uri = boto.storage_uri('', 'gs')
    for bucket in uri.get_all_buckets(headers=header_values):
        print bucket.name


License
-------

All source code is licensed under the `MIT License <https://raw.githubusercontent.com/rs/eve-auth-jwt/master/LICENSE>`_.
