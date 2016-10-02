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
    # db.orders.aggregate([
    #     {$match: {'CustomerID': 'ALFKI'}},
    #     {$lookup: {
    #         from: 'order-details',
    #         localField: 'OrderID',
    #         foreignField: 'OrderID',
    #         as: 'Products'
    #     }},
    #     {$unwind: '$Products'},
    #     {$lookup: {
    #         from: 'products',
    #         localField: 'Products.ProductID',
    #         foreignField: 'ProductID',
    #         as: 'Products'
    #     }},
    #     {$project: {
    #         'OrderID': 1,
    #         'Products.ProductName': 1,
    #         'Products.ProductID': 1
    #     }},
    # ])
    pipeline = [
        {'$match': {'CustomerID': 'ALFKI'}},
        {'$lookup': {
            'from': 'order-details',
            'localField': 'OrderID',
            'foreignField': 'OrderID',
            'as': 'Products'
        }},
        {'$unwind': '$Products'},
        {'$lookup': {
            'from': 'products',
            'localField': 'Products.ProductID',
            'foreignField': 'ProductID',
            'as': 'Products'
        }},
        {'$project': {
            'OrderID': 1,
            'Products.ProductName': 1,
            'Products.ProductID': 1,
            '_id': 0
        }},
    ]
    for orders in db.orders.aggregate(pipeline):
        print(orders)

    # {'Products': [{'ProductID': 28, 'ProductName': 'Rössle Sauerkraut'}], 'OrderID': 10643}
    # {'Products': [{'ProductID': 46, 'ProductName': 'Spegesild'}], 'OrderID': 10643}
    # {'Products': [{'ProductID': 39, 'ProductName': 'Chartreuse verte'}], 'OrderID': 10643}
    # {'Products': [{'ProductID': 63, 'ProductName': 'Vegie-spread'}], 'OrderID': 10692}
    # {'Products': [{'ProductID': 3, 'ProductName': 'Aniseed Syrup'}], 'OrderID': 10702}
    # {'Products': [{'ProductID': 76, 'ProductName': 'Lakkalikööri'}], 'OrderID': 10702}
    # {'Products': [{'ProductID': 59, 'ProductName': 'Raclette Courdavault'}], 'OrderID': 10835}
    # {'Products': [{'ProductID': 77, 'ProductName': 'Original Frankfurter grüne Soße'}], 'OrderID': 10835}
    # {'Products': [{'ProductID': 6, 'ProductName': "Grandma's Boysenberry Spread"}], 'OrderID': 10952}
    # {'Products': [{'ProductID': 28, 'ProductName': 'Rössle Sauerkraut'}], 'OrderID': 10952}
    # {'Products': [{'ProductID': 71, 'ProductName': 'Flotemysost'}], 'OrderID': 11011}
    # {'Products': [{'ProductID': 58, 'ProductName': 'Escargots de Bourgogne'}], 'OrderID': 11011}
