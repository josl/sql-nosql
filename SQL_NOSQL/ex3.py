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

Get all orders (with products) made by ALFKI that contain at least 2 product
types.
'''


def ex2SQLite():
    c = conn.cursor()
    customerID = 'ALFKI'

    query = '''
        SELECT * FROM "Order Details Extended",
            (
                SELECT Orders.OrderID, COUNT(Orders.OrderID)
                    AS NumberOfProducts
                FROM "Orders", "Order Details Extended"
                USING ("OrderID")
                WHERE Orders.CustomerID="%s"
                GROUP BY "Order Details Extended".OrderID
            ) as ALFKI_count USING ("OrderID")
            WHERE ALFKI_count.NumberOfProducts >= 2;
    ''' % customerID

    orders = [order for order in c.execute(query)]
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()
    return orders


def ex2Mongo():
    db.orders.aggregate([
        {$match: {'CustomerID': 'ALFKI'}},
        {$lookup: {
            from: 'order-details',
            localField: 'OrderID',
            foreignField: 'OrderID',
            as: 'Products'
        }},
        {$project: {
            'OrderID': 1,
            'OrderDate': 1,
            'Products.ProductName': 1,
            'Products.ProductID': 1,
            'NumberOfProducts': {$size: "$Products"}
        }},
        {$unwind: '$Products'},
        {$lookup: {
            from: 'products',
            localField: 'Products.ProductID',
            foreignField: 'ProductID',
            as: 'Products'
        }},
        {$match: {'NumberOfProducts': {$gte: 2}}}
    ])

    # for post in db.customers.find({'CustomerID': {}}):
    #     print(post['CustomerID'])
