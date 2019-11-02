from django.forms import ModelForm
from .models import Textbook, Department
from django import forms
from . import models

class TextbookForm(ModelForm):
    class Meta:
        model = Textbook
        fields = ['title', 'image', 'department', 'schoolyear', 'lesson', 'comment', 'status', 'point']
#        widgets = {
#            'title': forms.textInput(attrs={'placeholder':'教科書のタイトル'}),
#            'comment': forms.teztarea(attrs={'rows':4}),
#        }

#class SearchForm(ModelForm):
#    class Meta:
#        model = Textbook
#        fields = ['title', 'department']
#    model = Textbook
#    fields = ['title', 'image', 'department', 'schoolyear', 'lesson', 'comment', 'status', 'point']
#    title = model.CharField(label='タイトル', required=False)
#    department = model.ChoiceField(label='学科', choices=Department, required=False)

class SearchForm(forms.Form):
    department = forms.ModelChoiceField(models.Department.objects, label='学科', empty_label='洗濯してください')
    title = forms.CharField(max_length=30, label='タイトル')
