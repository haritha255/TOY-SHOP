from django import forms

from . models import Reg_tbl

class regform(forms.ModelForm):
    class Meta:
        model = Reg_tbl
        fields =['mail','psw','cpsw','fname','lname','gender','loc']
        widgets = {
            'mail': forms.EmailInput
            (attrs = {'class':'form_control','placeholder':'Email','style':'width:500px; height:50px;border-radius:10px;border-color:skyblue'}),
            'psw': forms.PasswordInput
            (attrs = {'class':'form_control','placeholder':'password','style':'width:500px; height:50px;border-radius:10px;border-color:skyblue'}),
            'cpsw': forms.PasswordInput
            (attrs = {'class':'form_control','placeholder':'confirm-pssword','style':'width:500px; height:50px;border-radius:10px;border-color:skyblue'}),
            'fname': forms.TextInput
            (attrs = {'class':'form_control','placeholder':'Full-name','style':'width:500px; height:50px;border-radius:10px;border-color:skyblue'}),
            'lname': forms.TextInput
            (attrs = {'class':'form_control','placeholder':'last-name','style':'width:500px; height:50px;border-radius:10px;border-color:skyblue'}),
            'gender': forms.TextInput
            (attrs = {'class':'form_control','placeholder':'gender','style':'width:500px; height:50px;border-radius:10px;border-color:skyblue'}),
            'loc': forms.TextInput
            (attrs = {'class':'form_control','placeholder':'Location','style':'width:500px; height:50px;border-radius:10px;border-color:skyblue'}),
        }

# class regform(forms.Form):
#     Fullname = forms.CharField(max_length=25)
#     Mobile = forms.IntegerField()
#     Email = forms.EmailField()
#     Password = forms.CharField(max_length=25)
#     Confirmpassword = forms.CharField(max_length=25)      