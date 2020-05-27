from django.shortcuts import render

# Create your views here.

from .models import Post

def post_list(request):
	posts = Post.objects.all()
	context = {
		'post_list': posts
	}
	return render(request, 'posts/post_list.html', context)