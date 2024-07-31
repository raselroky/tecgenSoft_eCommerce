from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _



GENDER=(
    ('Gender','Gender'),
    ('Male','Male'),
    ('Female','Female'),
    ('Common','Common')
)

class Users(AbstractBaseUser):
   
    username = models.CharField(max_length=500)
    email = models.EmailField(_('email address'),null=True,blank=True)
    contact_number = models.CharField(max_length=14, null= True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=500,null=True,blank=True)
    last_name = models.CharField(max_length=500,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    profile_pic = models.FileField(upload_to='images',null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, default='Gender')
    
    last_login = None

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['contact_number','email']
    objects = UserManager()
    

    class Meta:
        db_table = 'userss'
        verbose_name_plural = 'Users'
        verbose_name = 'User'
        ordering = ['-date_joined']

    def __str__(self):
        return self.username
    
    @property
    def get_full_name(self):
        if(self.first_name and self.last_name):
            return str(self.first_name) + ' ' + str(self.last_name)
        else:
            if(self.first_name):
                return str(self.first_name)
            elif(self.last_name):
                return str(self.last_name)





class UserAddress(models.Model):
    user = models.ForeignKey(Users, on_delete=models.PROTECT,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'user_addresses'
        indexes = [
            models.Index(fields=['-created_at']),
        ]
    
    def __str__(self):
        return self.user.username