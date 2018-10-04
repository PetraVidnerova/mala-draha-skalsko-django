from django import forms

from .models import Post, Image

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'publish']
        labels = {
            'title': ('Titulek'),
            'text': ('Text'),
            'publish': ('Publikovat?'),
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        labels = { 'image': 'Přidat fotku:'}
