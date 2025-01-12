# -*- coding: UTF-8 -*-

import os
from typing import Tuple

from .consts import APP_TYPE_ISV, APP_TYPE_INTERNAL
from .logger import Logger, LoggerProxy
from .app_settings import AppSettings
from .store import MemoryStore, Store


class Config(object):

    def __init__(self, domain, app_settings, logger, log_level, store):
        # type: (str, AppSettings, Logger, int, Store) -> None
        self.domain = domain
        self.app_settings = app_settings
        self.logger = LoggerProxy(log_level, logger)
        self.store = store

    @staticmethod
    def new_config_with_memory_store(domain, settings, logger,
                                     log_level):  # type: (str, AppSettings, Logger, int) -> Config
        return Config(domain, settings, logger, log_level, MemoryStore())

    @staticmethod
    def new_config(domain, settings, logger, log_level,
                   store):  # type: (str, AppSettings, Logger, int, Store) -> Config
        return Config(domain, settings, logger, log_level, store)

    @staticmethod
    def __app_settings_from_env():  # type: () -> Tuple[str, str, str, str]
        """
        This function reads app_id, app_secret, ... from system env.
        If app_id or app_secret doesn't exist in system env, a RuntimeError will be raised.
        """

        app_id = os.getenv('APP_ID', '')
        app_secret = os.getenv('APP_SECRET', '')
        verification_token = os.getenv('VERIFICATION_TOKEN', '')
        encrypt_key = os.getenv('ENCRYPT_KEY', '')

        if app_id == '':
            raise RuntimeError('environment variables not exist `APP_ID`')
        if encrypt_key == '':
            raise RuntimeError('environment variables not exist `APP_SECRET`')

        return app_id, app_secret, verification_token, encrypt_key

    @staticmethod
    def new_isv_app_settings_from_env():
        """
        This static method initialize a new ISV App Settings and read app_id, app_secret, ... from system env
        """

        app_id, app_secret, verification_token, encrypt_key = Config.__app_settings_from_env()
        return AppSettings(APP_TYPE_ISV, app_id, app_secret, verification_token, encrypt_key)

    @staticmethod
    def new_internal_app_settings_from_env():
        """
        This static method initialize a new internal App Settings and read app_id, app_secret, ... from system env
        """

        app_id, app_secret, verification_token, encrypt_key = Config.__app_settings_from_env()
        return AppSettings(APP_TYPE_INTERNAL, app_id, app_secret, verification_token, encrypt_key)

    @staticmethod
    def new_internal_app_settings(app_id, app_secret, verification_token,
                                  encrypt_key):  # type: (str, str, str, str) -> AppSettings
        return AppSettings(APP_TYPE_INTERNAL, app_id, app_secret, verification_token, encrypt_key)

    @staticmethod
    def new_isv_app_settings(app_id, app_secret, verification_token,
                             encrypt_key):  # type: (str, str, str, str) -> AppSettings
        return AppSettings(APP_TYPE_ISV, app_id, app_secret, verification_token, encrypt_key)
