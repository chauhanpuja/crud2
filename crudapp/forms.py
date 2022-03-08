
from . models import User_Data
from django import forms

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User_Data
        fields = ['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class' :'form-control'}),
            'email':forms.EmailInput(attrs={'class' :'form-control'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class' :'form-control'}),
        }

