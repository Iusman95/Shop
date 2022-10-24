from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from purchases.models import Posts, Comment
from purchases.forms import CommentForm


class PostListView(ListView):
    model = Posts
    template_name = 'posts/index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs): # Для отоброжения всех постов, начиная с последнего 
        posts = Posts.objects.all()
        context = super(PostListView, self).get_context_data(**kwargs)
        end_post = posts[::-1]
        context['end_post'] = end_post
        return context
    

class PostDetailView(DetailView): # Подробная информация о посте 
    model = Posts 
    template_name = 'posts/detail.html'
    context_object_name = 'post'


class PostCommentView(CreateView):
    model = Comment
    template_name = 'posts/detail.html'
    context_object_name = 'comments'  
    forms = CommentForm
    