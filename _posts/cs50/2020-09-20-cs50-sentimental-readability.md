---
title: "[Python] Readability"
date: 2022-10-27 08:00:00 -0400
categories: python readability cs50
---

Python version of Readability

The Coleman-Liau index of a text is designed to output that (U.S.) grade level that is needed to understand some text

Formula
`index = 0.0588 * L - 0.296 * S - 15.8`

```python
from cs50 import get_string
import re


def main():
    text = get_string("Text: ")

    cnt_l = len(re.findall("[a-zA-Z]", text))
    cnt_w = len(text.split())
    cnt_s = len(re.split('[.]|[?]|[!]', text))
    cnt_s -= 1

    # get avg of letters per 100 words
    L = round((cnt_l * 100) / cnt_w, 2)
    # get avg of sentences per 100 words
    S = round((cnt_s * 100) / cnt_w, 2)
    index = round(0.0588 * L - 0.296 * S - 15.8)
    print_grade(index)


def print_grade(index):
    if (index < 1):
        return print("Before Grade 1")
    if (index >= 16):
        return print("Grade 16+")
    print(f"Grade {index}")


main()

```
