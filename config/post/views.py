from django.shortcuts import render, redirect, get_object_or_404

from .forms import NewPostForm

from .models import Tag, Post, Follow, Stream
# Create your views here.
def index(request):
    user = request.user
    posts=[]
    object_list = Stream.objects.all().filter(user=user)
    for object in object_list:
        posts.append(object.post)
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

def new_post(request):
    user = request.user
    tags_objects = []

    if request.method == "POST":
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get('image')
            caption = form.cleaned_data.get('caption')
            tag_form = form.cleaned_data.get('tag')
            tags_list = list(tag_form.split(','))

            for tag in tags_list:
                t, created = Tag.objects.get_or_create(title=tag)
                tags_objects.append(t)

            p, created = Post.objects.get_or_create(image=image, caption=caption, user_id=user.id)
            p.tags.set(tags_objects)
            p.save()
            print("=p is saved=")
            return redirect('index')

    else:
        form = NewPostForm()

    context = {
        'form': form,
    }

    return render(request, 'newpost.html', context)

def post_detail(request, post_id):
    
    post = get_object_or_404(Post, id=post_id)
    context = {
        'post': post,
    }
    return render(request, 'postdetail.html', context)

def post_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user 
    if user in post.likes.all():
        post.likes.remove(user)
    else :
        post.likes.add(user)
    return redirect('index')