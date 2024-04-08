import csv
import psycopg2

with psycopg2.connect(
        host="localhost",
        database="north",
        user="postgres",
        password="12345"
) as connection:

    with connection.cursor() as cursor:
        # Добавление данных в таблицу employees
        with open('north_data\\employees_data.csv') as csv_file:
            header = next(csv_file)
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                query = """INSERT INTO employees 
                VALUES (%s, %s, %s, %s, %s, %s)"""
                cursor.execute(query, row)

        # Добавление данных в таблицу customers
        with open('north_data\\customers_data.csv') as csv_file:
            header = next(csv_file)
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                query = """INSERT INTO customers 
                VALUES (%s, %s, %s)"""
                cursor.execute(query, row)

        # Добавление данных в таблицу orders
        with open('north_data\\orders_data.csv') as csv_file:
            header = next(csv_file)
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                query = """INSERT INTO orders 
                VALUES (%s, %s, %s, %s, %s)"""
                cursor.execute(query, row)

connection.close()