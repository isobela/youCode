from django.contrib import admin
from .models import Prize , People, Event, UserProfile, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

admin.site.register(Prize)

admin.site.register(Event)

admin.site.register(People)
admin.site.register(UserProfile)

admin.site.unregister(User) # Necessary

class UserProfileInline(admin.TabularInline):
    model = UserProfile

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
