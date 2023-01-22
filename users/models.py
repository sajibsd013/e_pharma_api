from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
credits = models.PositiveIntegerField(default=100)


USER_TYPE = (
    ('doctor', 'doctor'),
    ('nurse', 'nurse'),
    ('caregiver', 'caregiver'),
    ('physiotherapist', 'physiotherapist'),
    ('partner ', 'partner '),
    ('patient', 'patient'),
)


# Create your models here
class MyUserManager(BaseUserManager):
    def create_user(self, phone, full_name, password=None):
        """
        Creates and saves a User with the given phone, date of
        birth and password.
        """
        if not phone:
            raise ValueError('Users must have an phone address')

        user = self.model(
            phone=phone,
            full_name=full_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, full_name, password=None):
        """
        Creates and saves a superuser with the given phone, date of
        birth and password.
        """
        user = self.create_user(
            phone,
            password=password,
            full_name=full_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    phone = models.CharField(
        max_length=255,
        unique=True,
    )
    full_name = models.CharField(
        max_length=255,
    )
    email = models.CharField(
        max_length=255, null=True, blank=True
    )
    birthday = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    user_type = models.CharField(
        max_length=120, choices=USER_TYPE, default="patient", )
    expiry_date = models.DateTimeField(null=True, blank=True)
    objects = MyUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        verbose_name_plural = "Users"
