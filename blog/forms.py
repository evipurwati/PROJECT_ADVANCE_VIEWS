from django import forms
from .models import BlogPost

class PostForm(forms.ModelForm) :
    class Meta :
        model = BlogPost
        fields = '__all__'
