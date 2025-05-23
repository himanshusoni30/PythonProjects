'''
1. Double every second digit:
Starting from the rightmost digit, double every other digit in the number.
2. Sum digits:
If doubling results in a two-digit number (e.g., doubling 9 results in 18), sum the individual digits of that number (1 + 8 = 9).
3. Sum all digits:
Add all the resulting digits, including the doubled and single-digit numbers, together.
4. Check for validity:
If the final sum is divisible by 10, the identification number is considered valid.
'''

def validate_card_input(card_number):
    if len(card_number)==0:
        raise ValueError('Card number is empty!!!')
    if not card_number.isdigit():
        raise ValueError('Card contains other than digits: '+card_number)

def verify_card_number(card_number):
    decoded_card_number = card_translator(card_number)
    validate_card_input(decoded_card_number)
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    reversed_card_number = decoded_card_number[::-1]
    even_digits = reversed_card_number[1::2]
    for digit in even_digits:
        num = int(digit) * 2
        if num > 9:
            num = num//10 + num%10
        sum_of_even_digits += num
    odd_digits = reversed_card_number[0::2]
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
    return (sum_of_odd_digits + sum_of_even_digits) % 10 == 0


def verify_card_number_using_negative_indexes(card_number):
    decoded_card_number = card_translator(card_number)
    validate_card_input(decoded_card_number)
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    even_digits = decoded_card_number[-2:- len(decoded_card_number) - 1:-2]
    for digit in even_digits:
        num = int(digit) * 2
        if num > 9:
            num = num//10 + num%10
        sum_of_even_digits += num
    odd_digits = decoded_card_number[-1:- len(decoded_card_number) - 1:-2]
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
    return (sum_of_odd_digits + sum_of_even_digits) % 10 == 0

def card_translator(card_number):
    tranlator = str.maketrans({'-': '', ' ': '', ',': ''})
    return card_number.translate(tranlator)

def execute():
    # card_number = '4123-1234-6789-0987'
    # card_number = '4111-1111-4555-1141'
    # card_number = '4111-1111-4655-1141'
    card_number = '4111,1111-4655-1141'
    # card_number = ''
    # card_number = 'A111-1111-4655-1141'


    if verify_card_number(card_number) and verify_card_number_using_negative_indexes(card_number):
        print('VALID!')
    else:
        print('INVALID!')

execute()
