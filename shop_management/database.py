# pylint: disable=missing-docstring

import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self, host, username, password):
        try:
            self.connection = mysql.connector.connect(
                host=host, user=username, password=password
            )
            self.cursor = self.connection.cursor()
        except Error as e:
            print(f"Error connecting to MySQL: {e}")

    def create_database(self):
        try:
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS `BizTrack`")
            self.cursor.execute("USE `BizTrack`")
        except Error as e:
            print(f"Error creating database: {e}")

    def create_table(self):
        try:
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS `products`(
                    id INT AUTO_INCREMENT PRIMARY KEY, 
                    name VARCHAR(255) NOT NULL, 
                    price DECIMAL(10, 2) NOT NULL, 
                    quantity INT NOT NULL
                )"""
            )
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS `sales` (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    product_name VARCHAR(255) NOT NULL, 
                    quantity INT, 
                    total_price DECIMAL(10, 2),
                    sales_date DATE NOT NULL
                )"""
            )
        except Error as e:
            print(f"Error creating table: {e}")

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params or ())
            self.connection.commit()
        except Error as e:
            print(f"Error executing query: {e}")

    def fetch_all(self, query, params=None):
        try:
            self.cursor.execute(query, params or ())
            return self.cursor.fetchall()
        except Error as e:
            print(f"Error fetching data: {e}")
            return []

    def fetch_one(self, query, params=None):
        try:
            self.cursor.execute(query, params or ())
            return self.cursor.fetchone()
        except Error as e:
            print(f"Error fetching data: {e}")
            return None
