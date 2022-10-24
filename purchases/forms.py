
from dataclasses import field
from django.forms import ModelForm
from purchases.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', ]
