from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from .models import Post
from django.views.generic import ListView

# Create your views here.
def post_list(request):
    posts = Post.published.all()
    # Pagination with 3 Posts per Page
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        # If page number is out of range, get the last page of the results
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        # If page number is not an integer, get the first page
        posts = paginator.page(1)
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post, publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )

class PostListView(ListView):

    """
    Alternative post list view
    """

    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'