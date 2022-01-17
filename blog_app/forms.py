from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post;
        fields = ("author", "subject", "body");

        widgets = {
            "author": forms.Select(attrs={"class": "form-control"}),
            "subject": forms.TextInput(attrs={"class": "form-control", "placeholder": "Máximo 200 caracteres"}),
            "body": forms.Textarea(attrs={"class": "form-control"})
        };