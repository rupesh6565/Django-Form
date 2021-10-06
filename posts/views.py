from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.

def index(request):
    #if the method is post
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        #if the form is validif
        if form.is_valid():
            #yes, save 
            form.save()

            #redirect to home
            return HttpResponseRedirect('/')
        else:    
            #no, show error
            return HttpResponseRedirect(form.errors.as_json())



    # Get all posts , limit=20
    posts = Post.objects.all()[:20]

    # show 
    return render(request, 'posts.html',
    {'posts': posts}) 


def delete(request, post_id):
    #Find post
    post = Post.objects.get(id = post_id)
    post.delete()
    return redirect('/')