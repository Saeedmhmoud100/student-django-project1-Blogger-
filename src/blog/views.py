from django.shortcuts import render, get_object_or_404
from .models import post,comment
from .form import NewComment, PostCreateform
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


posts =[
        {
        'title':'التدوينة الاولي',
        'content':'نص التدوينة الاولي كنص تجريبي',
        'post_date':'15-3-2020',
        'author':'Ahmed Mhmoud',
    },
        {
        'title':'التدوينة الثانية',
        'content':'نص التدوينة الثانية كنص تجريبي',
        'post_date':'15-3-2020',
        'author':'Ahmed Mhmoud',
    },
        {
        'title':'التدوينة الثالثة',
        'content':'نص التدوينة الثالثة كنص تجريبي',
        'post_date':'15-3-2020',
        'author':'Ahmed Mhmoud',
    },
        {
        'title':'التدوينة الرابعة',
        'content':'نص التدوينة الرابعة كنص تجريبي',
        'post_date':'15-3-2020',
        'author':'Ahmed Mhmoud',
    }]



def home(request):
    posts = post.objects.all()
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    try:
        posts= paginator.page(page)
    except PageNotAnInteger:
        posts= paginator.page(1)
    except EmptyPage:
        posts= paginator.page(paginator.num_page)
    context ={
        'title':'الصفحة الرئيسية',
        'posts': posts,
        'page':page,
    }
    return render(request, 'blog/index.html',context)

def about(request):
    return render(request, 'blog/about.html', {'title':'من انا'})


def post_detail(request, post_id):

    posts= get_object_or_404(post, pk= post_id)
    comments = posts.comments.filter(active=True) #comment.objects.all().filter(active=True, Post=posts)


    if request.method == "POST":
        comment_form = NewComment(data=request.POST)
        if comment_form.is_valid():
            print('yes')
            new_comment = comment_form.save(commit=False)
            new_comment.Post=posts
            new_comment.save()
            comment_form = NewComment()
            
    else:
        comment_form = NewComment()
        
    context = {
        'title':posts,
        'post':posts,
        'comments':comments,
        'comment_form':comment_form
    }

    return render(request, 'blog/detail.html', context)


class PostCreateViews(LoginRequiredMixin ,CreateView):
    model = post
    #fields = ('title', 'content')
    template_name='blog/new_post.html'
    form_class = PostCreateform
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateViews(UserPassesTestMixin ,LoginRequiredMixin ,UpdateView):
    model = post
    template_name='blog/post_update.html'
    form_class = PostCreateform
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteview(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = post
    success_url= '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False