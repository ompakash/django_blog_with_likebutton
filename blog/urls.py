from django.urls import path
# from django.views import PostList,PostDetail,likeView
# from . import views
from blog.views import PostList
from blog.views import PostDetail
from blog.views import likeView


app_name = 'blog'

urlpatterns = [
    path('',PostList.as_view(),name = 'post-list'),
    path('detail/<int:pk>/',PostDetail.as_view(),name= 'post-detail'),
    path('ajax/likes/',likeView,name = 'like')

]