from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import views as AuthViews
from .models import Profile



class Registr(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(Registr, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs\
            .update({
                'placeholder': 'Придумайте себе имя',
                'class': 'form-control form-inp input-lg'
            })
        self.fields['email'].widget.attrs\
            .update({
                'placeholder': 'Ваш email',
                'class': 'form-control form-inp input-lg'
            })
        self.fields['password1'].widget.attrs\
            .update({
                'placeholder': 'Придумайте пароль',
                'class': 'form-control form-inp input-lg'
            })
        self.fields['password2'].widget.attrs\
            .update({
                'placeholder': 'Повторите пароль',
                'class': 'form-control input-lg'
            })





class Confirm(forms.Form):
    cnf = forms.IntegerField(label='Введите код', widget=forms.TextInput(attrs={'class': 'form-control input-lg'}))
    
    class Meta:
        fields = ['cnf']


class SupportForm(forms.Form):
    theme = forms.CharField(max_length=70)
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        fields = ['theme', 'text']


class UpdateProfile(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
    
    def __init__(self, *args, **kwargs):
        super(UpdateProfile, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs\
            .update({
                'placeholder': 'Введите новое имя: ',
                'class': 'form-control form-inp input-lg'
            })
        self.fields['email'].widget.attrs\
            .update({
                'placeholder': 'Введите почту: ',
                'class': 'form-control form-inp input-lg'
            })
        

class ProfileAvatar(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['avatar']

