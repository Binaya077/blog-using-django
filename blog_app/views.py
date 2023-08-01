from typing import Any
from django.shortcuts import render
from blog_app.models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView,View,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
#function based views
#80-90% are CRUD
#next one is class based views
#10-20% are CRUD

class PostListView(ListView): #This is CLASS BASED
    model=Post
    template_name="post_list.html"
    context_object_name="posts"

    def get_queryset(self):
        queryset=Post.objects.filter(published_at__isnull=False).order_by("published_at")
        return queryset
# def post_list(request): THIS IS FUNCTION BASED
#     posts=Post.objects.filter(published_at__isnull=False).order_by("-published_at")
#     return render(
#         request,
#         "post_list.html",
#         {"posts":posts},
#     )


class PostDetailView(DetailView):
    model=Post
    template_name="post_detail.html"
    context_object_name="post"

    def get_queryset(self):
      queryset=Post.objects.filter(pk=self.kwargs["pk"], published_at__isnull=False)
      return queryset


# def post_detail(request, pk):
#     post=Post.objects.get(pk=pk, published_at__isnull=False)
#     return render(
#         request,
#         "post_detail.html",
#         {"post":post},
#     )


class DraftListView(LoginRequiredMixin, ListView):
    model=Post
    template_name="draft_list.html"
    context_object_name="posts"

    def get_queryset(self):
        QuerySet=Post.objects.filter(published_at__isnull=True).order_by("published_at")
        return QuerySet

# @login_required
# def draft_list(request):
#     posts=Post.objects.filter(published_at__isnull=True).order_by("-published_at")
#     return render(
#         request,
#         "draft_list.html",
#         {"posts":posts},
#     )
class DraftDetailView(LoginRequiredMixin, DetailView):
    model=Post
    template_name="draft_detail.html"
    context_object_name="post"

    def get_queryset(self):
        queryset=Post.objects.filter(pk=self.kwargs["pk"], published_at__isnull=True)
        return queryset


# @login_required
# def draft_detail(request, pk):
#     post=Post.objects.get(pk=pk, published_at__isnull=True)
#     return render(
#         request,
#         "draft_detail.html",
#         {"post":post},
#     )
from django.utils import timezone
from django.shortcuts import redirect

class  DraftPublishView(LoginRequiredMixin, View):
    def get(self, request, pk):
        post=Post.objects.get(pk=pk, published_at__isnull=True)
        post.published_at=timezone.now()
        post.save()
        return redirect("post_list")


# @login_required
# def draft_publish(request, pk):
#     post=Post.objects.get(pk=pk, published_at__isnull=True)
#     post.published_at=timezone.now()
#     post.save()
#     return redirect("post_list")


class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        post=Post.objects.get(pk=pk)
        post.delete()
        return redirect("post_list")

# @login_required
# def post_delete(request, pk):
#     post=Post.objects.get(pk=pk)
#     post.delete()
#     return redirect("post_list")

from blog_app.forms import PostForm

class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    template_name="post_create.html"
    form_class=PostForm
    success_url=reverse_lazy("post_list")
    
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

# @login_required
# def post_create(request):
#     if request.method=="POST":
#       form=PostForm(request.POST)
#       if form.is_valid():
#           post=form.save(commit=False)
#           post.author=request.user
#           post.save()
#           return redirect("draft_list")
      

#       else:
#         form=PostForm()
#         return render(
#             request,
#             "post_create.html",
#             {"form":form},
#         )
#     else:
#         form=PostForm()
#         return render(
#             request,
#             "post_create.html",
#             {"form":form},
#         )
          

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model=Post
    template_name="post_create.html"
    form_class=PostForm
    success_url=reverse_lazy("post_list")

    def get_success_url(self):
        post=self.get_object()
        if post.published_at:
            return reverse_lazy("post_detail", kwargs={"pk":post.pk})
        else:
            return reverse_lazy("draft_detail",kwargs={"pk":post.pk})


# @login_required
# def post_update(request, pk):
#     post=Post.objects.get(pk=pk)
#     form=PostForm(instance=post)
#     if request.method=="POST":
#         form=PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post=form.save()
#             if post.published_at:
#                 return redirect("post_detail",post.pk)
#             else:
#                 return redirect("draft_detail",post.pk)
            
#         else:

#             return render(
#                 request,
#                 "post_create.html",
#                 {"form":form},
#             )
        
#     else:
#         return render(
#             request,
#             "post_create.html",
#             {"form":form},
#         )
