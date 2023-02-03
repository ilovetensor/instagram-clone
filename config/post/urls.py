from django.urls import path 
from .views import index, new_post, post_detail, post_like
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', index, name="index"),
    path('new-post/', new_post, name="new_post"),
    path('<uuid:post_id>/', post_detail, name="post_detail"),
    path('<uuid:post_id>/like', post_like, name="post_like"),

]

