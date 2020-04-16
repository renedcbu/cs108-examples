from django import * #forms
from .models import * #Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):

    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2012,1920,-1),),)
    city = forms.CharField(label="City", required=True)
    email_adress = forms.CharField(label="Email Adress", required=True)
    image_url = forms.URLField(label="Image url", required=False)

    class Meta:
        """Associate this form with the Profile model."""
        model = Profile
        fields = ['first_name', 'last_name', 'birth_date', 'city', 'email_adress', 'image_url']

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        """Associate this form with the Profile model."""
        model = Profile
        fields = {'city', 'email_adress', 'image_url'}

class CreateStatusMessageForm(forms.ModelForm):

    image = forms.ImageField(label="Image", required = False)

    class Meta:
        """Associate this form with the StatusMessage model."""
        model = StatusMessage
        fields = ['message', 'image',]
