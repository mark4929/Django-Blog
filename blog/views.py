from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Subscriber
from .forms import SubscriptionForm

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    else:
        form = SubscriptionForm()
    return render(request, 'blog/subscribe.html', {'form': form})
from django.shortcuts import render, redirect
from .models import Post, Subscriber
from .forms import SubscriptionForm

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    else:
        form = SubscriptionForm()
    return render(request, 'blog/subscribe.html', {'form': form})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})
