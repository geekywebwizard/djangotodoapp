
from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import List


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed" ]