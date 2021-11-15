from django import forms
from django.forms import ModelForm
from .models import Customer
class CustomerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix','')
        super(CustomerForm, self).__init__(*args, **kwargs)

    fname = forms.CharField(label='First_Name:-', widget=forms.TextInput(attrs={'class': 'form-control'}))
    lname = forms.CharField(label='Last_Name:-', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email_id:-', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    age = forms.CharField(label='Age:-', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    con = forms.CharField(label='Contact-No:-', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    add = forms.CharField(label='LandMark:-', widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(label='State:-', widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(label='City:-', widget=forms.TextInput(attrs={'class': 'form-control'}))
    zip = forms.CharField(label='Zip_Code:-', widget=forms.TextInput(attrs={'class': 'form-control'}))
    post = forms.CharField(label='Post_Office:-', widget=forms.TextInput(attrs={'class': 'form-control'}))
    skill = forms.CharField(label='Skill:-', widget=forms.TextInput(attrs={'class': 'form-control'}))
    ho1 = forms.CharField(label='Hobbies1:-', widget=forms.TextInput(attrs={'class': 'form-control'}))
    ho2 = forms.CharField(label='Hobbies2:-', widget=forms.TextInput(attrs={'class': 'form-control'}))
    ho3 = forms.CharField(label='Hobbies3:-', widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Customer
        fields = ['fname','lname','email','age','con','add','state','city','zip','post','skill','ho1','ho2','ho3']