from django import forms
from .models import user
class userForm(forms.ModelForm):

    class Meta:
        model = user
        fields = '__all__'
        labels = {
            'FirstName':'First Name',
            'LastName':'Last Name',
            'DoB':'Date Of Birth'
        }