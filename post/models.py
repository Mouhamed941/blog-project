from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class Post(models.Model):
    title = models.CharField(max_length=50,blank=True, null=True)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(User,on_delete=CASCADE,related_name="blog_posts",blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField( auto_now_add=True)
    status = models.IntegerField(choices=STATUS,default=0)
    body = models.TextField()

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post,on_delete=CASCADE,related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True,null=True)
    class Meta:
        ordering = ['created_on']
    def __str__(self):
        return 'Comment {} by {}'.format(self.body,self.name)

    

