
from django.contrib import auth
from django.http.response import HttpResponseRedirect
from post.models import Comment, Post
from django.shortcuts import get_object_or_404, redirect, render
from . forms import *
from django.contrib.auth import logout
from django.urls import reverse
# def post_list(request):

    # posts = Post.objects.all
    # form = PostForm(request.POST)
    # if request.method == "POST":
    #     if form.is_valid():
    #         form.save(commit=False)
    #         form.author = request.user
            
    #         form.save()
    #         return redirect("/")
    #     else:
    #         form = PostForm()

    
    # context = {
    #     "posts":posts,
    #     "form":form,
    # }
    # return render(request,'index.html',context)
from django.views import generic
class PostList(generic.ListView):
    model = Post
#Detail and Comments
# def post_detail(request, pk):
#     template_name = 'post_detail.html'
#     post = get_object_or_404(Post, id=pk)
#     comment_form = CommentForm()
#     comments = post.comments
#     new_comment = None
#     comment_form = CommentForm()
#     # Comment posted
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():

#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             new_comment.name = comment_form.cleaned_data.get("name")
#             new_comment.email = comment_form.cleaned_data.get("email")
#             new_comment.body = comment_form.cleaned_data.get("body")



#             # Assign the current post to the comment
#             new_comment.post = post
#             # Save the comment to the database
#             new_comment.save()
#             comment_form = CommentForm()
            
#     else:
#         comment_form = CommentForm()

#     return render(request, template_name, {'post': post,
#                                         'comments': comments,
#                                         'comment_form': comment_form,
#                                         'new_comment': new_comment
                                        
#                                         })

#post Detail class based views

class PostDetail(generic.DeleteView):
    model = Post
    ordering = ['-created_on']

def edit_comment(request,pk):
    comment = Comment.objects.get(id=pk)
    comment_form = CommentForm(instance=comment)
    if request.method =='POST':
        comment_form = CommentForm(request.POST,instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            return redirect('/')
    context = {
        "comment_form":comment_form
    }
    return render(request,'edite_comment.html',context)

def delete_comment(request,pk):
    try:
        comment = Comment.objects.get(id=pk)
        if request.method=="POST":
            comment.delete()
    except Comment.DoesNotExist:
        comment = None
    
        
    context = {
        "comment":comment
    }
    return HttpResponseRedirect(reverse('post_detail',args=[pk]))

def logout(request):
    auth.logout()
    return redirect("/")


