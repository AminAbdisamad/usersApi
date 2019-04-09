from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("access/", admin.site.urls, name="admin"),
    path("", include("profilesApi.urls")),
]
