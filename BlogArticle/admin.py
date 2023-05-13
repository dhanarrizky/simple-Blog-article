from django.contrib import admin

from .models import Post, category, Profile, comment

# Register your models here.

admin.site.register(Post)
admin.site.register(category)
admin.site.register(Profile)
admin.site.register(comment)