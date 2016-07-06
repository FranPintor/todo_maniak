# -*- coding: utf-8 -*-
__author__ = 'coffe67'
from django.contrib.auth.models import User
from django import forms
from .models import ToDo


def get_choices():
    items = User.objects.all().exclude(is_staff=True, is_superuser=True)
    choices = [(None, 'Chose User')]
    return choices + [(item.id, '%s %s' % (item.first_name, item.last_name)) for item in items]


class ToDoForm(forms.ModelForm):

    name = forms.CharField(label='ToDo Name',
                           widget=forms.TextInput(attrs={'placeholder': 'ToDo Name',
                                                         'class': 'form-control',
                                                         'id': 'todo_name',
                                                         'required': True}))

    slug = forms.CharField(label='Slug',
                           widget=forms.TextInput(attrs={'placeholder': 'Slug ToDo Name',
                                                         'class': 'form-control slug',
                                                         'required': False}))

    class Meta:
        model = ToDo
        fields = ('name', 'slug')
