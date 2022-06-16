from django.shortcuts import render, redirect
from chat.models import Room, Message, User
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
import random


# auto suggest username:
def suggestUsername(username):   
    if(len(username) < 3):
        alpha = "abcdefghijklmnopqrstuvwxyz"
        ALPHA = alpha.upper()
        alpha = list(alpha)
        ALPHA = list(ALPHA)
        
        username += random.choice(ALPHA)
        for i in range(0, 3):
            username += random.choice(alpha) 
    
    # check for first username:
    totalDigits = sum(c.isdigit() for c in username)

    # username/password validation:
    if totalDigits < 3:
        # 1. Atleast three digits : The 3 digits chosen ( will be added after lowecase letters)
        digits_chosen = random.choices("0123456789",k=3) 
            
        # 2. Include the 1 sp char and then three digits
        username += digits_chosen[0] + digits_chosen[1] + digits_chosen[2]
             
    while User.objects.filter(username=username).exists():
        # 1. Atleast three digits : The 3 digits chosen ( will be added after lowecase letters)
        digits_chosen = random.choices("0123456789",k=3) 
            
        # 2. Include three digits
        username += digits_chosen[0] + digits_chosen[1] + digits_chosen[2]
    
    print("The Final Username Generated is: ", username)
    return username


# validates username and password:
def validateDetails(username, password):
    # sp = ['.','-', '_']
    # specialChar = sum(c in sp for c in username)
    totalDigits = sum(c.isdigit() for c in username)

    # username/password validation:
    # if specialChar < 1 or totalDigits < 3 or len(password) < 3:
    #     return False
    if totalDigits < 3 or len(username) < 3 or len(password) < 3:
        return False
    else: 
        return True
    

# Create your views here.
def home(request):
    return render(request, 'home.html')


# sends messages to room
def room(request, room):
    # ajax request, not POST:
    username = request.GET.get('username')
    # room_details = Room.objects.get(name=room)     #fetch messages
    
    return render(request, 'room.html', {
        'username' : username,
        'room' : room,
        # 'room_details' : room_details
    })


# gets entry details:
def entry(request):
    # find user -> if found -> check pass and enter
    # if not found -> validate -> save -> enter

    username = request.POST['username']
    password = request.POST['password']
    room_name = request.POST['room_name']
    
    context = {
        'username' : username,
        'password': password,
        'room_name' : room_name,
    }
    
    if room_name == "":
        messages.success(request, "Room name can't be empty.")
        return render(request, 'home.html', context)
    
    # check if user already exists or not:
    print("USER CHECK.................")
    if User.objects.filter(username=username).exists():
        existingUserDetails = User.objects.get(username=username)
        if existingUserDetails.password != password:
            print("PASSWORD DOESNT MATCHED!!!!!")
            messages.success(request, "Incorrect Password. Username Suggestions: " + suggestUsername(""))
            return render(request, 'home.html', context)
    
    else:
        if(validateDetails(username, password)):
            print("NEW USER........................")
            newUser = User.objects.create(username=username, password=password)
            newUser.save()
            
            # greet message:
            new_message = Message.objects.create(value="Hey Guys 👋.", user=username, room=room_name)
            new_message.save()
            
        else:
            print("not valid........................")
            messages.success(request, "Invalid username or password. Username Suggestions: " + suggestUsername(username))
            # messages.success(request, f"{userNameError}")
            
            # context = {
            #     'userNameError': userNameError,
            #     'password': password,
            #     'room_name' : room_name,
            # }
            return render(request, 'home.html', context)
            

    # make user enter to room:
    print("ENTERING IN A ROOM")
    if Room.objects.filter(name=room_name).exists():
        context = {
            'room': room_name,
            'username' : username,
        }
        return render(request, 'room.html', context)
        # return redirect('/' + room_name + '/?username=' + username)
    else:
        new_room = Room.objects.create(name=room_name)
        new_room.save()
        context = {
            'room': room_name,
            'username' : username,
        }
        
        # greet message:
        new_message = Message.objects.create(value="Welcome User 👋.", user="iConnect Team", room=room_name)
        new_message.save()
        
        return render(request, 'room.html', context)
    

# takes data from form and saves to DB as a message entity:
def send(request):
    room = request.POST['room']
    username = request.POST['username']
    message = request.POST['message']
    
    new_message = Message.objects.create(value=message, user=username, room=room)
    new_message.save()
    
    return HttpResponse('Message Sent succesfully!!')
    

# sends userlist to ajax:
def getUserList(request, room):
    # cant use get() here coz it returns dict of all
    messages = Message.objects.filter(room=room)
    s = []
    for i in messages:
        s.append(i.user)
    
    x = set(s)
    x = list(x)
    
    print("Printing------ ", x)
    return JsonResponse({
        "messages" : x
    })


# send messages to ajax in the form of JSON in realtime from DB:
def getMessages(request, room):
    # room = Room.objects.get(name=room)
    
    # return list of values of message in json format:
    messages = Message.objects.filter(room=room)
    # print(messages)
    return JsonResponse({
        "messages" : list(messages.values())
    })