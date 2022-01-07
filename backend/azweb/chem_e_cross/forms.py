from django import forms
from .models import User_Chem_e_cross

class RegisterForm2(forms.Form):
    # username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), )
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), )
    # alternate_phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False )
    college = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    current_year = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}),)
    # permanent_address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'rows':3}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    pincode = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=True )