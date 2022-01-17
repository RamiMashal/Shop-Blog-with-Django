from django.urls import path

from . import views

app_name = 'blog_app'
urlpatterns = [
    path('base/', views.base, name='base'),
    path('index/', views.index, name='index'),

    #path('shop/', views.show_products, name='shop'),
    path('shop/', views.ShopView.as_view(), name='shop'),

    #path('shop/<int:product_id>/', views.product_detail, name='detail'),
    path('shop/<int:pk>/', views.DetailView.as_view(), name='detail'),

    path('blog/', views.BlogView.as_view(), name='blog'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),

    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('edit_post/<int:pk>/', views.EditPost.as_view(), name='edit_post'),
    path('delete_post/<int:pk>/', views.DeletePost.as_view(), name='delete_post'),
]