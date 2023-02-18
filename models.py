""" Snippets Data Models """


from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """ Users """

    image = models.ImageField(
        null=True,
        blank=True,
        help_text='Your profile picture'
    )
    bio = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text='Tell us about your self'
    )


class Snippet(models.Model):
    """ Code Snippets """

    # The owner of the snippet
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
