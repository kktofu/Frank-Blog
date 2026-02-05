from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()
class BlogPost(models.Model):
    title = models.CharField(max_length=50, unique=True, null=False)
    subtitle = models.CharField(max_length=250, null=False)
    date = models.CharField(max_length=250, null=False)
    body = RichTextField(null=False)
    author = models.CharField(max_length=250, null=False)
    img_url = models.CharField(max_length=250, null=False)
    objects = models.Manager()

class Comment(models.Model):
    text = RichTextField(null=False)
    comment_author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="comment_author")
    parent_post = models.ForeignKey(BlogPost,on_delete=models.CASCADE,related_name="parent_post")