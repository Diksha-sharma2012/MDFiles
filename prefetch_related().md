 # Understanding Forward and Reverse Foreign Keys in Django

#### When reading the topics related to Django's select_related() and prefetch_related() on some websites including Stack Overflow, I frequently see the words Forward Foreign Key and Reverse Foreign Key but I couldn't find the definitions on Django Documentation:

# `models.py`

```py 
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=5)  
```
### So, what are Forward Foreign Key and Reverse Foreign Key in Django?

* <B>Forward Foreign Key</B> means that the child model which has the foreign key to the parent model accesses the parent model.

*<B> Reverse Foreign Key</B> means that a parent model accesses the child model which has the foreign key to the parent model.

So in your case, because Product model has the foreign key to Category model so Category model is a parent model and Product model is a child model as shown below:

# `models.py`
``` PY
from django.db import models

class Category(models.Model): # Parent model
    name = models.CharField(max_length=20)

class Product(models.Model): # Child model
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=5)
```
<B>Forward Foreign Key</B>
The child model Product accesses the parent model Category with obj.category.name as shown below:
``` PY
for obj in Product.objects.all():
    print(obj.category.name) # Here
```    
<B>Reverse Foreign Key</B>
The parent model Category accesses the child model Product with obj.product_set.all() as shown below:
``` PY
for obj in Category.objects.all():
    print(obj.product_set.all()) # Here
```    
  

#  What is `prefetch_related()`?

Django’s `prefetch_related()` is used to **load related data more efficiently** from the database, especially when you are dealing with:

-  `ManyToMany` relationships
-  Reverse `ForeignKey` relationships (like `related_name`)

---

## ❓ Why use it?

If you don’t use `prefetch_related()`, Django may hit the database **again and again in a loop** — which is **slow** and causes what's known as the **N+1 query problem**.

---

##  Simple Example

###  Models:

```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
```
* One book can have many authors

* One author can write many books → this is a ManyToMany relationship

* Without prefetch_related():
``` PY
books = Book.objects.all() 
for book in books:
    print(book.title)
    for author in book.authors.all():  # Django makes 1 query per book
        print(author.name)
```        
#### If you have 10 books, Django will make:

* 1 query to get all books
* 10 queries (one for each book's authors)

➡️ Total = 11 queries  
➡️ This is the N+1 problem

###  With prefetch_related():
``` PY
books = Book.objects.prefetch_related('authors')

for book in books:
    print(book.title)
    for author in book.authors.all():  # No extra query here!
        print(author.name)
```        
#### Django runs only 2 queries:
* One for all books
* One for all authors linked to those books

##  When to use prefetch_related()?
#### Use it when:

* You are accessing ManyToMany or reverse ForeignKey fields
* You want to avoid slow performance due to many database queries

<B>👨‍🎓 Another Example</B>
``` PY
class Category(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
```    
#### Now fetch all categories and their products:
``` PY 
categories = Category.objects.prefetch_related('products')

for cat in categories:
    print(cat.name)
    for product in cat.products.all():  # No extra query for each category
        print(product.name)
```        
 Efficient: Only 2 queries are made, no matter how many categories or products you have.

## Summary
| Feature         | `prefetch_related()`               |
| --------------- | ---------------------------------- |
| ✅ Good for      | `ManyToMany`, reverse `ForeignKey` |
| ⚙️ How it works | Separate queries, join in Python   |
| 🚀 Benefit      | Reduces number of database hits    |
| 🚫 Avoids       | The N+1 query problem              |










