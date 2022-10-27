---
title: "[Python] Credit Card Validation"
date: 2022-10-27 08:00:00 -0400
categories: python credit card validation
---

This is a credit card validation with Luhn's Algorithm

1. Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
2. Add the sum to the sum of the digits that weren’t multiplied by 2.
3. If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid.

Ex)

Card Number: 4003600000000014

Multiply each of the underlined digits by 2:

`1•2 + 0•2 + 0•2 + 0•2 + 0•2 + 6•2 + 0•2 + 4•2`

That gives us:

`2 + 0 + 0 + 0 + 0 + 12 + 0 + 8`

Now let’s add those products’ digits (i.e., not the products themselves) together:

`2 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 8 = 13`

Add that sum (13) to the sum of the digits that weren’t multiplied by 2 (starting from the end):

`13 + 4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 20`

The last digit in that sum (20) is a 0, then the card number is valid.

```python
from cs50 import get_int
import re

divider = 10000000000000


def main():
    card_number = get_int("Enter credit card number: ")
    size = validate_card_type(card_number)
    is_valid = validate_card_numbers(card_number)

    if size == 0 or is_valid > 0:
        print("INVALID")


def validate_card_type(card_number):
    size = is_amex(card_number)
    if size > 0:
        return size

    size = is_master(card_number)
    if size > 0:
        return size

    size = is_visa(card_number)
    if size > 0:
        return size

    return size


def validate_card_numbers(card_number):
    odds = str(card_number)[0::2]
    evens = str(card_number)[1::2]

    result = 0
    for num in odds:
        multiplied = int(num) * 2
        if (multiplied < 10):
            result += multiplied
        else:
            str_num = str(multiplied)
            result += int(str_num[0])
            result += int(str_num[1])

    for num in evens:
        result += int(num)

    return result % 10


def is_amex(card_number):
    number = int(card_number / divider)
    if number + 66 == 100 or number + 63 == 100:
        print("AMEX")
        return 15
    else:
        return 0


def is_master(card_number):
    # Master 16 digit and start 51,52,53,54, 55
    r = re.search("^[5][1-5]", str(card_number))

    if r:
        print("MASTERCARD")
        return 16
    else:
        return 0


def is_visa(card_number):
    # Visa 13 16 digit and start with 4
    r = re.match("^[4]", str(card_number))
    l = len(str(card_number))

    if r and (l == 16 or l == 13):
        print("VISA")
        return 16
    else:
        return 0


if __name__ == "__main__":
    main()
    
```
