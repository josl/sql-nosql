#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of SQL_NOSQL.
# https://github.com/josl/SQL_NOSQL

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Jose L. Bellod Cisneros <bellod.cisneros@gmail.com>

from unittest import TestCase as PythonTestCase
from SQL_NOSQL.ex1 import ex1SQLite


class TestCase(PythonTestCase):
    def ex1Test(self):
        ans = ex1SQLite()
        print('lalalala')
        return ans
        print(ans)
        self.assertTrue(False)
