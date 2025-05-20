## CASCADE

In general, **"CASCADE"** means something that happens in a **chain reaction**, where one action leads to another automatically.

In **databases**, especially in **SQL and Django**, **CASCADE** is used with **foreign keys** to define what happens when a related record is deleted or updated.

### Example in SQL/Django:

If you have two tables/models:  
- `Author`  
- `Book` (which has a foreign key to `Author`)

And you use:

```python
author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

It means:
> If an **Author** is deleted, then **all related Books** are also deleted automatically.

### Summary:
- **CASCADE** = Delete or update **related records automatically**.
- It helps keep the database clean and prevents broken references.
