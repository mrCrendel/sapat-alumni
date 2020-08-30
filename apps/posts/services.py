from apps.commons.services import BaseService

from .models import PostCategory, Post


class PostCategoryService(BaseService):
    model = PostCategory


class PostService(BaseService):
    model = Post
