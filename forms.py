from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django .utils. translation import gettext,gettext_lazy as  _
from .models import newpost,newimage

class SignUpForm(UserCreationForm):
    password1=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='confirm password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}) )
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
        labels={'first_name':'First Name', 'last_name':'Last Name','email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))    
    password=forms.CharField(label= _("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))


class postform(forms.ModelForm):
    class Meta:
        model=newpost
        fields=['title','description']
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
        'description':forms.Textarea(attrs={'class':'form-control'}),}
        #'photos':forms.Textarea(attrs={'class':'form-control'}),
        #'dates':forms.Textarea(attrs={'class':'form-control'}),}

class img_form(forms.ModelForm):
    class Meta:
        model=newimage
        fields=['image']
        #widgets={'image':forms.ImageField}