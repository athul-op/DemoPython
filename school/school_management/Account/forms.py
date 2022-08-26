from  django import forms
from . models import Account




class RegistrationForm(forms.ModelForm):


    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=Account
        fields=['username','email','password','mobile']

        

    def _init_(self,*args,**kwargs):
        super(RegistrationForm ,self)._init_(*args,**kwargs)  

        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
        


    def clean(self):

        cleaned_data    =super(RegistrationForm,self).clean()
        password        =cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')    

        if password != confirm_password:
            raise forms.ValidationError("Password does not match")



