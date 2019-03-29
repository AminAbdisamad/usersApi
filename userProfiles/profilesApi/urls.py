from django.urls import path
from . import views


urlpatterns = [
    path("api/", views.Welcome.as_view()),
    path("api/add", views.Add.as_view()),
]
