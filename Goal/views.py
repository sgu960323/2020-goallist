from django.shortcuts import render, redirect
from .models import Post
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