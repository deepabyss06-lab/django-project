from django.shortcuts import render
from blog.models import Post
# Create your views here.
def post_list_view(request):
    post = Post.objects.all()
    return render(request,"blog/post_list.html",{"posts":post})