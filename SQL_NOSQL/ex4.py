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

Determine how many and who ordered “Uncle Bob’s Organic Dried Pears”
(productID 7).
'''


def ex4SQLite():
    c = conn.cursor()
    productID = 7

    # How many producto each customer bought . This is the good one
    query = '''
            SELECT Customers.CustomerID, Customers.ContactTitle,
                   COUNT(Orders.OrderID) AS NumberOfProducts
            FROM Customers
                LEFT JOIN Orders
                    ON Customers.CustomerID = Orders.CustomerID
                LEFT JOIN "Order Details Extended"
                    ON "Order Details Extended".OrderID = Orders.OrderID
            WHERE "ProductID"="7"
            GROUP BY Orders.CustomerID
    ''' % productID

    # Customer who bought the product
    query = '''
            SELECT Customers.CustomerID, Customers.ContactTitle
            FROM Customers
                LEFT JOIN Orders
                    ON Customers.CustomerID = Orders.CustomerID
                LEFT JOIN "Order Details Extended"
                    ON "Order Details Extended".OrderID = Orders.OrderID
            WHERE "ProductID"="7"
            GROUP BY Orders.CustomerID
    ''' % productID
    c.execute(query)
    total = 0
    for customer in c.execute(query):
        print(customer[0])
        total += customer[2]
    print(total)
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    # conn.close()
    # return orders


def ex4Mongo():
    # db['order-details'].aggregate([
    #     {$match: {'ProductID': 7}},
    #     {$lookup: {
    #         from: 'orders',
    #         localField: 'OrderID',
    #         foreignField: 'OrderID',
    #         as: 'Customers'
    #     }},
    #     {$unwind: '$Customers'},
    #     {$group: {
    #         _id: '$Customers.CustomerID',
    #         count: {$sum: 1}
    #     }},
    #     {$lookup: {
    #         from: 'customers',
    #         localField: '_id',
    #         foreignField: 'CustomerID',
    #         as: 'Customers'
    #     }},
    #     {$project: {
    #         'Customers': '$Customers.ContactName',
    #         count: 1
    #     }},
    # ])
    # { "_id" : "LILAS", "count" : 1, "Customers" : [ "Carlos González" ] }
    # { "_id" : "OCEAN", "count" : 1, "Customers" : [ "Yvonne Moncada" ] }
    # { "_id" : "EASTC", "count" : 2, "Customers" : [ "Ann Devon" ] }
    # { "_id" : "SANTG", "count" : 1, "Customers" : [ "Jonas Bergulfsen" ] }
    # { "_id" : "REGGC", "count" : 2, "Customers" : [ "Maurizio Moroni" ] }
    # { "_id" : "LACOR", "count" : 1, "Customers" : [ "Daniel Tonini" ] }
    # { "_id" : "OTTIK", "count" : 2, "Customers" : [ "Henriette Pfalzheim" ] }
    # { "_id" : "GOURL", "count" : 1, "Customers" : [ "André Fonseca" ] }
    # { "_id" : "SAVEA", "count" : 1, "Customers" : [ "Jose Pavarotti" ] }
    # { "_id" : "ERNSH", "count" : 1, "Customers" : [ "Roland Mendel" ] }
    # { "_id" : "BONAP", "count" : 2, "Customers" : [ "Laurence Lebihan" ] }
    # { "_id" : "QUICK", "count" : 2, "Customers" : [ "Horst Kloss" ] }
    # { "_id" : "RATTC", "count" : 3, "Customers" : [ "Paula Wilson" ] }
    # { "_id" : "FOLIG", "count" : 1, "Customers" : [ "Martine Rancé" ] }
    # { "_id" : "FOLKO", "count" : 1, "Customers" : [ "Maria Larsson" ] }
    # { "_id" : "BSBEV", "count" : 2, "Customers" : [ "Victoria Ashworth" ] }
    # { "_id" : "VAFFE", "count" : 1, "Customers" : [ "Palle Ibsen" ] }
    # { "_id" : "VICTE", "count" : 2, "Customers" : [ "Mary Saveley" ] }
    # { "_id" : "BOTTM", "count" : 1, "Customers" : [ "Elizabeth Lincoln" ] }
    # { "_id" : "SPLIR", "count" : 1, "Customers" : [ "Art Braunschweiger" ] }
    pipeline = [
            {'$match': {'ProductID': 7}},
            {'$lookup': {
                'from': 'orders',
                'localField': 'OrderID',
                'foreignField': 'OrderID',
                'as': 'Customers'
            }},
            {'$unwind': '$Customers'},
            {'$group': {
                '_id': '$Customers.CustomerID',
                'count': {'$sum': 1}
            }},
            {'$lookup': {
                'from': 'customers',
                'localField': '_id',
                'foreignField': 'CustomerID',
                'as': 'Customers'
            }},
            {'$project': {
                'Customers': '$Customers.ContactName',
                'count': 1
            }},
        ]
    for customer in db['order-details'].aggregate(pipeline):
        print(customer)
    print(len(list(db['order-details'].aggregate(pipeline))))
    # {'Customers': ['Carlos González'], '_id': 'LILAS', 'count': 1}
    # {'Customers': ['Yvonne Moncada'], '_id': 'OCEAN', 'count': 1}
    # {'Customers': ['Ann Devon'], '_id': 'EASTC', 'count': 2}
    # {'Customers': ['Jonas Bergulfsen'], '_id': 'SANTG', 'count': 1}
    # {'Customers': ['Maurizio Moroni'], '_id': 'REGGC', 'count': 2}
    # {'Customers': ['Daniel Tonini'], '_id': 'LACOR', 'count': 1}
    # {'Customers': ['Henriette Pfalzheim'], '_id': 'OTTIK', 'count': 2}
    # {'Customers': ['André Fonseca'], '_id': 'GOURL', 'count': 1}
    # {'Customers': ['Jose Pavarotti'], '_id': 'SAVEA', 'count': 1}
    # {'Customers': ['Roland Mendel'], '_id': 'ERNSH', 'count': 1}
    # {'Customers': ['Laurence Lebihan'], '_id': 'BONAP', 'count': 2}
    # {'Customers': ['Horst Kloss'], '_id': 'QUICK', 'count': 2}
    # {'Customers': ['Paula Wilson'], '_id': 'RATTC', 'count': 3}
    # {'Customers': ['Martine Rancé'], '_id': 'FOLIG', 'count': 1}
    # {'Customers': ['Maria Larsson'], '_id': 'FOLKO', 'count': 1}
    # {'Customers': ['Victoria Ashworth'], '_id': 'BSBEV', 'count': 2}
    # {'Customers': ['Palle Ibsen'], '_id': 'VAFFE', 'count': 1}
    # {'Customers': ['Mary Saveley'], '_id': 'VICTE', 'count': 2}
    # {'Customers': ['Elizabeth Lincoln'], '_id': 'BOTTM', 'count': 1}
    # {'Customers': ['Art Braunschweiger'], '_id': 'SPLIR', 'count': 1}
