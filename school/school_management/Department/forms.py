from django import forms
from Account.models import Materials


from .models import Department,Course
from order.models import Order

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']        

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Materials
        fields = ['name']              