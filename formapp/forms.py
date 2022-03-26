from django import forms
class RegForm(forms.Form):
    firstname=forms.CharField(max_length=10)
    lastname=forms.CharField(max_length=10)
    username=forms.CharField(max_length=15)
    password=forms.CharField(max_length=15)
    cpassword=forms.CharField(max_length=15)
    mailid=forms.EmailField()
    mobno=forms.IntegerField()