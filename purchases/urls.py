from django.urls import path
from purchases.views import PostDetailView, PostListView, PostCommentView

urlpatterns = [
  path('posts/', PostListView.as_view(), name='index'),
  path('detail/<int:pk>', PostDetailView.as_view(), name='detail'), 
  path('<int:pk>', PostCommentView.as_view()), 

  ]