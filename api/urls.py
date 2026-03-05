from django.urls import path
from .views import PostList,PostDetails,CommentList,CommentDetails,UserList,UserDetails

urlpatterns = [
    path('post/',PostList.as_view()),
    path('post/<int:pk>/',PostDetails.as_view()),
    path('comment/',CommentList.as_view()),
    path('comment/<int:pk>/',CommentDetails.as_view()),
    path('users/',UserList.as_view()),
    path('users/<int:pk>/',UserDetails.as_view())
]