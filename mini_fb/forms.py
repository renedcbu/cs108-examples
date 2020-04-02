from django import forms
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):

    first_name = forms.CharField(label="First Name", required=True)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2012,1920,-1),),)

    # ...

    