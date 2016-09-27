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

The customer with customerID ALFKI has made a number of orders containing some
products. Query for, and return, all orders made by ALFKI and the products they
contain.
'''


def ex2SQLite():
    c = conn.cursor()
    customerID = 'ALFKI'

    query = '''
        SELECT Orders.OrderID, Orders.OrderDate, Orders.EmployeeID,
              "Order Details Extended".ProductName
        FROM Orders, "Order Details Extended"
        USING ("OrderID")
        WHERE "CustomerID"="ALFKI"
    ''' % customerID

    orders = [order for order in c.execute(query)]
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()
    return orders


def ex2Mongo():
    customerID = 'ALFKI'
    db.orders.aggregate([
        {$match: {'CustomerID': 'ALFKI'}},
        {$lookup: {
            from: 'order-details',
            localField: 'OrderID',
            foreignField: 'OrderID',
            as: 'Products'
        }},
        {$unwind: '$Products'},
        {$lookup: {
            from: 'products',
            localField: 'Products.ProductID',
            foreignField: 'ProductID',
            as: 'Products'
        }},
        {$project: {
            'OrderID': 1,
            'OrderDate': 1,
            'Products.ProductName': 1,
            'Products.ProductID': 1
        }}
    ])

    # for post in db.customers.find({'CustomerID': {}}):
    #     print(post['CustomerID'])
