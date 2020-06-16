from django import forms
from .models import Post

class createPost(forms.ModelForm):
    class Meta:
        model  = Post
        fields = [
            'description',
            'subcategory',
            'subject',
        ]