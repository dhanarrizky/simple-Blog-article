from django.forms.models import BaseModelForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post,category, Profile, comment

from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from .form import PostForm, CommentForm

from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def SearchView(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        cont = Post.objects.filter(title_tag__contains=searched)
        return render(request, 'BlogArticle/search_page.html', {'searched':searched,'cont':cont})
    else:
        return render(request, 'BlogArticle/search_page.html')


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
        
    return HttpResponseRedirect(reverse('detile-post',args=[str(pk)] ))

class HomeView(ListView):
    model = Post
    paginate_by = 6
    template_name = 'BlogArticle/index.html'
    ordering = ['-id']
    
    def get_context_data(self, **kwargs):
        cat_menu = category.objects.all()
        context = super().get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context
    
    
    
class DetilePostView(DetailView):
    model = Post
    template_name = 'BlogArticle/full_post.html'
    
    def get_context_data(self,*args, **kwargs):
        cat_menu = category.objects.all()
        context = super().get_context_data(**kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        total_likes = stuff.total_likes()
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


    
class AddPostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "BlogArticle/add_post.html"
    
    def get_context_data(self, **kwargs):
        cat_menu = category.objects.all()
        context = super().get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context
    

    #fields = '__all__'
class AddCommentsView(CreateView):
    model = comment
    form_class = CommentForm
    template_name = "BlogArticle/comments_page.html"
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = reverse_lazy('homePage')
    
    
class MyPostView(ListView):
    model = Post
    template_name = 'BlogArticle/my_post.html'
    
    def get_context_data(self, **kwargs):
        cat_menu = category.objects.all()
        context = super().get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context
    
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'BlogArticle/add_post.html'
    
    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'BlogArticle/delete_post.html'
    success_url=reverse_lazy('my-post')
    
    
def CategoryView(request, cat):
    cat_menu = category.objects.all()
    cats = Post.objects.filter(category=cat)
    return render(request, 'BlogArticle/category.html', {'cat':cat, 'cats':cats ,'cat_menu':cat_menu})

def CategoryListView(request):
    cat_menu = category.objects.all()
    return render(request, 'BlogArticle/category_list.html', {'cat_menu':cat_menu})
    



class ShowDetileProfileView(DetailView):
    model = Profile
    template_name = 'BlogArticle/detile_profile.html'
    
    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        cat_menu = category.objects.all()
        post_article = Post.objects.all()
        context = super(ShowDetileProfileView, self).get_context_data(*args, **kwargs)
        
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        
        context["post_article"] = post_article
        context["cat_menu"] = cat_menu
        context["page_user"] = page_user
        return context
    
