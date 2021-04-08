# forms
from django import forms
from .models import Board, Category

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'descriptions', 'category']