from django import forms

class CommentForm(forms.Form):
    text = forms.CharField(label="Expression", max_length=30)