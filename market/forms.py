from django.forms import ModelForm
from .models import Textbook

class TextbookForm(ModelForm):
    class Meta:
        model = Textbook
        fields = ['title', 'image', 'department', 'schoolyear', 'lesson', 'comment', 'status', 'point']
#        widgets = {
#            'title': forms.textInput(attrs={'placeholder':'教科書のタイトル'}),
#            'comment': forms.teztarea(attrs={'rows':4}),
#        }
