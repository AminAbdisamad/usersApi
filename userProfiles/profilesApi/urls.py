from django.urls import path, include

# from rest_framework.routers import DefaultRouter
from . import views

# # # Registering viewsert router
# router = DefaultRouter()
# router.register("profile", views.UserProfileViewSet, base_name="profiles")
# # router.register(r"profile", views.UserProfileViewSet, base_name="profiles")

urlpatterns = [
    # path("", include(router.urls)),
    # path("api/", views.Welcome.as_view()),
    path("api/", views.UserProfileView.as_view()),
    path("api/feed", views.FeedView.as_view()),
    path("api/speaker", views.SpeakerView.as_view()),
]

