from .models import Events
from django.forms import ModelForm, DateInput, Textarea


class EventsForm(ModelForm):
    class Meta:
        model = Events
        fields = ['text', 'date']

        widgets = {
            "text": Textarea(attrs={
                'class':'form-control',
                'placeholder':"Some info"
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': "Date"
            })
        }