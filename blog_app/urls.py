from django.urls import path

from blog_app import views

urlpatterns =[
    path("",views.PostListView.as_view(), name='post_list'),
    # path("",views.post_list, name='post_list'),
    path("post_detail/<int:pk>/",views.PostDetailView.as_view(), name='post_detail'),
    # path("draft_list/", views.draft_list, name="draft_list"),
     path("draft_list/", views.DraftListView.as_view(), name="draft_list"),
    # path("draft_detail/<int:pk>/",views.draft_detail, name='draft_detail'),
    path("draft_detail/<int:pk>/",views.DraftDetailView.as_view(), name='draft_detail'),
    # path("draft_publish/<int:pk>/",views.draft_publish, name='draft_publish'),
      path("draft_publish/<int:pk>/",views.DraftPublishView.as_view(), name='draft_publish'),
    # path("post_delete/<int:pk>/",views.post_delete, name='post_delete'),
     path("post_delete/<int:pk>/",views.PostDeleteView.as_view(), name='post_delete'),
    path("post_create/",views.PostCreateView.as_view(), name="post_create"),
    path("post_update/<int:pk>/",views.PostUpdateView.as_view(), name='post_update'),

]