from datetime import timedelta

from django.contrib import admin
from django.utils import timezone

from .models import Author, Category, Post


class MyAdminSite(admin.AdminSite):

    """
    Our custom admin site

    By overriding this rather than using the default builtin one we get:

    - No users and groups models to edit
    - Custom titles and headers
    """

    index_title = "Blog Browser & Editor"
    site_header = index_title
    site_title = index_title
    site_url = None


admin_site = MyAdminSite(name="myadmin")


@admin.register(Author, site=admin_site)
class AuthorAdmin(admin.ModelAdmin):
    # Controls which fields are displayed
    # https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
    # Note: post_count is a custom field defined in a method below
    list_display = ("name", "status", "post_count")

    # Makes a field editable on the list view screen
    # https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_editable
    list_editable = ("status",)

    def post_count(self, obj):
        """Show a count of blogs by this author"""

        # Note: This is purposefully not optimized
        return obj.post_set.count()


@admin.register(Category, site=admin_site)
class CategoryAdmin(admin.ModelAdmin):
    # Controls which fields are displayed
    list_display = ("name", "post_count")

    def post_count(self, obj):
        """Show a count of blogs in this category"""

        # Note: This is purposefully not optimized
        return obj.post_set.count()


class PostPublishDateFilter(admin.SimpleListFilter):

    """
    Filter posts by when they were published

    This is a custom "filter" that allows filtering a blog by its publishing date.
    This illustrates how to create a custom filter but the Django built-in filter
    for date fields is arguably already better than this one.

    However, you might consider using this for a field that spanned model relationships
    or one that has a complex data type.
    """

    title = "publish date"
    parameter_name = "publish"

    def lookups(self, request, model_admin):
        return [
            ("unpublished", "Unpublished"),
            ("recent", "Recently Published"),
            ("old", "Old"),
        ]

    def queryset(self, request, queryset):
        value = self.value()
        if value == "unpublished":
            return queryset.filter(publish_date=None)
        if value == "recent":
            return queryset.filter(publish_date__gt=timezone.now() - timedelta(days=30))
        if value == "old":
            return queryset.filter(
                publish_date__lt=timezone.now() - timedelta(days=365)
            )

        return queryset


@admin.register(Post, site=admin_site)
class PostAdmin(admin.ModelAdmin):
    # Gives a date-based drilldown filter on this model by this field
    # https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.date_hierarchy
    date_hierarchy = "publish_date"

    # Controls which fields are displayed
    list_display = ("title", "author", "post_categories", "publish_date")

    # Filters that are shown on the right side of the list view
    # https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_filter
    list_filter = (
        # PostPublishDateFilter,
        "author",
        "categories",
    )

    # Fields searchable by the search box
    # https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields
    search_fields = ("title", "body")

    def post_categories(self, obj):
        """Show a combined list of categories for each post"""

        # Note: This is purposefully not optimized
        return ", ".join([c.name for c in obj.categories.all()])
