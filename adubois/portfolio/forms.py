from .models import MyWorks
from django.forms import ModelForm, TextInput, FileInput, Textarea


class MyWorkForm(ModelForm):
    class Meta:
        model = MyWorks
        fields = ('title', 'descriptions', 'image')

        widgets ={
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название работы'
            }),
            'descriptions': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание работы'
            })
        }