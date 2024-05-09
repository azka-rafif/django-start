import bcrypt
from django import forms 

class SignupForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password')
    nama = forms.CharField(label='Nama')
    GENDER_CHOICES = [(0, 'Male'), (1, 'Female')]
    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES, widget=forms.RadioSelect)
    tempat_lahir = forms.CharField(label='Tempat Lahir')
    kota_asal = forms.CharField(label='Kota Asal')
    tanggal_lahir = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d', '%Y/%m/%d', '%Y%m%d'],
    )
    ROLES_CHOICES = (
        ('podcaster', 'Podcaster'),
        ('songwriter', 'Songwriter'),
        ('artist', 'Artist'),
    )
    roles = forms.MultipleChoiceField(
        label='Roles',
        required=True, 
        choices=ROLES_CHOICES,
        widget=forms.CheckboxSelectMultiple,
    )

class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
