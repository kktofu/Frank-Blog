from rest_framework import serializers
from app.models import BlogPost,Comment
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = BlogPost
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    comment_author = serializers.ReadOnlyField(source='comment_author.username')
    class Meta:
        model = Comment
        fields = ['id', 'text', 'comment_author','parent_post']


class UserSerializer(serializers.ModelSerializer):
    post_author = serializers.PrimaryKeyRelatedField(many=True, queryset=BlogPost.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'post_author']