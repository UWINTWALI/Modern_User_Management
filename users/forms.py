from django import forms
from .models import User, Country, Province, District, Sector, Cell, Village

class UserForm(forms.ModelForm):
    foreign_location = forms.CharField(
        max_length=255, required=False,
        help_text="Enter foreign location if you are not from this country.",
        widget=forms.TextInput(attrs={'class': 'form-control'})  # Bootstrap styling
    )

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'userid', 'sex', 'phone', 'email', 'profile_picture',
            'is_foreigner', 'country', 'province', 'district',
            'sector', 'cell', 'village', 'foreign_location'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name...'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name...'}),
            'userid': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter User ID...'}),
            'sex': forms.Select(choices=[('M', 'Male'), ('F', 'Female'), ('I', 'Intersex')], attrs={'class': 'form-select'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email..'}),
            'is_foreigner': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'country': forms.Select(attrs={'class': 'form-select'}),
            'province': forms.Select(attrs={'class': 'form-select'}),
            'district': forms.Select(attrs={'class': 'form-select'}),
            'sector': forms.Select(attrs={'class': 'form-select'}),
            'cell': forms.Select(attrs={'class': 'form-select'}),
            'village': forms.Select(attrs={'class': 'form-select'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'})  # For file uploads

        }

    def clean(self):
        cleaned_data = super().clean()
        is_foreigner = cleaned_data.get('is_foreigner')
        foreign_location = cleaned_data.get('foreign_location')
        country = cleaned_data.get('country')  # Get country value

        if is_foreigner:
            if not foreign_location:
                self.add_error('foreign_location', "Foreign location is required for foreigners.") # Use add_error
            # Clear local fields
            cleaned_data['country'] = None
            cleaned_data['province'] = None
            cleaned_data['district'] = None
            cleaned_data['sector'] = None
            cleaned_data['cell'] = None
            cleaned_data['village'] = None
        else:
            # If the user is not a foreigner, clear foreign_location
            cleaned_data['foreign_location'] = None

            # Ensure at least one local field is filled
            if not any([cleaned_data.get('country'), cleaned_data.get('province'),
                        cleaned_data.get('district'), cleaned_data.get('sector'),
                        cleaned_data.get('cell'), cleaned_data.get('village')]):
                self.add_error(None, "At least one local location field must be selected.") #Use add_error

        return cleaned_data
