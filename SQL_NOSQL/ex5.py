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


def ex5SQLite():
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

def ex5Mongo():
    # db['order-details'].aggregate([
    #     {$match: {'ProductID': 7}},
    #     {$lookup: {
    #         from: 'orders',
    #         localField: 'OrderID',
    #         foreignField: 'OrderID',
    #         as: 'Customers'
    #     }},
    #     {$unwind: '$Customers'},
    #
    #     {$lookup: {
    #         from: 'orders',
    #         localField: 'Customers.CustomerID',
    #         foreignField: 'CustomerID',
    #         as: 'Orders'
    #     }},
    #     {$unwind: '$Orders'},
    #     {$lookup: {
    #         from: 'order-details',
    #         localField: 'Orders.OrderID',
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
    #     {$group: {
    #         _id: '$Products.ProductName',
    #         count: {$sum: 1},
    #     }},
    # ])
    pipeline = [
        {'$match': {'ProductID': 7}},
        {'$lookup': {
            'from': 'orders',
            'localField': 'OrderID',
            'foreignField': 'OrderID',
            'as': 'Customers'
        }},
        {'$unwind': '$Customers'},

        {'$lookup': {
            'from': 'orders',
            'localField': 'Customers.CustomerID',
            'foreignField': 'CustomerID',
            'as': 'Orders'
        }},
        {'$unwind': '$Orders'},
        {'$lookup': {
            'from': 'order-details',
            'localField': 'Orders.OrderID',
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
        {'$group': {
            '_id': '$Products.ProductName',
            'count': {'$sum': 1},
        }},
    ]
    for products in db['order-details'].aggregate(pipeline):
        print(products)
    print(len(list(db['order-details'].aggregate(pipeline))))
    # {'_id': ['Mishi Kobe Niku'], 'count': 2}
    # {'_id': ['Gravad lax'], 'count': 2}
    # {'_id': ['Genen Shouyu'], 'count': 2}
    # {'_id': ['Rössle Sauerkraut'], 'count': 9}
    # {'_id': ['Rogede sild'], 'count': 6}
    # {'_id': ['Singaporean Hokkien Fried Mee'], 'count': 17}
    # {'_id': ['Maxilaku'], 'count': 10}
    # {'_id': ['Boston Crab Meat'], 'count': 20}
    # {'_id': ["Sirop d'érable"], 'count': 9}
    # {'_id': ['Longlife Tofu'], 'count': 7}
    # {'_id': ["Gustaf's Knäckebröd"], 'count': 8}
    # {'_id': ['Vegie-spread'], 'count': 7}
    # {'_id': ['Gudbrandsdalsost'], 'count': 13}
    # {'_id': ['Carnarvon Tigers'], 'count': 13}
    # {'_id': ['Outback Lager'], 'count': 19}
    # {'_id': ['Gumbär Gummibärchen'], 'count': 13}
    # {'_id': ['Thüringer Rostbratwurst'], 'count': 12}
    # {'_id': ['Tourtière'], 'count': 17}
    # {'_id': ['Teatime Chocolate Biscuits'], 'count': 12}
    # {'_id': ['Spegesild'], 'count': 17}
    # {'_id': ['Original Frankfurter grüne Soße'], 'count': 24}
    # {'_id': ['Chartreuse verte'], 'count': 16}
    # {'_id': ['Escargots de Bourgogne'], 'count': 7}
    # {'_id': ['Queso Cabrales'], 'count': 17}
    # {'_id': ['Geitost'], 'count': 20}
    # {'_id': ['Tunnbröd'], 'count': 13}
    # {'_id': ['Queso Manchego La Pastora'], 'count': 9}
    # {'_id': ['Gula Malacca'], 'count': 11}
    # {'_id': ['Ikura'], 'count': 24}
    # {'_id': ['Chai'], 'count': 13}
    # {'_id': ['Northwoods Cranberry Sauce'], 'count': 9}
    # {'_id': ["Sir Rodney's Scones"], 'count': 12}
    # {'_id': ['Camembert Pierrot'], 'count': 29}
    # {'_id': ["Grandma's Boysenberry Spread"], 'count': 9}
    # {'_id': ['Pavlova'], 'count': 21}
    # {'_id': ['Nord-Ost Matjeshering'], 'count': 13}
    # {'_id': ["Chef Anton's Cajun Seasoning"], 'count': 13}
    # {'_id': ['Louisiana Hot Spiced Okra'], 'count': 7}
    # {'_id': ['Lakkalikööri'], 'count': 18}
    # {'_id': ['Guaraná Fantástica'], 'count': 18}
    # {'_id': ['Manjimup Dried Apples'], 'count': 23}
    # {'_id': ['NuNuCa Nuß-Nougat-Creme'], 'count': 9}
    # {'_id': ['Schoggi Schokolade'], 'count': 7}
    # {'_id': ['Pâté chinois'], 'count': 18}
    # {'_id': ['Zaanse koeken'], 'count': 13}
    # {'_id': ['Steeleye Stout'], 'count': 20}
    # {'_id': ['Perth Pasties'], 'count': 14}
    # {'_id': ['Ravioli Angelo'], 'count': 12}
    # {'_id': ["Uncle Bob's Organic Dried Pears"], 'count': 49}
    # {'_id': ['Côte de Blaye'], 'count': 13}
    # {'_id': ['Konbu'], 'count': 23}
    # {'_id': ['Filo Mix'], 'count': 12}
    # {'_id': ['Flotemysost'], 'count': 25}
    # {'_id': ['Sasquatch Ale'], 'count': 6}
    # {'_id': ["Sir Rodney's Marmalade"], 'count': 13}
    # {'_id': ['Mascarpone Fabioli'], 'count': 8}
    # {'_id': ['Aniseed Syrup'], 'count': 11}
    # {'_id': ['Wimmers gute Semmelknödel'], 'count': 22}
    # {'_id': ['Rhönbräu Klosterbier'], 'count': 25}
    # {'_id': ['Mozzarella di Giovanni'], 'count': 25}
    # {'_id': ['Röd Kaviar'], 'count': 6}
    # {'_id': ['Ipoh Coffee'], 'count': 17}
    # {'_id': ['Valkoinen suklaa'], 'count': 2}
    # {'_id': ['Inlagd Sill'], 'count': 9}
    # {'_id': ['Scottish Longbreads'], 'count': 18}
    # {'_id': ['Chang'], 'count': 27}
    # {'_id': ['Louisiana Fiery Hot Pepper Sauce'], 'count': 21}
    # {'_id': ['Alice Mutton'], 'count': 26}
    # {'_id': ['Gorgonzola Telino'], 'count': 28}
    # {'_id': ['Tarte au sucre'], 'count': 38}
    # {'_id': ['Raclette Courdavault'], 'count': 25}
    # {'_id': ['Tofu'], 'count': 11}
    # {'_id': ["Chef Anton's Gumbo Mix"], 'count': 9}
    # {'_id': ['Gnocchi di nonna Alice'], 'count': 29}
    # {'_id': ['Chocolade'], 'count': 3}
    # {'_id': ["Jack's New England Clam Chowder"], 'count': 32}
