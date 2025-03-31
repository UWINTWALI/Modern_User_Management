from django import forms
from .models import User, UserLocation

class UserForm(forms.ModelForm):
    # Fields for the User model
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
                                        
                                        

    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last Name'}))
    userid = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User ID'}))
    sex = forms.ChoiceField(choices=User.SEX_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Sex'}))
    phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    profile_picture = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))

    # Location fields
    is_foreigner = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    
    country = forms.ChoiceField( choices=[('', 'Select country')] + [], widget=forms.Select(attrs={'id': 'id_country', 'class': 'form-control'}))
    province = forms.ChoiceField( choices=[('', 'Select province')] + [], widget=forms.Select(attrs={'id': 'id_province', 'class': 'form-control'}))
    district = forms.ChoiceField( choices=[('', 'Select district')] + [], widget=forms.Select(attrs={'id': 'id_district', 'class': 'form-control'}))
    sector = forms.ChoiceField( choices=[('', 'Select sector')] + [],  widget=forms.Select(attrs={'id': 'id_sector', 'class': 'form-control'}))
    cell = forms.ChoiceField( choices=[('', 'Select cell')] + [],widget=forms.Select(attrs={'id': 'id_cell', 'class': 'form-control'}))
    village = forms.ChoiceField( choices=[('', 'Select village')] + [], widget=forms.Select(attrs={'id': 'id_village', 'class': 'form-control'}))

    # Foreign location for foreigners
    foreign_location = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'userid', 'sex', 'phone', 'email', 
            'profile_picture', 'is_foreigner', 'country', 'province', 
            'district', 'sector', 'cell', 'village', 'foreign_location'
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        # Optionally create or update the location if the user is local
        if not user.is_foreigner:
            location = UserLocation.objects.create(
                country=self.cleaned_data['country'],
                province=self.cleaned_data['province'],
                district=self.cleaned_data['district'],
                sector=self.cleaned_data['sector'],
                cell=self.cleaned_data['cell'],
                village=self.cleaned_data['village']
            )
            user.location = location
            user.save()
        return user
