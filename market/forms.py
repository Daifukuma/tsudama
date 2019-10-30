from django.forms import ModelForm
from .models import Textbook
#from django import forms

class TextbookForm(ModelForm):
    class Meta:
        model = Textbook
        fields = ['title', 'image', 'department', 'schoolyear', 'lesson', 'comment', 'status', 'point']
#        widgets = {
#            'title': forms.textInput(attrs={'placeholder':'教科書のタイトル'}),
#            'comment': forms.teztarea(attrs={'rows':4}),
#        }

class SearchForm(ModelForm):
    class Meta:
        model = Textbook
        fields = ['title', 'department']
