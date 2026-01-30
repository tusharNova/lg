from django import forms

from .models import Employees

class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['name'].widget.attrs.update({
    #         'class': 'form-control', 
    #         'placeholder': 'Enter your nick name'
    #     })
    #     self.fields['email'].widget.attrs.update({
    #         'class': 'form-control',
    #         'placeholder': 'Enter your business email'
    #     })
    #     self.fields['department'].widget.attrs.update({
    #         'class': 'form-control', 
    #         # 'placeholder': 'Enter your nick name'
    #     })
    #     self.fields['salary'].widget.attrs.update({
    #         'class': 'form-control', 
    #         # 'placeholder': 'Enter your nick name'
    #     })
        
        
