from django.contrib import admin

from .models import User

admin.site.site_header = "Food Admin"
admin.site.site_title = "Food Admin Portal"
admin.site.index_title = "Welcome to Food Admin Portal"


@admin.register(User)
class UserCustomizedAdmin(admin.ModelAdmin):
    list_display=["email"]




