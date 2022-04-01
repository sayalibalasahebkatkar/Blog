from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from blogapp.models import Blog,BlogComment
from django.contrib import messages
from blogapp.templatetags import extras

# Create your views here.
def bloghome(request):
    allpost=Blog.objects.all()
    context={'allpost':allpost}
    # print()
    return render(request,'blog/bloghome.html',context)



def blogpost(request,slug):
    post=Blog.objects.filter(slug=slug).first()
    comment=BlogComment.objects.filter(post=post,parent=None)
    replies=BlogComment.objects.filter(post=post).exclude(parent=None)
    
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    print(replyDict)
    context={'post':post,'comment':comment,'user':request.user,'replyDict':replyDict}
    return render(request,'blog/blogpost.html',context)


def postComment(request):
    if request.method=='POST':
        comment=request.POST.get('comment')
        user=request.user
        postsno=request.POST.get('postsno')
        parentSno=request.POST.get('parentSno')
        post=Blog.objects.get(sno=postsno)
        if parentSno=="":
            comment=BlogComment(comment=comment,user=user,post=post)
            comment.save()
            messages.success(request,'Your comment has been set successfully')
        else:
            parent=BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment=comment,user=user,post=post,parent=parent)
            comment.save()
            messages.success(request,'Your reply has been set successfully')
        
    return redirect(f'/blog/{post.slug}')


