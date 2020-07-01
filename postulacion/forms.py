from django import forms
from .models import postulantes


class PostulantesForm(forms.ModelForm):

    class Meta:
        model = postulantes
        fields = ['nombre',
                  'email',
                  'rut',
        ]
