from pickle import TRUE
from django.db import models


from django.contrib.auth.models import AbstractBaseUser,BaseUserManager





class UserManager(BaseUserManager):
    def create_user(self,username,email,mobile,password=None,is_staff=False):
        
        if not email:
            raise ValueError('must have an email')

        if not mobile:
            raise ValueError('must have an number')    

        user=self.model(
            email  = self.normalize_email(email),
            mobile = mobile, 
            username =username,
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username,password,mobile):
    
        user = self.create_user(
            email = self.normalize_email(email),
            mobile = mobile,
            username=username,
            password = password,
            
        )
        user.is_admin   = True
        user.is_active  = True
        user.is_staff  = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

   
class Account(AbstractBaseUser):
    
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    mobile =  models.CharField(max_length=10,null=True,blank=True)
    is_staff      = models.BooleanField(default=False)
    is_active     = models.BooleanField(default=True)
    is_admin      = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)




    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','mobile']
    objects = UserManager()
    
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

class Materials(models.Model):

    name =models.CharField(max_length=100)

    def __str__(self) :
        return self.name





