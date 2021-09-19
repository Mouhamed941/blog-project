from django import forms
from django.db.models import fields
from django import forms
from . models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title','body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Your name', max_length=100)        

# class ContactForm(forms.Form):
#     subject = forms.CharField(max_length=100)
#     message = forms.CharField(widget=forms.Textarea)
#     sender = forms.EmailField()
#     cc_myself = forms.BooleanField(required=False)    