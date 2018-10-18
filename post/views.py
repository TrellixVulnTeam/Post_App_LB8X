from django.shortcuts import render
from django.http import HttpResponse
from .models import post
# Create your views here.
def index(request):
    #return HttpResponse('hello world')
    posts = post.objects.all()[:10]

    context = {
        'title':'recent nodes',
        'posts' : posts
    }
    return render(request,'post/index.html', context)