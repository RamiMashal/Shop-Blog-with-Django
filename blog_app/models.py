from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, DecimalField, EmailField, IntegerField
from django.urls import reverse

class Users(models.Model):
    name = models.CharField(max_length=20);
    surname = models.CharField(max_length=20);
    email = models.EmailField(blank=False, null=False);
    address = models.CharField(max_length=100);
    city = models.CharField(max_length=20);
    post_code = models.CharField(max_length=5);
    country = models.CharField(max_length=30);

    def __str__(self):
        return f"{self.name} {self.surname}";

class Product(models.Model):
    name = models.CharField(max_length=50);
    price = models.DecimalField(max_digits=8, decimal_places=2);
    section = models.CharField(max_length=30);

    def __str__(self):
        return f"{self.section} | {self.name}";

class Order(models.Model):
    # En vez de usar nuestro modelo Users, heredamos de auth.models User
    client = models.ForeignKey(Users, on_delete=models.PROTECT);
    product = models.ForeignKey(Product, on_delete=models.PROTECT);
    date = models.DateTimeField(auto_now_add=True);

    def __str__(self):
        return f"{self.client.name} | {self.client.surname} | {self.date}";

class Post(models.Model):
    subject = models.TextField(max_length=200);
    # En vez de usar nuestro modelo Users, heredamos de auth.models User
    author = models.ForeignKey(User, on_delete=models.PROTECT);
    body = models.TextField();
    date = models.DateTimeField(auto_now_add=True);
    
    def __str__(self):
        return f"Autor: {str(self.author)} | Asunto: {self.subject}";

    def get_absolute_url(self):
        return reverse("blog_app:post_detail", args=(self.id,));
        # args= toma el id (pk) del objeto creado, y redirige a la url post_detail, la cual pide dicho parámetro
        # path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
        # args=(self.id,)) --> Acuérdate de esto porque pasaron horas hasta que te diste cuenta. Típica coma para que entienda que es un iterable.

