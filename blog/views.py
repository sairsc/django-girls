from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect
from django.conf import settings
from django.http import JsonResponse


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        "published_date"
    )
    return render(
        request, "blog/post_list.html", {"posts": posts, "app_name": settings.APP_NAME}
    )


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(
        request, "blog/post_detail.html", {"post": post, "app_name": settings.APP_NAME}
    )


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(
        request, "blog/post_edit.html", {"form": form, "app_name": settings.APP_NAME}
    )


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return JsonResponse({"success": "success", "title": post.title, "text": post.text})
    return JsonResponse({"error": form.errors})


def post_delete(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)
        if post:
            post.delete()
            return JsonResponse({"success": "success"})
    return JsonResponse({"error": "error"})
