from django.shortcuts import render

# Create your views here.

def post_list(request):
	context = {}
	return render(request, 'posts/list_posts.html', context)