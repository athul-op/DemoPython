from django import forms
from .models import Order,Course


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name','date_of_birth','mobile','email','address','age','gender','course','department','purpose','materials']
    

   

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).all()
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.pk:
        #     self.fields['course'].queryset = self.instance.department.course_set.order_by('name')