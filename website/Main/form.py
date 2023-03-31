from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User, Album
from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput


class MyUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
    label="Password",
    widget=forms.PasswordInput(attrs={'class':'form-control, p-3 bg-info bg-opacity-10 border border-info border rounded', 'type':'password', 'align':'center', 'placeholder':'Password', 'id':'form3Example4c' }),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control, p-3 bg-info bg-opacity-10 border border-info border rounded', 'type':'password', 'align':'center', 'placeholder':'Repeat your password', 'id':'form3Example4cd'}),
    )
    class Meta:
        model = User
        
        fields = ['name', 'username', 'email', 'password1', 'password2', 'grade', 'section']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control, p-3 bg-info bg-opacity-10 border border-info border rounded',
                'placeholder': 'Enter your name ',
                'type':'text',
                'id':'form3Example1c'
            }),
            'username': TextInput(attrs={
                'class': 'form-control, p-3 bg-info bg-opacity-10 border border-info border rounded',
                'placeholder': 'Enter your username',
                'id':'fuckuser',
                'type':'text',
            }),
            'email': EmailInput(attrs={
                'class': 'form-control, p-3 bg-info bg-opacity-10 border border-info border rounded',
                'placeholder': 'Enter your email',
                'id':'form3Example3c',
                'type':'email'
            }),
            
            'grade': TextInput(attrs={
                'class': 'form-control, p-3 bg-info bg-opacity-10 border border-info border rounded',
                'placeholder': 'Enter your grade',
                'id':'fuckg',
                'type':'text',
            }),
            'section': TextInput(attrs={
                'class': 'form-control, p-3 bg-info bg-opacity-10 border border-info border rounded'  ,
                'placeholder': 'Enter your section',
                'id':'fucks',
                'type':'text',
            }),
        }


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants', 'type', 'topic', 'description']




class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']


class AlbumForm(ModelForm):

    class Meta:
        model = Album
        fields = ['artist', 'album_title', 'genre', 'album_logo', 'audio_file', 'song_title']


class ChatFrom(ModelForm):
    class Meta:
        pass
