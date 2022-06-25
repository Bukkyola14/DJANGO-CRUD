from django.shortcuts import render

# Create your views here.

class PostListView(ListView):
	model = Post
	fields = "__all__"
	sucess_url = reverse_lazy('blog:all")

class PostDetailView(DetailView):
	model = Post

class PostUpdateView(UpdateView):
	model = Post
	fields = "__all__"
	sucess_url = reverse_lazy('blog:all")

class PostDeleteView(DeleteView):
	model = Post
	fields = "__all__"
	sucess_url = reverse_lazy('blog:all")