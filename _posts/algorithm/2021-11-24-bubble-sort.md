---
title: "[Algorithm] Bubble Sort"
date: 2021-11-24 08:00:00 -0400
categories: algorithm bubble sort c
---

This example shows that `Bubble Sort` custom type in C.

Place largest number to the end of an array when it sorted.

```c
// guess that other library is already included such as stdio.h

typedef struct
{
    string name;
    int scores;
} candidate;

candidate candidates[9];

int bubble_sort()
{
    int sort_counter = 0;
    for (int i = 0; i < 8; i++)
    {
        if (candidates[i + 1].name != NULL && (candidates[i].scores > candidates[i + 1].scores))
        {
            // swap large number to end of an array
            swap(&candidates[i], &candidates[i + 1]);
            sort_counter++;
        }
    }
    // if not sorted, repeat
    if (sort_counter > 0)
    {
        sort_counter = bubble_sort();
    }
    return sort_counter;
}

void swap(candidate *a, candidate *b)
{
    candidate tmp = *a;
    *a = *b;
    *b = tmp;
}
```

```c
// get the largest one with end element of an array
candidate result = candidates[9];
```
