from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from . import views

app_name = "blog"

urlpatterns = [
    # WebPage CBV
    path('', views.IndexView.as_view(), name='index'),
    path("post/", views.PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path('post/create/', views.PostCreateView.as_view(), name='post-create'),
    path(
        "post/<int:pk>/delete/",
        views.PostDeleteView.as_view(),
        name="post-delete",
    ),
    path(
        "post/<int:pk>/edit/", views.PostEditView.as_view(), name="post-edit"
    ),
    
    # API
    path("post/api/", views.PostListApiView.as_view(), name="post-list-api"),
    
    path("api/v1/", include("blog.api.v1.urls")),
]
