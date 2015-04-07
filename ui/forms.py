from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserForm(forms.Form):
    username = forms.CharField(max_length=128, help_text="Please enter the category name.")
    password = forms.CharField(widget=forms.PasswordInput())
    
    def clean(self):
        
        print 'user'
        print self.cleaned_data.get('username') 

        if (self.cleaned_data.get('username') is None):
            

            raise ValidationError(
                "Email addresses must match."
            )

        return self.cleaned_data

    # An inline class to provide additional information on the form.
    #class Meta:
    #    # Provide an association between the ModelForm and a model
    #    model = User
    #    fields = ('username','password')