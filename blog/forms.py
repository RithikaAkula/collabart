from django import forms
from .models import BlogComment

APPLICATION_TYPES= [
    ('donate', 'Donation'),
    ('buy', 'Buy a product'),
    ]

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['content']


class SupportForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    email = forms.EmailField(required=False, label='Email Address')
    application_type = forms.CharField(label='Application type', widget=forms.Select(choices=APPLICATION_TYPES))
    message = forms.CharField(widget=forms.Textarea)