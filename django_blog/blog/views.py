from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.db.models import Q
from .models import Post
from .forms import PostForm


class SearchResultsView(ListView):
  model = Post
  template_name = 'blog/search_results.html'
  context_object_name = 'posts'
  paginate_by = 10


  def get_queryset(self):
     q = self.request.GET.get('q', '').strip()
     if not q:
      return Post.objects.none()
     
     return (
            Post.objects.filter(
                Q(title__icontains=q) |
                Q(content__icontains=q) |
                Q(tags__name__icontains=q)
            ).distinct()
)


class TaggedPostListView(ListView):
  model = Post
  template_name = 'blog/posts_by_tag.html'
  context_object_name = 'posts'
  paginate_by = 10


  def get_queryset(self):
     tag_name = self.kwargs.get('tag_name')
     if not tag_name:
      return Post.objects.none()
     return Post.objects.filter(tags__name__iexact=tag_name).distinct()


  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['tag_name'] = self.kwargs.get('tag_name')
    return context
  
class PostCreateView(LoginRequiredMixin, CreateView):
  model = Post
  form_class = PostForm


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
 model = Post
 form_class = PostForm