from django.urls import path
from . import views
urlpatterns = [
    path('',views.get_all_posts, name="get_all_posts"),
    path('add_post',views.add_new_post,name="add_post"),
    path('edit_post/<int:post_id>', views.edit_post,name="edit_post"),
    path('post/<int:post_id>',views.show_post,name="show_post"),
    path('delete/<int:post_id>',views.delete_post,name='delete_post'),
    path('register',views.register,name="register"),
    path('user_login',views.user_login,name="user_login"),
    path('user_logout',views.user_logout,name="user_logout"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact")
]