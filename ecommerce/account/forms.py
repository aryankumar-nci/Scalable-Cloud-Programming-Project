
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import PasswordInput, TextInput


# Registration form

class CreateUserForm(UserCreationForm):
    
    class Meta:
        
        model =User
        fields = ['username','email','password1','password2']
        
    # accessing fields that are defined in user models.    
    def __init__(self, *args , **kwargs):
        super(CreateUserForm,self).__init__ (*args, **kwargs)
        
        # makes email field as required.
        self.fields['email'].required = True
        
        
        
        
    # Email Validations   
    def clean_email(self):
        
        email = self.cleaned_data.get("email")
        
        if User.objects.filter(email=email).exists():
            
            raise forms.ValidationError('This email is invalid !')
        
        # len function updated
        if len(email)>=350:
            raise forms.ValidationError('This email is too long')

        # saves email to the database.
        return email
        


#Login Form

class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
    
#update form

class UpdateUserForm(forms.ModelForm):
    
    password = None
    
    class Meta:
        
        model = User
        
        fields = ['username','email']
        exclude = ['password1','password2'] 
    
     # accessing fields that are defined in user models.    
    def __init__(self, *args , **kwargs):
        super(UpdateUserForm,self).__init__ (*args, **kwargs)
        
        # makes email field as required.
        self.fields['email'].required = True
    
    
    
     # Email Validations form  
    def clean_email(self):
        
        email = self.cleaned_data.get("email")
        
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            
            raise forms.ValidationError('This email is invalid !')
        
        # len function updated
        if len(email)>=350:
            raise forms.ValidationError('This email is too long')

        # saves email to the database.
        return email
        


















