from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post, Comment
from .forms import CommentForm
# Create your views here.

def index(response):            #function-based view for the landing page
    return render(response, "blog/base.html", {})

def allPosts(request):     #function-based view to display all posts 
    posts = Post.objects.all()
    post_dict ={"posts":posts}
    return render(request, "blog/allPosts.html", post_dict)

def detailedView(request, pk):         #function-based view to display the posts individually
    posts = Post.objects.get(id=pk)
    post_dict ={"posts":posts}
    return render(request, "blog/detailed.html", post_dict)

class BlogCreateView(CreateView):      #class-based view to create a new post 
    model = Post
    template_name = 'blog/newpost.html'
    fields = ['title', 'author', 'body']
    success_url = reverse_lazy('listpost')

class BlogUpdateView(UpdateView):       #class-based view to edit/update a post
    model = Post
    template_name = 'blog/edit.html'
    fields = ['title', 'body']
    # success_url = reverse_lazy('fullPost')

class BlogDeleteView(DeleteView):                #class-based view to delete a post
    model = Post
    template_name = 'blog/deletepost.html'
    success_url = reverse_lazy('listpost')


class AddCommentView(CreateView):   #class-based view to add a comment
    model = Comment
    template_name = 'AccountReg/newcomment.html'
    fields = ['body']
    success_url = reverse_lazy('fullPost')


    # def form_valid(self, form):
    #     form.instance.post_id = self.kwargs['pk']
    #     form.instance.author = request.user
    #     #return super().form_valid(form)


    # success_url = reverse_lazy('fullPost')




    