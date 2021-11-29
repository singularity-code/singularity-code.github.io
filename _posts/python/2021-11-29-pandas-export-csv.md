---
title: "[Python] Pandas export as a csv file"
date: 2021-11-29 11:00:00 -0400
categories: python pandas export csv
---

Sample code that how to export data as a csv using pandas library.
this function will create `filename` string with date as a actual filename.

```python
from datetime import datetime
import pandas

def export_csv(_data, _headers, _filename):
	date = datetime.today().date()
	df = pandas.DataFrame(_data)
	path = 'C:\\download\\csv\\' + _filename + str(date) + '.csv'
	df.to_csv(path, header=_headers, index=False, encoding='utf-8-sig')
```

```python
# Usage
headers = ['A', 'B', 'C'];
data = [];
export_csv(data, headers, 'sample');
```