# -*- coding: utf-8 -*-
__author__ = 'coffe67'
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='User',
                               widget=forms.TextInput(attrs={'placeholder': 'User',
                                                             'class': 'form-control',
                                                             'required': True}))

    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'required': True}))


class SignUpForm(forms.ModelForm):

    username = forms.CharField(label='User',
                               widget=forms.TextInput(attrs={'placeholder': 'User',
                                                             'class': 'form-control',
                                                             'required': True}))

    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'required': True}))

    email = forms.CharField(label='Email',
                            widget=forms.EmailInput(attrs={'placeholder': 'mail@domain.com',
                                                           'class': 'form-control',
                                                           'required': True}))

    first_name = forms.CharField(label='First Name',
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               'required': True}))

    last_name = forms.CharField(label='Last Name',
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              'required': True}))

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        if 'password' in cleaned_data and cleaned_data['password']:
            if validate_password(cleaned_data['password']) is not None:
                self._errors['password'] = self.error_class([u'Password Invalid'])

        return cleaned_data


