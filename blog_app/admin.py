from django.contrib import admin

from blog_app.models import Users, Product, Order, Post 

admin.site.register([Users, Product, Order, Post]);
