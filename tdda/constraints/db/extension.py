# -*- coding: utf-8 -*-

"""
Extensions to the ``tdda`` command line tool, to support databases.
"""

from __future__ import print_function

import sys

from tdda.constraints.extension import ExtensionBase

from tdda.constraints.db.dbbase import applicable
from tdda.constraints.db.dbdiscover import DatabaseDiscoverer
from tdda.constraints.db.dbverify import DatabaseVerifier


class TDDADatabaseExtension(ExtensionBase):
    def __init__(self, argv, verbose=False):
        ExtensionBase.__init__(self, argv, verbose=verbose)

    def applicable(self):
        return applicable(self.argv)

    def help(self, stream=sys.stdout):
        print('  - Tables from PostgreSQL databases ("postgres:table-name")',
              file=stream)
        print('  - Tables from MySQL databases ("mysql:table-name")',
              file=stream)
        print('  - Tables from SQLite databases ("sqlite:table-name")',
              file=stream)
        print('  - Collections from MongoDB NoSQL databases '
              '("mongodb:collection-name")', file=stream)

    def discover(self):
        return DatabaseDiscoverer(self.argv, verbose=self.verbose).discover()

    def verify(self):
        return DatabaseVerifier(self.argv, verbose=self.verbose).verify()
