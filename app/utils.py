import os

import onepasswordconnectsdk
from onepasswordconnectsdk.client import Client, new_client_from_environment


def get_op_config():
    op_client: Client = new_client_from_environment()

    OP_DJANGO_SETTINGS_VARS = [
        'database.host',
        'database.port',
        'database.name',
        'database.user',
        'database.password',
        'settings.ALLOWED_HOSTS',
        'settings.DEBUG',
        'settings.SCOPE',
        'settings.SENTRY_DSN',
        'settings.SECRET_KEY',
    ]

    op_config_get = {}
    for var in OP_DJANGO_SETTINGS_VARS:
        op_config_get[var] = {"opitem": "mines", "opfield": var}

    return onepasswordconnectsdk.load_dict(op_client, op_config_get)
