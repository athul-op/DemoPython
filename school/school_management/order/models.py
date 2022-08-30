from django.db import models
from Account.models import Account,Materials
from Department.models import Course
from Department.models import Department


class Order(models.Model):

    purpose_types = (
        ('Enquiry', 'Enquiry'),
        ('place_order', 'place_order')
    )

    TYPES = (

        ('Male' , 'Male'),
        ( 'Woman' , 'Woman'),
    )


    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    mobile =  models.CharField(max_length=10,null=True,blank=True)
    user =models.ForeignKey(Account,on_delete=models.CASCADE,null=True)
    date_of_birth =  models.DateField(null=True,blank=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, choices=TYPES)
    address=models.TextField()
    course        = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    purpose       = models.TextField(max_length=255, choices=purpose_types)
    materials     = models.ForeignKey(Materials,on_delete=models.CASCADE,null=True)
    department    = models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.name