from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(label='Name', max_length=25)
    email = forms.EmailField(label='Email')
    to = forms.EmailField()
    comments = forms.CharField(
        widget=forms.Textarea,
        required=False)