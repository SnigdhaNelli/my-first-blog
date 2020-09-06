from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from .filters import PostFilter
from .models import Chat
from .forms import ChatForm
# from django.views.generic import TemplateView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse
# @csrf_exempt

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})

def login(request):
    return render(request, 'login.html', {'form': form})
    # return render_to_response('login.html', context_instance=RequestContext(request))
    # return HttpResponse("I have opened my view up to cross site request forgery, yippee!")

def search(request):
    search_list = Post.objects.all()
    post_filter = PostFilter(request.GET, queryset=search_list)
    return render(request, 'blog/search_list.html', {'filter': post_filter})

def chat(request):
    if request.method == "CHAT":
        form = ChatForm(request.CHAT)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.name = request.user
            chat.message = timezone.now()
            post.save()
            return redirect('chat', pk=chat.pk)
    else:
        form = ChatForm()
    return render(request, 'chat.html', {'form': form})
