from backend import db_helper
import pytest

def test_fetch_expense_for_data():
    expenses = db_helper.fetch_expense_for_data('2024-08-15')

    assert len(expenses) == 1
    assert expenses[0]['amount'] == 10
    assert expenses[0]['category'] == "Shopping"
    assert expenses[0]['notes'] == "Bought potatoes"