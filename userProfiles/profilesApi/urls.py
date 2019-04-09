from django.urls import path, include

# from rest_framework.routers import DefaultRouter
from . import views

# # # Registering viewsert router
# router = DefaultRouter()
# router.register("profile", views.UserProfileViewSet, base_name="profiles")
# # router.register(r"profile", views.UserProfileViewSet, base_name="profiles")

urlpatterns = [
    path("api/users", views.UserProfileView.as_view()),
    path("api/user/<int:pk>/", views.UserProfileDetial.as_view()),
    path("api/feed", views.FeedView.as_view()),
    path("api/speaker", views.SpeakerView.as_view()),
    path("api/session", views.Session.as_view()),
    path("api/session/<int:_id>/", views.SessionDetail.as_view()),
]

