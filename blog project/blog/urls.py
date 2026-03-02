
from django.urls import path
from blog.views import post_list_view
urlpatterns = [
    path('',post_list_view,name="post_list_view"),
]
