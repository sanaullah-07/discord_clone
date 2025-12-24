from django.shortcuts import render
from .models import Room
# Create your views here.


# rooms = [
#     {'id': 1, 'name': 'Python Basics'},
#     {'id': 2, 'name': 'JAVA Basics'},
#     {'id': 3, 'name': 'C++ Basics'}
# ]

def home(request):

    rooms =  Room.objects.all()    

    return render(request, 'base/home.html', {'rooms' : rooms})

def room(request, pk):

    # room_details = None

    # for i in rooms:

    #     if i['id'] == int(pk):

    #         room_details = i

    room_details = Room.objects.get(id=pk)

    context = {'room' : room_details}

    return render(request, 'base/room.html', context)