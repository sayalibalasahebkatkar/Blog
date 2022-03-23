from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from blogapp.models import Blog

# Create your views here.
def bloghome(request):
    allpost=Blog.objects.all()
    context={'allpost':allpost}
    # print(allpost[0].title)
    return render(request,'blog/bloghome.html',context)



def blogpost(request,slug):
    post=Blog.objects.filter(slug=slug).first()
    context={'post':post}
    print('slug')
    return render(request,'blog/blogpost.html',context)


