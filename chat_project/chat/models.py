from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Chatroom(models.Model):
    name = models.CharField(max_length=100, unique=True)
    creator = models.ForeignKey("chat.User", null=True, on_delete=models.SET_NULL, related_name="created_chatrooms")

    def __str__(self):
        return f"{self.pk}_{self.name}"


class User(AbstractUser):
    # current_chatrooms = models.ManyToManyField(Chatroom, related_name="users_online")
    chatroom_invitations = models.ManyToManyField(Chatroom, blank=True, related_name="invited_users")
