---
title: "[SQL] Duplicate entry of Primary Index"
date: 2021-10-14 08:00:00 -0400
categories: sql debug
---

If you see Duplicate entry of Primary Index (Primary Key) Error
Then most of case might be an user clicked request multiple times or query executed multiple times.

If you can solve it from frondend, the event should be unbinded until get the response.
If you want to backend solved, try below samples depends on your business logic.

### INSERT IGNORE

`Ignore when the key is duplicated`

```sql
INSERT IGNORE 
INTO `user`(`email`, `id`) 
VALUES('sample@gmail.com', 'testuser');
```

### REPLACE INTO

`DELETE EXISTING ROW and INSERT NEW ROW`

```sql
REPLACE INTO `user`(`email`, `id`) 
VALUES('sample@gmail.com', 'testuser');
```

### ON DUPLICATE KEY UPDATE

`UPDATE ROW when the key is duplicated`

```sql
INSERT INTO `user`(`email`, `id`) 
VALUES('sample@gmail.com', 'testuser')
    ON DUPLICATE KEY UPDATE `id`=VALUES(`id`);
```