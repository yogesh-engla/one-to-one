
from django import forms
from .models import StudentModel,AadharModel

class Aadhar_Form(forms.ModelForm):
    class Meta:
        model = AadharModel
        fields = '__all__'


class Student_Form(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
