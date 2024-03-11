from django import forms 
from django.contrib.auth import get_user_model

User=get_user_model()

class RegistrationForm(forms.ModelForm):
    password1=forms.CharField(max_length=16,min_length=8,widget=forms.PasswordInput,label='Password',)
    password2=forms.CharField(max_length=16,min_length=8,widget=forms.PasswordInput,label='Confirm  Password',)
    
    class Meta:
        model=User
        fields='__all__'
        
    def clean_passoword2(self):
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')
        
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError(f'Password Doesn\'t match ') 
        return password2
    
    def save(self,commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        
        if commit:
            user.save()
            
        return user
        
        
        