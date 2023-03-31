from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Room, User, Message, Post, Album, Following
from .form import RoomForm, UserForm, MyUserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.





def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''



    if request.user.is_authenticated:
        post = Post.objects.all()
        room = Room.objects.all()
        room_count = room.count()
        room_messages = Message.objects.all()
        context = {'room':room, 'post':post, 'room_count': room_count, 'room_messages': room_messages}
    else:
        return render(request, 'base/not_logged_in.html')



    return render(request, 'base/home.html',  context)



def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/login_register.html', {'form': form})


def userProfile(request, pk):
    user = User.objects.get(id=pk)

    

    follows = Following.objects.get
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    
    context = {'user': user, 'rooms': rooms, 
               'room_messages': room_messages, 'follows':follows }
    return render(request, 'base/profile.html', context  )


@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
       

        Room.objects.create(
            host=request.user,
            
            topic=request.POST.get('topic'),
            description=request.POST.get('description'),
        )
        return redirect('home')

    context = {'form': form,}
    return render(request, 'base/room_form.html', context)
