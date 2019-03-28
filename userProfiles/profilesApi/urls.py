from django.urls import path
from . import views


urlpatterns = [
    path("api/", views.Welcome.as_view()),
    path("api/list", views.ListAll.as_view()),
]

