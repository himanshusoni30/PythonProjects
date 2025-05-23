import pytest
import freecodecamp.LuhnAlgorithm as la

zero_card_number = '0000-0000-0000-0000'
invalid_card_number = '4111-1111-4555-1141'
valid_card_number = '4111-1111-4655-1141'
comma_separated_card_number = '4111,1111-4655-1141'
card_number_with_whitespaces = '4111 1111 4655 1141'
empty_card_number = ''
non_numeric_card_number = 'A111-1111-4655-1141'

def test_luhn_algorithm_with_empty_card_number():
    with pytest.raises(ValueError, match='Card number is empty!!!'):
        la.verify_card_number(empty_card_number)
        la.verify_card_number_using_negative_indexes(empty_card_number)

def test_luhn_algorithm_with_non_numeric_card_number():
    with pytest.raises(ValueError, match=r'Card contains other than digits: .*'):
        la.verify_card_number(non_numeric_card_number)
        la.verify_card_number_using_negative_indexes(non_numeric_card_number)

def test_luhn_algorithm_with_card_number_having_all_zeroes():
    assert la.verify_card_number(zero_card_number)
    assert la.verify_card_number_using_negative_indexes(zero_card_number)

def test_luhn_algorithm_with_card_number_with_whitespaces():
    assert la.verify_card_number(card_number_with_whitespaces)
    assert la.verify_card_number_using_negative_indexes(card_number_with_whitespaces)

def test_luhn_algorithm_with_comma_separated_card_number():
    assert la.verify_card_number(comma_separated_card_number)
    assert la.verify_card_number_using_negative_indexes(comma_separated_card_number)

def test_luhn_algorithm_with_invalid_card_number():
    assert not la.verify_card_number(invalid_card_number)
    assert not la.verify_card_number_using_negative_indexes(invalid_card_number)

def test_luhn_algorithm_with_valid_card_number():
    assert not la.verify_card_number(valid_card_number)
    assert not la.verify_card_number_using_negative_indexes(valid_card_number)
