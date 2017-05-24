from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# teste
class EmailUserManager(BaseUserManager):
    def create_user(self, *args, **kwargs):
        email = kwargs["email"]
        email = self.normalize_email(email)
        password = kwargs["password"]
        kwargs.pop("password")

        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.save(using=self._db)
        return user

class MyUser(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(
        verbose_name=_('Email address'),
        unique=True,
    )
    first_name = models.CharField(
        verbose_name=_('Nome'),
        max_length=50,
        blank=False,
    )
    last_name = models.CharField(
        verbose_name=_('Sobrenome'),
        max_length=50,
        blank=False
    )
    siape = models.IntegerField()

    USERNAME_FIELD = 'email'
    objects = EmailUserManager()

    def __str__(self):
        return self.email
