from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Andrii',
        'title': 'blog post 1',
        'content': 'First post content',
        'date_posted': 'December 20, 2021'
    },
    {
        'author': 'Ihor',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    #return HttpResponse('<h1>Blog Home</h1>')
    return render(request,'Blog/home.html',context)


def about(request):
    #return HttpResponse('<h1>Blog about</h1>')
    return render(request,'Blog/about.html')
