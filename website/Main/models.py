from django.db import models
from django.contrib.auth.models import AbstractUser 





class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(max_length= 100, blank = True, null=True)
    grade = models.CharField(max_length= 2, null = True)
    section = models.CharField(max_length= 6, null = True)
    title = models.CharField(max_length=100, null= True, blank=True, default=None)
    



    avatar = models.ImageField(blank = True, null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Album(models.Model):
    user = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
    artist = models.CharField(max_length=250, blank=True)
    album_title = models.CharField(max_length=500, blank=True)
    genre = models.CharField(max_length=100, blank=True)
    album_logo = models.FileField(blank=True)
    is_favorite = models.BooleanField(default=False)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='', blank=True)
    audio_address = models.CharField(max_length=250, null=True)


    def __str__(self):
        return self.album_title + ' - ' + self.artist

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CHAT = 'CH'
    STUDY = 'ST'
    MUSIC = 'MU'
    BUISNESS = 'BU'
    topic = models.CharField(max_length=200, null = True)
    CHEKCK = [
        (CHAT, 'Chat'),
        (STUDY, 'Study'),
        (MUSIC, 'Music'),
        (BUISNESS, 'dealing?')
    ]
    type = models.CharField(
        max_length=2,
        choices=CHEKCK,
        default=CHAT,
    )
    Muisc = models.ManyToManyField(Album,blank=True, null= True)

    
    
    
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(
        User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.topic


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    message = models.ManyToManyField(

        User, related_name='messages',
        symmetrical=False,
        blank=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    commemnt = models.CharField(max_length=200, blank= True)


class Following(models.Model):
    following = models.ManyToManyField(

        User, related_name='followed_by',
        symmetrical=False,
         blank=True)





# need to add titles for users selected by the admins



