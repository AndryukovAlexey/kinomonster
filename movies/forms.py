from django import forms
from .models import Comments

class Comment(forms.ModelForm):
    text = forms.TextInput()
    class Meta:
        model = Comments
        fields = ('text',)


