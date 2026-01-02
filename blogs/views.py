from django.shortcuts import render


# Create your views here.
def start_page(request):
    return render(request, "blogs/index.html")

def post(request):
    return render(request, "blogs/all-posts.html")

def post_detail(request, slug):
    return render(request, "blogs/post-detail.html")