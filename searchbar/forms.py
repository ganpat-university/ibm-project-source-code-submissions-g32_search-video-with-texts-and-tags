from django import forms
from .models import *

class Videoform(forms.Form):
    search= forms.CharField(max_length=100)

# class VideoSearchform(forms.ModelForm):  
#     class Meta:  
#         # To specify the model to be used to create form  
#         model = Video  
#         # It includes all the fields of model  
#         fields = '__all__' 