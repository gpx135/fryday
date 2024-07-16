from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, RegexValidator
from django.contrib.postgres.indexes import GinIndex
from django.utils.translation import gettext_lazy as _



from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.core.validators import RegexValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.indexes import GinIndex

class User(AbstractUser):
    """
    Extended user model with additional fields for user information.
    """
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(
        max_length=20,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )
    street = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(
        max_length=20,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^\d{5}(-\d{4})?$',
                message="Postal code must be in the format: '12345' or '12345-6789'."
            )
        ]
    )
    country = models.CharField(max_length=100, blank=True)
    birthday = models.DateField(null=True, blank=True)
    loyalty_points = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    preferred_language = models.ForeignKey('localization.Language', on_delete=models.SET_NULL, null=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    additional_info = models.JSONField(default=dict, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Unique related_name to avoid clashes
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # Unique related_name to avoid clashes
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    class Meta:
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['birthday']),
            GinIndex(fields=['additional_info']),
        ]
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def save(self, *args, **kwargs):
        if self.pk is not None:
            original_birthday = User.objects.get(pk=self.pk).birthday
            if self.birthday != original_birthday:
                raise ValueError("Changing the birthday field is not allowed.")
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username


class UserThirdPartyLogin(models.Model):
    """Stores third-party login information for users."""
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider = models.CharField(max_length=50)
    provider_user_id = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=['provider', 'provider_user_id'])]
        verbose_name = _("User Third Party Login")
        verbose_name_plural = _("User Third Party Logins")

    def __str__(self):
        return f"{self.user.username} - {self.provider}"
    

class UserGroup(models.Model):
    """Stores user groups for special pricing."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = _("User Group")
        verbose_name_plural = _("User Groups")

    def __str__(self):
        return self.name


class UserGroupMembership(models.Model):
    """Associates users with user groups."""
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'user_group')
        verbose_name = _("User Group Membership")
        verbose_name_plural = _("User Group Memberships")

    def __str__(self):
        return f"{self.user.username} - {self.user_group.name}"


class UserDietaryPreference(models.Model):
    """Associates users with their dietary preferences."""
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dietary_preference = models.ForeignKey('menu.DietaryPreference', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'dietary_preference')
        verbose_name = _("User Dietary Preference")
        verbose_name_plural = _("User Dietary Preferences")

    def __str__(self):
        return f"{self.user.username} - {self.dietary_preference.name}"
