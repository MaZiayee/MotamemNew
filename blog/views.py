from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,JsonResponse
from blog.models import Post
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import PostSerializer
# Create your views here.

@api_view(["GET","POST"])
def api_post_list(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=1)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    
@api_view(["GET","PUT","DELETE"])
def api_post_detail(request,id):
    post = get_object_or_404(Post, pk=id , status=1)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)  #be jaye if valid
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"detail":"Item removed successfully"},status=status.HTTP_204_NO_CONTENT)