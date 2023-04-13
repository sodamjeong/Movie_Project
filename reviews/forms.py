from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('like_users', 'user',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)