import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger('db_helper')

print("**file**:", __file__)
@contextmanager
def database_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='expense_manager'
        )
        if connection.is_connected():
            print("Connection is successful")
            yield connection
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        yield None
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Connection closed")


def fetch_all_record():

    with database_connection() as connection:
        if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM expenses")
            expenses = cursor.fetchall()

            for expense in expenses:
                print(expense)

            cursor.close()

def fetch_expense_for_data(expense_date):
    logger.info(f"fetch_expense_for_data called with {expense_date}")
    with database_connection() as connection:
        if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
            expenses = cursor.fetchall()

            for expense in expenses:
                print(expense)

            cursor.close()
            return expenses

def insert_expense(expense_date, amount, category, notes):
    logger.info(f"insert_expense called with date: {expense_date}, amount: {amount}, category: {category}, notes: {notes}")
    with database_connection() as connection:
        if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(
                "INSERT INTO expenses(expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
                (expense_date, amount, category, notes)
            )
            connection.commit()
            cursor.close()
            print("Expense inserted successfully")

def delete_expense_for_data(expense_date):
    logger.info(f"delete expense data called with {expense_date}")
    with database_connection() as connection:
        if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute('DELETE FROM expenses WHERE expense_date = %s', (expense_date,))
            connection.commit()
            cursor.close()


def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetch expense summary data called with {start_date} and {end_date}")
    with database_connection() as connection:
        if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute('''SELECT category, SUM(amount) AS total 
                            FROM expenses 
                            WHERE expense_date BETWEEN %s AND %s 
                            GROUP BY category''',
                            (start_date, end_date)

            )

        data = cursor.fetchall()
        return data

import os
if __name__ == "__main__":
    print("**file**:", os.path.dirname(__file__))
    expenses = fetch_expense_for_data('2024-08-01')
    print(expenses)

    #insert_expense('2024-08-09', 100, 'Food', 'fuska')
    #delete_expense_for_data('2024-08-09')


    summary = fetch_expense_summary('2024-08-01', '2024-08-03')
    for record in summary:
        print(record)