from django.contrib import admin
from .models import Post, Subscriber

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)
admin.site.register(Subscriber)
