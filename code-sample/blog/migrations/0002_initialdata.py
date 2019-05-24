"""
Fills the database with sample blog/author/category data
"""

import random
import string
from datetime import timedelta

from django.db import migrations
from django.utils.text import slugify
from django.utils import timezone


CATEGORIES = (
    "Astronomy",
    "Charms",
    "Dark Arts",
    "Herbology",
    "History of Magic",
    "Potions",
    "Transfiguration",
    "Magical Creatures",
    "Divination",
    "Arithmancy",
    "Muggle Studies",
    "Alchemy",
    "Apparition",
)

AUTHORS = (
    "Harry Potter",
    "Ron Weasley",
    "Hermione Granger",
    "Lord Voldemort",
    "Albus Dumbledore",
    "Severus Snape",
    "Rubeus Hagrid",
    "Draco Malfoy",
    "Ginny Weasley",
    "Remus Lupin",
    "Minerva McGonagall",
    "Alastor Moody",
    "Poppy Pomfrey",
    "Quirinus Quirrell",
    "Horace Slughorn",
    "Pomona Sprout",
    "Sybill Trelawney",
    "Dolores Umbridge",
    "Barty Crouch",
    "Bellatrix Lestrange",
    "Lucius Malfoy",
    "Sirius Black",
    "Viktor Krum",
    "Peter Pettigrew",
)

POST_TITLE_BEGINNINGS = CATEGORIES + (
    "Death Eaters",
    "Quidditch",
    "Unbreakable Vows",
    "Curses",
    "Chamber of Secrets",
    "Azkaban",
    "Magical Law",
    "Deathly Hollows",
    "Tri-Wizard Tournament",
    "Dragons",
    "Hogwarts",
    "Unforgivable Curses",
    "House Elves",
)
POST_TITLE_ENDINGS = (
    "How to Protect Yourself",
    "How I Learned to Love Them",
    "Why You Should Learn Them",
    "Things You Need to Know",
    "What Can You Do",
    "Where Should You Go",
    "A History",
    "Deep Background",
    "Journalism",
    "The Crucio Curse",
    "Godric Gryffindor's Sword",
    "Basilisks",
    "Horcruxes",
    "Goblet of Fire",
    "Strategies",
    "Mysteries",
)


def forwards(apps, schema_editor):
    Category = apps.get_model("blog", "Category")
    Author = apps.get_model("blog", "Author")
    Post = apps.get_model("blog", "Post")

    if any((Post.objects.exists(), Category.objects.exists(), Author.objects.exists())):
        # If the user somehow created a bunch of data already, do nothing
        return

    # Add a number of categories
    categories = []
    for name in CATEGORIES:
        categories.append(Category(name=name))
    Category.objects.bulk_create(categories)
    categories = Category.objects.all()

    # Add a number of authors
    authors = []
    for name in AUTHORS:
        authors.append(Author(name=name, status=random.choice(["guest", "staff"])))
    Author.objects.bulk_create(authors)
    authors = list(Author.objects.all())

    # Add a number of posts
    posts = []
    for prefix in POST_TITLE_BEGINNINGS:
        for suffix in POST_TITLE_ENDINGS:
            title = f"{prefix} and {suffix}"
            body = "".join(
                [
                    random.choice(string.printable)
                    for i in range(random.randint(200, 500))
                ]
            )

            # Randomly give posts a publish date and make some posts unpublished
            publish_date = timezone.now() - timedelta(
                days=random.randint(1, 1000), seconds=random.randint(0, 60 * 60 * 24)
            )
            if random.randint(1, 25) == 1:
                publish_date = None

            posts.append(
                Post(
                    title=title,
                    slug=slugify(title),
                    author=random.choice(authors),
                    body=body,
                    publish_date=publish_date,
                )
            )
    Post.objects.bulk_create(posts)

    # Connect posts with categories
    for post in Post.objects.all():
        post_categories = [random.choice(categories)]
        while random.randint(1, 5) > 2:
            post_categories.append(random.choice(categories))
        post.categories.set(post_categories)


class Migration(migrations.Migration):

    dependencies = [("blog", "0001_initial")]

    operations = [
        migrations.RunPython(forwards, reverse_code=migrations.RunPython.noop)
    ]
