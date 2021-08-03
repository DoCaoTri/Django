from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Post

# a = Post()
# a.title = 'First Title'
# a.body = 'Hello World'
# a.save()

# b = Post(title = 'Secondary Post', body = 'Hello Django')
# b.save()

def list_post(request):
    data = {'Posts': Post.objects.all().order_by("-date")}
    return render(request, 'blog/blog.html', data)

def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post.html', {'post': post})