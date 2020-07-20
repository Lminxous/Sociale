from .models import Post,Comment
from django import forms
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content']

        def __str__(self):
            return self.title

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

        def __str__(self):
            return self.comment
