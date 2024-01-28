from .models import Events, GalleryItem
from django.forms import ModelForm, DateInput, TextInput, Textarea, forms, Form, FileField


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


class UploadFileForm(forms.Form):
    file = forms.FileField(label='file')

# class LoadImageForm(ModelForm):
#     class Meta:
#         model = GalleryItem
#         fields = ['file', 'title', 'text']
#
#         widgets = {
#             'file': FileField(attrs={
#                 'class':'form-control',
#                 'placeholder':"file"
#             }),
#             'title': TextInput(attrs={
#                 'class':'form-control',
#                 'placeholder':"title"
#             }),
#             'text': TextInput(attrs={
#                 'class':'form-control',
#                 'placeholder':"some_info"
#             }),
#         }