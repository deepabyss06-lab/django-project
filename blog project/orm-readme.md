# Django ORM Quick Notes

## Open Django Shell
```bash
python manage.py shell
```

Import models:
```python
from django.contrib.auth.models import User
from blog.models import Post
```

---

# Creating Objects

## Get a User
```python
user = User.objects.get(username='admin')
```

- Retrieves **one object** from the database.
- Exceptions:
  - `DoesNotExist` → if no result found
  - `MultipleObjectsReturned` → if more than one result found

---

## Create Object (In Memory)

```python
post = Post(
    title='Another post',
    slug='another-post',
    body='Post body.',
    author=user
)
```

- Object exists **only in memory**
- Not yet saved to database

---

## Save Object

```python
post.save()
```

- Executes **SQL INSERT**
- Persists object to database

---

## Create and Save in One Step

```python
Post.objects.create(
    title='One more post',
    slug='one-more-post',
    body='Post body.',
    author=user
)
```

---

## get_or_create()

```python
user, created = User.objects.get_or_create(username='user2')
```

Returns:
- Object
- Boolean `created` (True if new object created)

---

# Updating Objects

```python
post.title = "New title"
post.save()
```

- Executes **SQL UPDATE**
- Changes saved only after calling `save()`

---

# Retrieving Objects

## Get Single Object

```python
Post.objects.get(id=1)
```

## Get All Objects

```python
all_posts = Post.objects.all()
```

- Returns a **QuerySet**
- QuerySets are **lazy** (executed only when needed)

Example forcing execution:

```python
Post.objects.all()
```

---

# Filtering Objects

```python
Post.objects.filter(title="Who was Django Reinhardt?")
```

View SQL query:

```python
posts = Post.objects.filter(title="Who was Django Reinhardt?")
print(posts.query)
```

---

# Field Lookups

Format:

```
field__lookup
```

## Exact

```python
Post.objects.filter(id__exact=1)
Post.objects.filter(id=1)
```

## Case-insensitive

```python
Post.objects.filter(title__iexact="django")
```

## Contains

```python
Post.objects.filter(title__contains="Django")
Post.objects.filter(title__icontains="django")
```

## IN Lookup

```python
Post.objects.filter(id__in=[1,3])
```

---

# Comparison Lookups

Greater than

```python
Post.objects.filter(id__gt=3)
```

Greater than or equal

```python
Post.objects.filter(id__gte=3)
```

Less than

```python
Post.objects.filter(id__lt=3)
```

Less than or equal

```python
Post.objects.filter(id__lte=3)
```

---

# String Lookups

Starts with

```python
Post.objects.filter(title__startswith="Who")
Post.objects.filter(title__istartswith="who")
```

Ends with

```python
Post.objects.filter(title__endswith="?")
Post.objects.filter(title__iendswith="reinhardt?")
```

---

# Date Lookups

```python
from datetime import date
```

Exact date

```python
Post.objects.filter(publish__date=date(2024,1,31))
```

Year

```python
Post.objects.filter(publish__year=2024)
```

Month

```python
Post.objects.filter(publish__month=1)
```

Day

```python
Post.objects.filter(publish__day=1)
```

Greater than date

```python
Post.objects.filter(publish__date__gt=date(2024,1,1))
```

---

# Filtering Related Fields

```python
Post.objects.filter(author__username="admin")
```

Chained lookup

```python
Post.objects.filter(author__username__startswith="ad")
```

Multiple filters

```python
Post.objects.filter(
    publish__year=2024,
    author__username="admin"
)
```

---

# Chaining Filters

```python
Post.objects.filter(publish__year=2024) \
            .filter(author__username="admin")
```

---

# Excluding Objects

```python
Post.objects.filter(publish__year=2024) \
            .exclude(title__startswith="Why")
```

---

# Ordering Objects

Ascending

```python
Post.objects.order_by("title")
```

Descending

```python
Post.objects.order_by("-title")
```

Multiple fields

```python
Post.objects.order_by("author", "title")
```

Random order

```python
Post.objects.order_by("?")
```

---

# Limiting QuerySets

First 5 results

```python
Post.objects.all()[:5]
```

Range

```python
Post.objects.all()[3:6]
```

Single object

```python
Post.objects.order_by("?")[0]
```

---

# Counting Objects

```python
Post.objects.filter(id__lt=3).count()
```

Equivalent SQL:

```
SELECT COUNT(*)
```

---

# Checking If Object Exists

```python
Post.objects.filter(title__startswith="Why").exists()
```

Returns:
- `True`
- `False`

---

# Deleting Objects

```python
post = Post.objects.get(id=1)
post.delete()
```

- Deletes object from database
- Related objects removed if `on_delete=CASCADE`

---

# Complex Queries with Q Objects

```python
from django.db.models import Q
```

Example OR query:

```python
starts_who = Q(title__istartswith="who")
starts_why = Q(title__istartswith="why")

Post.objects.filter(starts_who | starts_why)
```

Operators:

| Operator | Meaning |
|--------|--------|
| `&` | AND |
| `|` | OR |
| `^` | XOR |