
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from django import forms

class CreateUserForm(UserCreationForm):
    
    class Meta:
        
        model =User
        fields = ['username','email','password1','password2']
        
    # accessing fields that are defined in user models.    
    def __init__(self, *args , **kwargs):
        super(CreateUserForm,self).__init__ (*args, **kwargs)
        
        
        
        
     # Email Validations   
    def clean_email(self):
        
        email = self.cleaned_data.get("email")
        
        if User.objects.filter(email=email).exists():
            
            raise forms.ValidationError('This email is invalid !')
        
        if len(email>=350):
            raise forms.ValidationError('This email is too long')
        
        
        




















