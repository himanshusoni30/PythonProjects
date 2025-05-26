from cmath import *

import pytest

import freecodecamp.ExpenseTracker as et

@pytest.mark.parametrize('amount, category, expected', [(inf, 'Universe', inf), (-inf, 'Universe', -inf), ('-0.0000001', 'Universe', float('-0.0000001')), (pi, 'Universe', pi)])
def test_total_expenses_when_amount_is_accepted_as_float(amount, category, expected):
    expenses = []
    et.add_expense(expenses, float(amount), category)
    et.print_expenses(expenses)
    assert et.total_expenses(expenses) == expected

@pytest.mark.parametrize('amount, category, expected', [(10000000000, 'Universe', 10000000000), (-10000000000, 'Universe', -10000000000), ('-100', 'Universe', int('-100')), (0, 'Universe', int('000')), (0, 'Universe', int('000'))])
def test_total_expenses_when_amount_is_accepted_as_int(amount, category, expected):
    expenses = []
    et.add_expense(expenses, int(amount), category)
    et.print_expenses(expenses)
    assert et.total_expenses(expenses) == expected

def test_total_expenses_when_amount_is_nan():
    expenses = []
    et.add_expense(expenses, nan, 'Universe')
    assert isnan(et.total_expenses(expenses))

def test_total_expenses_when_amount_is_none():
    expenses = []
    et.add_expense(expenses, None, 'Universe')
    with pytest.raises(TypeError):
        et.total_expenses(expenses)

def test_add_expenses():
    expenses = []
    et.add_expense(expenses, float(10), 'Fruit')
    et.add_expense(expenses, float(15), 'Clothes')
    et.add_expense(expenses, float(21), 'Milk')
    et.add_expense(expenses, float(15.2), 'Milk')
    et.add_expense(expenses, float(6.05), 'Fruit')
    et.add_expense(expenses, float(2.5), 'Clothes')
    assert len(expenses) == 6

def test_total_expenses_after_adding_expenses():
    expenses = []
    et.add_expense(expenses, float(10), 'Fruit')
    et.add_expense(expenses, float(15), 'Clothes')
    et.add_expense(expenses, float(21), 'Milk')
    et.add_expense(expenses, float(15.2), 'Milk')
    et.add_expense(expenses, float(6.05), 'Fruit')
    et.add_expense(expenses, float(2.5), 'Clothes')
    assert et.total_expenses(expenses) == sum([10,15,21,15.2,6.05,2.5])

def test_total_expenses_after_adding_expenses_filtered_by_category():
    expenses = []
    et.add_expense(expenses, float(10), 'Fruit')
    et.add_expense(expenses, float(15), 'Clothes')
    et.add_expense(expenses, float(21), 'Milk')
    et.add_expense(expenses, float(15.2), 'Milk')
    et.add_expense(expenses, float(6.05), 'Fruit')
    et.add_expense(expenses, float(2.5), 'Clothes')
    assert et.total_expenses(et.filter_expenses_by_category(expenses, 'Fruit')) == sum([10,6.05])
    assert et.total_expenses(et.filter_expenses_by_category(expenses, 'Milk')) == sum([21,15.2])
    assert et.total_expenses(et.filter_expenses_by_category(expenses, 'Clothes')) == sum([15,2.5])
    assert et.total_expenses(et.filter_expenses_by_category(expenses, None)) == 0
    assert et.total_expenses(et.filter_expenses_by_category(expenses, 'fruit')) == 0
