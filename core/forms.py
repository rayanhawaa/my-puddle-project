from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'your username',
            'style':'width:100%; padding-inline:0.4rem;padding-block:0.6rem;borders-radius:10px;',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'your password',
            'style':'width:100%; padding-inline:0.4rem;padding-block:0.6rem;borders-radius:10px;',
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'your username',
            'style':'width:100%; padding-inline:0.4rem;padding-block:0.6rem;borders-radius:10px;',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'your email',
            'style':'width:100%; padding-inline:0.4rem;padding-block:0.6rem;borders-radius:10px;',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'your password',
            'style':'width:100%; padding-inline:0.4rem;padding-block:0.6rem;borders-radius:10px;',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'repeat password',
            'style':'width:100%; padding-inline:0.4rem;padding-block:0.6rem;borders-radius:10px;',
    }))