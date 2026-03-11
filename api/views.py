from django.shortcuts import render
from rest_framework import generics
from app.models import BlogPost,Comment
from .serializers import PostSerializer,UserSerializer,CommentSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from api.permissons import IsAuthorOrReadOnly
from datetime import date
# Create your views here.


class PostList(generics.ListCreateAPIView):
    queryset = BlogPost.objects.select_related('author').all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user,
                        date=date.today().strftime("%B %d, %Y"))

class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.select_related('author').all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(date=date.today().strftime("%B %d, %Y"))

class CommentList(generics.ListCreateAPIView):

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.request.query_params.get("post")
        qs = Comment.objects.select_related('comment_author', 'parent_post')
        if post_id:
            qs = qs.filter(parent_post=post_id)

        return qs
    def perform_create(self, serializer):
        serializer.save(comment_author=self.request.user)

class CommentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.select_related('comment_author', 'parent_post').all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly]

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly]
