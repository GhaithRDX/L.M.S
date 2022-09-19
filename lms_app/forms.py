from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-input',
                                                             'id':'name',
                                                             'name':'username',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-input',
                                                           'name':'email',
                                                           'id':'email',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-input',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password1',
                                                                  'name':'password1',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-input',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password2',
                                                                  'name':'password2',
                                                                  }))

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title',
                  'author',
                  'photo_book',
                  'photo_author',
                  'pages',
                  'price',
                  'retal_price_day',
                  'retal_period',
                  'total_rental',
                  'status',
                  'category')
        widgets = {
            'title': forms.TextInput(attrs={"class":"form-control"}),
            'author': forms.TextInput(attrs={"class":"form-control"}),
            'photo_book': forms.FileInput(attrs={"class":"form-control"}),
            'photo_author': forms.FileInput(attrs={"class":"form-control"}),
            'pages': forms.NumberInput(attrs={"class":"form-control"}),
            'price': forms.NumberInput(attrs={"class":"form-control"}),
            'retal_price_day': forms.NumberInput(attrs={"class":"form-control" ,'id':'dayrental'}),
            'retal_period': forms.NumberInput(attrs={"class":"form-control" ,'id':'periodrental'}),
            'total_rental':forms.NumberInput(attrs={"class":"form-control" ,'id':'totalrental'}),
            'status': forms.Select(attrs={"class":"form-control"}),
            'category': forms.Select(attrs={"class":"form-control"}),
        }

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields =[ 'name']
        widgets ={
            'name':forms.TextInput(attrs={"class":"form-control"})
        }
