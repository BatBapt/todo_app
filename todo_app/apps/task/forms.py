from django import forms
import datetime

from .models import Category


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

    due_date = forms.DateTimeField(label="A faire pour le...", required=True, initial=datetime.date.today,
                                   widget=forms.DateTimeInput(attrs={
                                       "class": "form-control",
                                       "type": "date",
                                   }), error_messages=my_default_errors)


class AddCategoryForm(forms.Form):
    name = forms.CharField(label="Nom", required=True, max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control",
    }))

    color = forms.CharField(label="Couleur", required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "color",
        "value": "#e66465",
    }))
