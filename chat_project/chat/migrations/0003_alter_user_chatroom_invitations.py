# Generated by Django 4.0.3 on 2022-03-22 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_user_chatroom_invitations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='chatroom_invitations',
            field=models.ManyToManyField(null=True, related_name='invited_users', to='chat.chatroom'),
        ),
    ]
