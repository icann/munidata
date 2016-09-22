# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .database import PICUDatabase


class UnicodeDataVersionManager(object):
    """
    Manage multiple version of UnicodeDatabase objects.

    Note: A UnicodeDataVersionManager instance can only manage
    UnicodeDatabase of the same class.
    """

    def __init__(self, database_class=PICUDatabase):
        self._versions = {}
        self._database_class = database_class

    def register(self, expected_version, *args, **kwargs):
        """
        Create and register a new UnicodeDatabase in the manager.

        :param expected_version: The expected Unicode version.
        :returns: The created UnicodeDatabase object.
        :raises ValueError: If expected_version and actual Unicode version
                            of the created database mismatch.
        """
        db = self._database_class(*args, **kwargs)
        loaded_ver = db.get_unicode_version()
        if expected_version and loaded_ver != expected_version:
            raise ValueError("unicode version mismatch ('{0}' != '{1}')".format(loaded_ver, expected_version))
        self._versions[loaded_ver] = db
        return db

    def get_db_by_version(self, unicode_version):
        """
        Retrieve a UnicodeDatabase instance by its version.

        :param unicode_version: The Unicode version of the database.
        :returns: The instance of the UnicodeDatabase
                  whose version is unicode_version.
        :raises ValueError: If no corresponding database has been registered.
        """
        return self._versions[unicode_version]
