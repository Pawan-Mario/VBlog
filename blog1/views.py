from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render, get_list_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from app.models import Post
from app.form import CommentForm, EditForm, PostForm
from django.http import HttpResponseRedirect

def LikeView(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article_details', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-created_at']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stuff = self.object
        total_likes = stuff.likes.count()
        liked = stuff.likes.filter(id=self.request.user.id).exists()
        comments = stuff.comments.all()
        comment_form = CommentForm()
        
        context.update({
            "total_likes": total_likes,
            "liked": liked,
            "comments": comments,
            "comment_form": comment_form,
        })
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = self.object
            new_comment.user = request.user
            new_comment.save()
            return redirect('article_details', pk=self.object.pk)
        return self.render_to_response(self.get_context_data(comment_form=comment_form))


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class DraftPostView(ListView):
    model = Post
    template_name = 'Draft.html'
    ordering = ['-created_at']