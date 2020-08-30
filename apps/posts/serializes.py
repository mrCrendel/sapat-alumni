from rest_framework import serializers

from apps.posts.models import PostCategory, Post


class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        exclude = []


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = []
