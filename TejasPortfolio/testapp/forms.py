from django import forms
from testapp.models import ContactDb
class ContactDbForm(forms.ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.Textarea()
    class Meta:
        model = ContactDb
        fields = '__all__'