from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email



# from django.db import models
# from django.forms import ValidationError
# from django.contrib.auth.models import AbstractUser, BaseUserManager
# from django.utils.translation import gettext_lazy as _
# class UserAccountManager(BaseUserManager):
#    use_in_migrations = True
#    def _create_user(self, email, name, password, **extra_fields):
#       if not email:
#          raise ValueError(_('Username must have an email'))
#       if not name:
#          raise ValueError(_('Username must be set'))
#       name = name
#       email = self.normalize_email(email)
#       user = self.model(name=name, email=email, **extra_fields)
#       user.set_password(password)
#       user.save(using=self._db)
#       return user
#    def create_user(self, email, name, password, **extra_fields):
#      extra_fields.setdefault('is_staff',False)
#      extra_fields.setdefault('is_superuser',False)
#      extra_fields.setdefault('is_active',True)
#    def create_superuser(self, email, name, password, **extra_fields):
#      extra_fields.setdefault('is_staff',True)
#      extra_fields.setdefault('is_superuser',True)
#      extra_fields.setdefault('is_active',True)
#      if extra_fields.get('is_staff') is not True:
#         raise ValueError(_('Superuser must have is_staff set to True'))
#      if extra_fields.get('is_superuser') is not True:
#         raise ValueError(_('Superuser must have is_superuser set to True'))
#         return self._create_user(email, name, password, **extra_fields)
# class UserAccount(AbstractUser):
#    email = models.EmailField(unique=True)
#    name = models.CharField(max_length=255)
#    is_staff = models.BooleanField(default=False)
#    is_superuser = models.BooleanField(default=False)
#    is_active = models.BooleanField(default=True)
#    USERNAME_FIELD = 'email'
#    REQUIRED_FIELDS = ['name']
#    objects = UserAccountManager()
# def __str__(self):
#    return self.email








# from charset_normalizer import from_path
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# class UserAccountManager(BaseUserManager):
#     def create_user(self,email,username,password = None, ):
#         if not email:
#             raise ValueError("Email field is required!")
#         elif not username:
#             raise ValueError("Username field is required!")
#         #user = self.create_user(email, username, password)

#         email = self.normalize_email(email)
#         user = self.model(username = username,email = email)
#         user.set_password(password)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()

#         return user

#     def create_superuser(self, username, password=None):
#         user = self.create_user(
#             username = username,
#             password=password,
#             is_staff=True,
#             is_admin=True
#         )
#         return user

#     #def create_superuser(self, email, username, password=None):
#         # if not email:
#         #     raise ValueError("Email field is required!")
#         # elif not username:
#         #     raise ValueError("Username field is required!")
#         # #user = self.create_user(email, username, password)

#         # email = self.normalize_email(email)
#         # user = self.model(username = username,email = email)
#         # user.set_password(password)
#         # user.is_superuser = True
#         # user.is_staff = True
#         # user.save()

#         # return user

# class UserAccount(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=255, unique=True)
#     username = models.CharField(max_length=255)
#     #name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = UserAccountManager()

#     USERNAME_FIELD = 'email'#Default Login Field
#     REQUIRED_FILELDS = ['username']

#     def get_full_name(self):
#         return self.username
    
#     def get_short_name(self):
#         return self.username

#     def __str__(self):
#         return self.email

# # Create your models here.


