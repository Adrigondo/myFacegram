from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.urls import reverse_lazy

from datetime import datetime

from posts.forms import PostForm
from posts.models import Post

class PostsFeedView(LoginRequiredMixin, ListView):
    """ Return all published posts. """
    template_name='posts/feed.html'
    model=Post
    ordering=("-created",)
    paginate_by=30
    context_object_name="posts"

class PostDetailView(LoginRequiredMixin, DetailView):
    """ Detail view for a post"""
    template_name='posts/post-detail.html'
    slug_field="id"
    slug_url_kwarg="username"
    pk_url_kwarg="id"
    queryset=Post.objects.all()
    context_object_name="post"

class CreatePostView(LoginRequiredMixin, CreateView):
    template_name="posts/new.html"
    form_class=PostForm
    success_url=reverse_lazy("posts:feed")
    def get_context_data(self, **kwargs):
        """Add user and profile to context"""
        context = super().get_context_data(**kwargs)
        context["current_date"] = datetime.today()
        context["user"] = self.request.user
        context["profile"] = self.request.user.profile
        return context   
