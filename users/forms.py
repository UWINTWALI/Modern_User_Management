from django import forms
from .models import User, Location

class UserForm(forms.ModelForm):
    location_name = forms.CharField(max_length=255, required=False, help_text="Start typing a location...")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'profile_picture', 'location']

    def clean(self):
        cleaned_data = super().clean()
        location_name = cleaned_data.get('location_name')
        
        if location_name:
            location, created = Location.objects.get_or_create(name=location_name)
            cleaned_data['location'] = location
        
        return cleaned_data
