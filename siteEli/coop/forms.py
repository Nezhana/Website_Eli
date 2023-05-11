from django.forms import ModelForm, TextInput, Textarea
from .models import Cooperation, Collaborator

class CooperationForm(ModelForm):

    class Meta:
        model = Cooperation
        fields = ['firstname', 'email', 'comment']

        widgets = {
            'firstname': TextInput(attrs={
                'placeholder': 'Ваше ім’я'
            }),
            'comment': Textarea(attrs={
                'placeholder': 'Коментар з Вашими ідеями',
                'style': "height:100px"
            }),
        }

class CollaboratorForm(ModelForm):

    class Meta:
        model = Collaborator
        fields = ['email']

        widgets = {
            'email': TextInput(attrs={
                'placeholder': 'Ваш Email'
            })
        }

    def clean(self):
        # data from the form is fetched using super function
        super(CollaboratorForm, self).clean()
        # extract the username and text field from the data
        email = self.cleaned_data.get('email')
        if len(email) < 5:
            self._errors['email'] = self.error_class([
                'Minimum 5 characters required'])
        # return any errors if found
        return self.cleaned_data