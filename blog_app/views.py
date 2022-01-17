from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from blog_app.models import Post, Product
from blog_app.forms import PostForm

def base(request):
    return render(request, "blog_app/base.html");

def index(request):
    return render(request, "blog_app/index.html");

"""def show_products(request):

    products_list = Product.objects.all();
    context = {"products_list": products_list};

    return render(request, "blog_app/shop.html", context);

def product_detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id);

    except Product.DoesNotExist:
        raise Http404("Ese producto no existe");
    
    return render(request, "blog_app/detail.html", {"product": product});"""

class ShopView(ListView):
    template_name = "blog_app/shop.html";
    context_object_name = "products_list";

    def get_queryset(self):
        return Product.objects.order_by('section').all();

class DetailView(DetailView):
    model = Product
    template_name = 'blog_app/detail.html';

class BlogView(ListView):
    model = Post;
    template_name = "blog_app/blog.html";
    ordering = ["-date"];

class PostDetail(DetailView):
    model = Post;
    template_name = "blog_app/post_detail.html";

class AddPost(CreateView):
    model = Post;
    form_class = PostForm;
    template_name = "blog_app/add_post.html";
    #fields = ("author", "subject", "body");

class EditPost(UpdateView):
    model = Post;
    form_class = PostForm;
    template_name = "blog_app/edit_post.html";

class DeletePost(DeleteView):
    model = Post;
    template_name = "blog_app/delete_post.html";
    success_url = reverse_lazy("blog_app:blog");
    # Para la vista Delete no funciona el método get_absolute_url que tiene el modelo Post.