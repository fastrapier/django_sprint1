from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def post_detail(request, post_id):
    return render(request, 'pages/post_detail.html')

def category_posts(request, category_slug):
    return render(request, 'pages/category_posts.html')