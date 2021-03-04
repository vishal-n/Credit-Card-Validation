
### Usage: python validate_credit_card.py card_number
### Example: python validate_credit_card.py 4016870202644910

import re
import sys

def sum_digits(numeric_string):
    return sum([int(d) for d in numeric_string])


def valid_length_cc(cc_candidate):
    return len(cc_candidate) == 16 or len(cc_candidate) == 15


def check_sum(numeric_string):
    odds = numeric_string[:-1][::-2]
    evens = numeric_string[::-2]
    return sum([int(i) for i in odds]) + sum([sum_digits(str(int(i) * 2)) for i in evens])


def find_check_digit(numeric_string):
    return (check_sum(numeric_string) * 9) % 10


def is_luhn_valid(candidate):
    if candidate.isdigit():
        check_digit = int(candidate[-1:])
        return (check_sum(candidate[:-1]) + check_digit) % 10 == 0
    else:
        return False

def is_valid_cc(candidate):

    return check_regex(candidate) and valid_length_cc(candidate) and is_luhn_valid(candidate)

def check_regex(candidate):
    pattern = "^((4\d{3})|(5[1-5]\d{2})|(6011)|(7\d{3}))-?\d{4}-?\d{4}-?\d{4}|3[4,7]\d{13}$"
    r = re.compile(pattern)
    return bool(r.match(candidate))

if __name__ == '__main__':
    if(is_valid_cc(str(sys.argv[1])) == True):
        print("Valid!")
    else:
        print("Invalid!")