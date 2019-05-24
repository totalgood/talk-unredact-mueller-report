from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from blog import urls as blog_urls


urlpatterns = [path("", include(blog_urls))]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
