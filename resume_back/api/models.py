from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth.models import Group, Permission
from django.conf import settings

USER_ROLES = [
    ("user", "일반 사용자"),
    ("admin", "관리자"),
]

class CustomUserManager(BaseUserManager):
    def create_user(self, user_id, username, email, phone, password=None, **extra_fields):
        if not user_id:
            raise ValueError("아이디는 필수입니다.")

        user = self.model(user_id=user_id, username=username, email=self.normalize_email(email) if email else None, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, username, email, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(user_id, username, email, phone, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(max_length=30, unique=True)
    username = models.CharField(max_length=30)
    email = models.EmailField(unique=True, blank=True)
    phone = models.CharField(max_length=15, unique=True, blank=True)
    role = models.CharField(max_length=20, choices=USER_ROLES, default="user")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="customuser_set", # related_name 추가
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_set", # related_name 추가
        related_query_name="user",
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "user_id"
    REQUIRED_FIELDS = ["username","email","phone"]

    def __str__(self):
        return self.user_id

