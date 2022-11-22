from django import forms
from comment_khosh_kam.models import Comment

class CommentForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class': ''}))
    text_comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'نظر خود را بنویسید ...'}))
    email_comment = forms.EmailField(widget=forms.EmailInput())

