#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of SQL_NOSQL.
# https://github.com/josl/SQL_NOSQL

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Jose L. Bellod Cisneros <bellod.cisneros@gmail.com>

from SQL_NOSQL import conn
from SQL_NOSQL import db

'''
This exercise accomplish the following:

For SQLite: Establish connection to this database in Python (use the sqlite3
module). Document the connection by making some simple queries.

For Mongo: To get started, clone this repository into your working directory.
Start a running instance of MongoDB* (on command-line: mongod), then run the
.sh file in a terminal. This should create a live Mongo database named
‘Northwind’ that you can connect to in Python. Document the connection by
making some simple queries.

*Make sure you have MongoDB installed.
'''


def ex1SQLite():
    c = conn.cursor()
    query = 'SELECT * FROM Regions'
    regions = [region[1].strip() for region in c.execute(query)]
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()
    # ['Eastern', 'Westerns', 'Northern', 'Southern']
    return regions


def ex1Mongo():
    for post in db.regions.find():
        print(post['RegionDescription'])
