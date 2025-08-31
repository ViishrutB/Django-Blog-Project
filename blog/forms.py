from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(label='Name', max_length=25)
    email = forms.EmailField(label='Email')
    to = forms.EmailField()
    comments = forms.CharField(
        widget=forms.Textarea,
        required=False)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')