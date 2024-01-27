from django.urls import path, include
from . import views

app_name = 'api-v1'

urlpatterns = [
    # FBV
    # path('post/', views.postList, name='post-list'), 
    # path('post/<id>/', views.postDetail, name='post-detail'), 
    
    # APIView
    path('post/', views.PostList.as_view(), name='post-list'), 
    path('post/<int:id>/', views.PostDetail.as_view(), name='post-detail'), 
    
]
