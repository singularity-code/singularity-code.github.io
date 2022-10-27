---
title: "[Python] Check Null or N/A or empty String"
date: 2021-11-25 08:00:00 -0400
categories: python string check null
---

Sample function to check if string is `None` or empty `""` or "N/A" or "-"

return true if str is not contains conditions.

```python
def is_not_blank_or_na(str):
	return bool(str and str.strip()) and not bool(str == 'N/A' or str == '-' or str.startswith(' ') or str == 'None' or str is None)
```
