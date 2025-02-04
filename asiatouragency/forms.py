from typing import Any
from django import forms
from .models import FormInput
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def save_in_db(self):
        # print(self.cleaned_data['email'])
        FormInput.objects.create(
            name = self.cleaned_data['name'],
            email = self.cleaned_data['email'],
            message = self.cleaned_data['message'],
        )

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password_confirm',
        ]

    def clean(self) -> dict[str, Any]:
        cleaned_data =  super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Passwords Do Not Match!')
        return cleaned_data