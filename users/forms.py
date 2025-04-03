from django import forms
from .models import User, UserLocation, ForeignerLocation




class UserLocationForm(forms.ModelForm):

    class Meta:
        model = UserLocation
        fields = ['country', 'province', 'district', 'sector', 'cell', 'village']

        widgets = {
                'country': forms.TextInput( attrs={'class': 'form-control', 'id': 'id_country', 'placeholder': 'Select your country'}),
                'province': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_province', 'placeholder': 'Select province'}),
                'district': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_district', 'placeholder': 'Select district'}),
                'sector': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_sector', 'placeholder': 'Select sector'}),
                'cell': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_cell', 'placeholder': 'Select cell'}),
                'village': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_village', 'placeholder': 'Select village'}),
        }

class ForeignerLocationForm(forms.ModelForm):

    foreign_location = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'locationInput', 'placeholder': 'select Or Enter foreign location ...',  'style': 'width: 500px;'}))

    class Meta:
        model = ForeignerLocation
        fields = ['foreign_location']
   
class UserForm(forms.ModelForm):
    sex = forms.ChoiceField(choices=User.SEX_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'userid', 'sex', 'phone', 'email',
            'profile_picture', 'is_foreigner'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'first_name', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'last_name', 'placeholder': 'Last Name'}),
            'userid': forms.TextInput(attrs={'class': 'form-control', 'id': 'userid', 'placeholder': 'User ID'}),
            'sex': forms.Select(attrs={'class': 'form-control', 'id': 'sex'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone', 'placeholder': 'Phone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Email'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'profile_picture'}),
            'is_foreigner': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
