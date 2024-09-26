from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission,UserManager
from django.utils.translation import gettext_lazy as _

GENDER = (
    ('Gender', 'Gender'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Common', 'Common')
)

# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, email=None, password=None, **extra_fields):
#         if not username:
#             raise ValueError(_('The Username field must be set'))
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(_('email address'), null=True, blank=True)
    contact_number = models.CharField(max_length=14, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='images', null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, default='Gender')
    date_of_birth=models.CharField(max_length=1000,null=True,blank=True)
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions_set', blank=True)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','date_of_birth']
    objects = UserManager()

    class Meta:
        db_table = 'users'
        verbose_name_plural = 'Users'
        verbose_name = 'User'
        ordering = ['-date_joined']

    def __str__(self):
        return str(self.username)
    
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
    user = models.ForeignKey(User, on_delete=models.PROTECT,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'user_addresses'
        indexes = [
            models.Index(fields=['-created_at']),
        ]
    
    def __str__(self):
        return str(self.user.username)