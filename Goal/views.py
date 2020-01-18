from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.core import serializers
import json
from django.http import JsonResponse, HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

def main(request):
    posts=Post.objects.all
    if request.method=="POST":
        author=request.user
        writer=request.user
        title=request.POST['title']
        body=request.POST['body']
        year=request.POST['year']
        month=request.POST['month']
        day=request.POST['day']
        reason=request.POST['reason']
        subject=request.POST['subject']
        Post.objects.create(author=author, writer=writer, title=title, body=body, year=year, month=month, day=day, reason=reason, subject=subject)
        return redirect('main')
    elif request.method=="GET":
        return render(request, 'main.html', {'posts':posts})

def post_detail(request):
    if request.method=="GET":
        pk=request.GET['pk']
        post=get_object_or_404(Post, pk=pk)
        flag=0
        a=request.user
        b=post.writer
        a=str(a)
        if a==b:
            flag=1
        context={'author':post.writer,'title':post.title, 'body':post.body, 'year':post.year, 'month':post.month, 'day':post.day, 'reason':post.reason, 'flag':flag}
        return JsonResponse(context)
        #return HttpResponse(json.dumps(context), content_type="application/json")

def mypage(request):
    posts=Post.objects.filter(writer=request.user)
    if request.method=="POST":
        author=request.user
        writer=request.user
        title=request.POST['title']
        body=request.POST['body']
        year=request.POST['year']
        month=request.POST['month']
        day=request.POST['day']
        reason=request.POST['reason']
        subject=request.POST['subject']
        Post.objects.create(author=author, writer=writer, title=title, body=body, year=year, month=month, day=day, reason=reason, subject=subject)
        return redirect('mypage')
    else:
        return render(request, 'mypage.html', {'posts':posts})
def mydetail(request):
    if request.method=="GET":
        pk=request.GET['pk']
        post=get_object_or_404(Post, pk=pk)
        context={'author':post.writer,'title':post.title, 'body':post.body, 'year':post.year, 'month':post.month, 'day':post.day, 'reason':post.reason}
        return JsonResponse(context)

def mydelete(request):
    if request.method=="GET":
        pk=request.GET['pk']
        post=get_object_or_404(Post, pk=pk)
        post.delete();
        return HttpResponse()

def myedit(request):
    if request.method=="POST":
        pk=request.POST['pk']
        post=get_object_or_404(Post, pk=pk)
        post.title=request.POST['title']
        post.body=request.POST['body']
        post.year=request.POST['year']
        post.month=request.POST['month']
        post.day=request.POST['day']
        post.reason=request.POST['reason']
        post.save()
        return HttpResponse()