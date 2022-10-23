from django.urls import path
from purchases.views import PostDetailView, PostListView

urlpatterns = [
  path('posts/', PostListView.as_view(), name='index'),
  path('detail/<int:pk>', PostDetailView.as_view(), name='detail'), 
  
]