from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.http import JsonResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

def main(request):
    posts=Post.objects.all
    if request.method=="POST":
        author=request.user
        title=request.POST['title']
        body=request.POST['body']
        year=request.POST['year']
        month=request.POST['month']
        day=request.POST['day']
        reason=request.POST['reason']
        subject=request.POST['subject']
        Post.objects.create(author=author, title=title, body=body, year=year, month=month, day=day, reason=reason, subject=subject)
        return redirect('main')
    elif request.method=="GET":
        return render(request, 'main.html', {'posts':posts})

def post_detail(request):
    if request.method=="GET":
        pk=request.GET['pk']
        post=get_object_or_404(Post, pk=pk)
        context={
            'author':post.author, 
            'title':post.title, 
            'body':post.body, 
            'year':post.year, 
            'month':post.month, 
            'day':post.day, 
            'reason':post.reason
        }
        return JsonResponse(context)