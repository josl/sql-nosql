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


def ex3SQLite():
    c = conn.cursor()
    customerID = 'ALFKI'

    query = '''
        SELECT * FROM "Order Details Extended",
            (
                SELECT Orders.OrderID, COUNT(Orders.OrderID)
                    AS NumberOfProducts
                FROM "Orders", "Order Details Extended"
                USING ("OrderID")
                WHERE Orders.CustomerID="ALFKI"
                GROUP BY "Order Details Extended".OrderID
            ) as ALFKI_count USING ("OrderID")
            WHERE ALFKI_count.NumberOfProducts >= 2;
    ''' % customerID

    orders = [order for order in c.execute(query)]
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.§
    conn.close()
    return orders


def ex3Mongo():
    # db.orders.aggregate([
    #     {$match: {'CustomerID': 'ALFKI'}},
    #     {$lookup: {
    #         from: 'order-details',
    #         localField: 'OrderID',
    #         foreignField: 'OrderID',
    #         as: 'Products'
    #     }},
    #     {$project: {
    #         'OrderID': 1,
    #         'Products.ProductName': 1,
    #         'Products.ProductID': 1,
    #         'NumberOfProducts': {$size: "$Products"},
    #         _id: 0
    #     }},
    #     {$unwind: '$Products'},
    #     {$lookup: {
    #         from: 'products',
    #         localField: 'Products.ProductID',
    #         foreignField: 'ProductID',
    #         as: 'Products'
    #     }},
    #     {$match: {'NumberOfProducts': {$gte: 2}}}
    # ])
    pipeline = [
        {'$match': {'CustomerID': 'ALFKI'}},
        {'$lookup': {
            'from': 'order-details',
            'localField': 'OrderID',
            'foreignField': 'OrderID',
            'as': 'Products'
        }},
        {'$project': {
            'OrderID': 1,
            'Products.ProductName': 1,
            'Products.ProductID': 1,
            'NumberOfProducts': {'$size': "$Products"},
            '_id': 0
        }},
        {'$unwind': '$Products'},
        {'$lookup': {
            'from': 'products',
            'localField': 'Products.ProductID',
            'foreignField': 'ProductID',
            'as': 'Products'
        }},
        {'$match': {'NumberOfProducts': {'$gte': 2}}},
        {'$project': {
            'OrderID': 1,
            'Products.ProductName': 1,
            'Products.ProductID': 1,
            'NumberOfProducts': 1,
            '_id': 0
        }},
    ]
    for orders in db.orders.aggregate(pipeline):
        print(orders)
    # {'Products': [{'ProductID': 28, 'ProductName': 'Rössle Sauerkraut'}], 'NumberOfProducts': 3, 'OrderID': 10643}
    # {'Products': [{'ProductID': 46, 'ProductName': 'Spegesild'}], 'NumberOfProducts': 3, 'OrderID': 10643}
    # {'Products': [{'ProductID': 39, 'ProductName': 'Chartreuse verte'}], 'NumberOfProducts': 3, 'OrderID': 10643}
    # {'Products': [{'ProductID': 3, 'ProductName': 'Aniseed Syrup'}], 'NumberOfProducts': 2, 'OrderID': 10702}
    # {'Products': [{'ProductID': 76, 'ProductName': 'Lakkalikööri'}], 'NumberOfProducts': 2, 'OrderID': 10702}
    # {'Products': [{'ProductID': 59, 'ProductName': 'Raclette Courdavault'}], 'NumberOfProducts': 2, 'OrderID': 10835}
    # {'Products': [{'ProductID': 77, 'ProductName': 'Original Frankfurter grüne Soße'}], 'NumberOfProducts': 2, 'OrderID': 10835}
    # {'Products': [{'ProductID': 6, 'ProductName': "Grandma's Boysenberry Spread"}], 'NumberOfProducts': 2, 'OrderID': 10952}
    # {'Products': [{'ProductID': 28, 'ProductName': 'Rössle Sauerkraut'}], 'NumberOfProducts': 2, 'OrderID': 10952}
    # {'Products': [{'ProductID': 71, 'ProductName': 'Flotemysost'}], 'NumberOfProducts': 2, 'OrderID': 11011}
    # {'Products': [{'ProductID': 58, 'ProductName': 'Escargots de Bourgogne'}], 'NumberOfProducts': 2, 'OrderID': 11011}
