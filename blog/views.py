from django.shortcuts import render
from .models import Blog

# Create your views here.


def allblogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/allblogs.html', {'blogs':blogs})
