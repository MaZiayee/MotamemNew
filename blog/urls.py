from django.urls import path
from blog.views import *

urlpatterns = [
    path('posts/', api_post_list, name='api_post_list'),
    path('post/<int:id>', api_post_detail, name='api_post_detail')
]