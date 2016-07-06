# -*- coding: utf-8 -*-
__author__ = 'coffe67'
from django import forms
from .models import ToDo

class ToDoForm(forms.ModelForm):

    class Meta:
        model = ToDo
        fields = ('name', 'slug', 'assigned')