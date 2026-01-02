from django.urls import path
from . import views

urlpatterns = [
    path("",views.start_page, name="starting-page"),
    path("post",views.post, name="post-page"),
    path("posts/<slug:slug>",views.post_detail, name="post-details-page"),
]