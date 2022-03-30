from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from blogapp.models import Blog,BlogComment
from django.contrib import messages

# Create your views here.
def bloghome(request):
    allpost=Blog.objects.all()
    context={'allpost':allpost}
    # print(allpost[0].title)
    return render(request,'blog/bloghome.html',context)



def blogpost(request,slug):
    post=Blog.objects.filter(slug=slug).first()
    comment=BlogComment.objects.filter(post=post)
    context={'post':post,'comment':comment}
    print('slug')
    return render(request,'blog/blogpost.html',context)


def postComment(request):
    if request.method=='POST':
        comment=request.POST.get('comment')
        user=request.user
        postsno=request.POST.get('postsno')
        post=Blog.objects.get(sno=postsno)
        comment=BlogComment(comment=comment,user=user,post=post)
        comment.save()
        messages.success(request,'Your comment has been set successfully')
    return redirect(f'/blog/{post.slug}')


