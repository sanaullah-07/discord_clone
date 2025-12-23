from django.shortcuts import render

# Create your views here.


rooms = [
    {'id': 1, 'name': 'Python Basics'},
    {'id': 2, 'name': 'JAVA Basics'},
    {'id': 3, 'name': 'C++ Basics'}
]

def home(request):

     

    return render(request, 'base/home.html', {'rooms' : rooms})

def room(request, pk):

    room_details = None

    for i in rooms:

        if i['id'] == int(pk):

            room_details = i

    context = {'room' : room_details}

    return render(request, 'base/room.html', context)