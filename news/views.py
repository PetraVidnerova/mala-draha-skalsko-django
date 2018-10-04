import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.forms import formset_factory

from .models import Post, Image
from .forms import PostForm, ImageForm

# Create your views here.
def aktuality(request):
    if request.user.is_authenticated:
        posts = Post.objects.all().order_by('-published_date')
    else:
        posts = Post.objects.filter(publish=True).order_by('-published_date')
    return render(request, 'news/aktuality.html', {"posts": posts})

"""
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
    return render(request, 'news/new.html', {"form": form})
"""

@login_required
def post_edit(request, pk):

    ImageFormSet = formset_factory(ImageForm, extra=3)
    
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        formset = ImageFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            for form in formset.cleaned_data:
                if 'image' in form:
                    image = form['image']
                    photo = Image(post=post, image=image)
                    photo.save()

            return redirect('post_detail', pk=post.pk)
        
    else:
        form = PostForm(instance=post)
        formset = ImageFormSet()
        
    return render(request, 'news/new.html', {"form": form, "formset": formset})
    

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date_published = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'news/new.html', {"form": form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.post = post
            image.save()
            return redirect('post_detail', pk=post.pk)
        else:
            return redirect('index')
    form = ImageForm()
    return render(request, 'news/detail.html', {"post": post, "form": form})

def delete_image(request, pk):
    image = get_object_or_404(Image, pk=pk)
    post_pk = image.post.pk
    filename = image.image.path
    image.delete()
    if os.path.isfile(filename):
        os.remove(filename)
    return redirect('post_detail', pk=post_pk)
