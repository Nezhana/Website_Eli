from django.forms import ModelForm, TextInput, Textarea
from .models import Cooperation

class CooperationForm(ModelForm):

    class Meta:
        model = Cooperation
        fields = ['firstname', 'email', 'comment']

        widgets = {
            'firstname': TextInput(attrs={
                'placeholder': 'Ваше ім’я'
            }),
            'email': TextInput(attrs={
                'placeholder': 'Ваш Email'
            }),
            'comment': Textarea(attrs={
                'placeholder': 'Коментар з Вашими ідеями',
                'style': "height:100px"
            }),
        }