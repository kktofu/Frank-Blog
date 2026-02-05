from django import forms
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.Form):
    title = forms.CharField(label='Blog Post Title', required=True)
    subtitle = forms.CharField(label="Subtitle", required=True)
    name = forms.CharField(label="Your Name", required=True)
    url = forms.URLField(label="Blog Image URL", required=True)
    body = forms.CharField(label="Blog Content", widget = CKEditorWidget(),required=True)

class RegisterForm(forms.Form):
    email = forms.CharField(label="Email", required=True)
    password = forms.CharField(label="Password",widget=forms.PasswordInput,required=True)
    name = forms.CharField(label="Name",required=True)

class LoginForm(forms.Form):
    name = forms.CharField(label="Name", required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput,required=True)

class CommentForm(forms.Form):
    comment_text = forms.CharField(label="Comment",widget=CKEditorWidget(config_name='comment_config'),required=True)