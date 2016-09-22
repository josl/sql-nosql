# SQL & NoSQL

Exercise 5 of 02807 Computational Tools for Big Data at DTU

## Content:

This week, we will take a look at two of the most common tools for storing data records: relational and NoSQL databases. Broadly speaking, a database is a software system that is engineered to store and query data efficiently, and typically also has some enterprisey features (such as providing easy backups or provinding different user access roles).

Perhaps the core classic feature of relational databases is that they generally provide ACID (atomicity, consistency, isolation, durability) guarantees, whereas typically NoSQL databases omit these to some extent, and instead allows for greater flexibility in the use of the database. These are guarantees that ensure that data is read and written in such a way that it is easy to reason about the state of the data (e.g. either a query fails or it succeeds, halfway completed operations cannot occur).

## Learning objectives:

After this week, you are supposed to know:

- The difference between relational and NoSQL databases
- How to setup and use a SQLite database
- How to setup and use a MongoDB database
- How to query both databases from Python using PyMongo and Sqlite3

## Resources:

- Reading: Read about the difference between SQL and NoSQL
- Video: Watch Martin Fowler explain the history and different types of NoSQL databases, and a comparison with relational databases.
- Reading: Read the Sqlite3 tutorial
- Reading: Read the PyMongo tutorial
- Tutorial: Familiarise yourself with the SQL language through the interactive tutorials at W3Schools. For SQL syntax reference, this is the place to go!

## Exercises:

In the following you will play around with querying and returning data from first a SQLite, and then a Mongo database. For simplicity the exercises are designed such that you complete each one twice, first using a SQLite database system and then using a Mongo database system. Both databases store the same information, which should reflect in your answers.

With each answer given, please provide both your queries (and code) and the returned data (data shortened if very long!). The exercises are meant to familiarize you with the query languages, so you should only use Python functionality in places where the languages come up short – i.e. solving the problems in single queries is better solving them in many (even though this may not always be an option). Comments and thoughts on differences in using the two systems are encouraged. You may structure your answers in whichever way you find most readable.

### Exercise 5.1:

For SQLite: Establish connection to this database in Python (use the sqlite3 module). Document the connection by making some simple queries.

For Mongo: To get started, clone this repository into your working directory. Start a running instance of MongoDB* (on command-line: mongod), then run the .sh file in a terminal. This should create a live Mongo database named ‘Northwind’ that you can connect to in Python. Document the connection by making some simple queries.

 *Make sure you have MongoDB installed.

### Exercise 5.2:

The customer with customerID ALFKI has made a number of orders containing some products. Query for, and return, all orders made by ALFKI and the products they contain.

### Exercise 5.3:

Get all orders (with products) made by ALFKI that contain at least 2 product types.

### Exercise 5.4:

Determine how many and who ordered “Uncle Bob’s Organic Dried Pears” (productID 7).

### Exercise 5.5:

How many different and which products have been ordered by customers who have also ordered “Uncle Bob’s Organic Dried Pears”?
## Install

It's recommended to create a virtual environment (conda env preffered)
``` bash
make setup
```
## Usage

## Testing

# Unit test
``` bash
make unit
```


## License
MIT © [Jose Luis Bellod Cisneros](http://josl.github.io)
