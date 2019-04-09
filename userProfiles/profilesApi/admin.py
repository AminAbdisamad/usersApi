from django.contrib import admin
from .models import UserProfile, Feed, Session, Speaker

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Feed)
admin.site.register(Session)
admin.site.register(Speaker)

# CUstomizing admin

admin.site.site_header = "User Profiles API. Dashboard"
admin.site.site_title = "User Profiles API "
