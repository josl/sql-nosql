#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of SQL_NOSQL.
# https://github.com/josl/SQL_NOSQL

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Jose L. Bellod Cisneros <bellod.cisneros@gmail.com>

from SQL_NOSQL.version import __version__  # NOQA
import sqlite3
from pymongo import MongoClient


conn = sqlite3.connect('database/northwind.db')
client = MongoClient('mongodb://localhost:27017/')
db = client.Northwind
