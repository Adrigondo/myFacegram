# Django
from django.contrib import admin

# Models
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""
    list_display = ('id', 'user', 'title', 'content_text', 'photo')
    list_display_links = ('id', 'user')
    search_fields = ('user__username', 'user__email', 'title',)
    list_filter = ('created', 'modified')