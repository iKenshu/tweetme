from django import forms

from .models import Tweet


class TweetModelForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'placeholder': "Your message",
                'class': "form-control",
                'rows': 5,
                'cols': 100,
            })
    )

    class Meta:
        model = Tweet
        fields = [
            "content",
        ]
