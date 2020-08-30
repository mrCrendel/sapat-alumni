from django.contrib import admin

from apps.posts.models import PostCategory, Post


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
