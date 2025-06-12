from django import forms
from .models import News_Comment

class NewsCommentForm(forms.ModelForm):
    class Meta:
        model = News_Comment
        fields = ['name', 'email', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ismingiz'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email manzilingiz'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Izohingiz'}),
        }
