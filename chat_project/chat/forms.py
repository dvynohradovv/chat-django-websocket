from django import forms
from django.core.exceptions import ValidationError

from .models import Chatroom


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "input", "placeholder": "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "input", "placeholder": "Password"}))

    def clean_username(self):
        data = self.cleaned_data["username"]
        for char in data:
            if not char.isalpha():
                raise ValidationError("Only letters!")
        return data


class ChatRoomForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "input", "placeholder": "New Chatroom"}))

    class Meta:
        model = Chatroom
        fields = ["name"]
