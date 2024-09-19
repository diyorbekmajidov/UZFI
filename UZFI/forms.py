from django import forms
from .models import Leadership

class LeadershipForm(forms.ModelForm):
    class Meta:
        model = Leadership
        fields = '__all__'
        widgets = {
            'duties': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
            'biography': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
        }


