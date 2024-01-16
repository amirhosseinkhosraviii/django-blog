from django.shortcuts import render, redirect
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import get_object_or_404
from blog.models import Post


def blog_view(request, ):
    posts = Post.objects.filter(status='pub')

    context = {'posts': posts}
    return render(request, 'blog/blog-post.html', context)


def post_list(request):
    posts = Post.objects.filter(status='pub')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def test_view(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/test.html', context)
