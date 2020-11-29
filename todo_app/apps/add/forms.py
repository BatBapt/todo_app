from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError

from .models import Task


class AddTaskForm(forms.Form):

    my_default_errors = {
        'required': 'Ce champ est requis',
        'invalid': 'Entrez une bonne valeur',
    }

    title = forms.CharField(label="Titre", required=True, max_length=250, widget=forms.TextInput(attrs={
        "class": "form-control",
    }), error_messages=my_default_errors)

    content = forms.CharField(label='Details', required=True, widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 4,
        "cols": 15,
    }), error_messages=my_default_errors)

    due_date = forms.DateField(label="A faire pour le...", required=True,
                               widget=forms.DateTimeInput(attrs={
                                   "class": "form-control",
                                   "type": "date",
                               }), error_messages=my_default_errors)

