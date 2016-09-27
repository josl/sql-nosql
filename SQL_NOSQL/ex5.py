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

How many different and which products have been ordered by customers who have
also ordered “Uncle Bob’s Organic Dried Pears”?

'''


def ex2SQLite():
    c = conn.cursor()
    productID = 7
    # Customers who bought product 7
    view = '''
        CREATE VIEW "Customers_7" AS
                SELECT Orders.CustomerID
                FROM Orders
                    LEFT JOIN "Order Details Extended"
                        ON "Order Details Extended".OrderID = Orders.OrderID
                WHERE "ProductID"="7"
                GROUP BY Orders.CustomerID
    ''' % productID

    c.execute(view)
    c.commit()
    # Other products bought by customers who bought product 7
    query = '''
        SELECT "Order Details Extended".ProductName, COUNT("Order Details Extended".ProductName)
        FROM Customers_7
            LEFT JOIN Orders
                ON Customers_7.CustomerID = Orders.CustomerID
            LEFT JOIN "Order Details Extended"
                ON "Order Details Extended".OrderID = Orders.OrderID
        GROUP BY "Order Details Extended".ProductName
    '''
    c.execute(query)
    for customer in c.execute(query):
        print(customer)
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()
    return orders

        {$project: {
            CustomerID: '$Customers.CustomerID'
        }},
        {$group: {
            _id: '$CustomerID',
        }},
def ex2Mongo():
    db['order-details'].aggregate([
        {$match: {'ProductID': 7}},
        {$lookup: {
            from: 'orders',
            localField: 'OrderID',
            foreignField: 'OrderID',
            as: 'Customers'
        }},
        {$unwind: '$Customers'},

        {$lookup: {
            from: 'orders',
            localField: 'Customers.CustomerID',
            foreignField: 'CustomerID',
            as: 'Orders'
        }},
        {$unwind: '$Orders'},
        {$lookup: {
            from: 'order-details',
            localField: 'Orders.OrderID',
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
        {$group: {
            _id: '$Products.ProductName',
            count: {$sum: 1},
        }},
    ])

    # for post in db.customers.find({'CustomerID': {}}):
    #     print(post['CustomerID'])
