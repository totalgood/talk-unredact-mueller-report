"""
These models make up a blogging application

- Blog posts have exactly one author
- Blog posts can have zero or more "categories"
"""

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Categories"


class Author(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(
        choices=(("staff", "Staff"), ("guest", "Guest")),
        max_length=255,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    body = models.TextField()
    publish_date = models.DateTimeField(db_index=True, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-publish_date",)
