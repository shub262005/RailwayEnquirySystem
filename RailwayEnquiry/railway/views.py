from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *


# Create your views here.
def home(request):
    return render(request, "railway/home.html")


def add_train(request):
    if request.method == "POST":
        train_number = request.POST.get("train_number")
        departure_station = request.POST.get("departure_station")
        arrival_station = request.POST.get("arrival_station")
        departure_time = request.POST.get("departure_time")
        arrival_time = request.POST.get("arrival_time")

        train = Train(
            train_number=train_number,
            departure_station=departure_station,
            arrival_station=arrival_station,
            departure_time=departure_time,
            arrival_time=arrival_time,
        )
        train.save()

        return redirect("trainlist")

    return render(request, "railway/add_train.html")


def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, "railway/ticket_list.html", {"tickets": tickets})


def train_list(request):
    trains = Train.objects.all()
    return render(request, "railway/train_list.html", {"trains": trains})


def add_ticket(request):
    if request.method == "POST":
        train_number_id = request.POST.get("train_number")
        passenger_name = request.POST.get("passenger")
        ticket_number = request.POST.get("ticket_number")
        seat_number = request.POST.get("seat_number")

        passenger = Passenger.objects.get(name=passenger_name)
        train = Train.objects.get(train_number=train_number_id)
        
        ticket = Ticket(
            train=train,
            passenger=passenger,
            ticket_number=ticket_number,
            seat_number=seat_number,
        )
        ticket.save()

        return redirect("home")

    else:
        trains = Train.objects.all()
        passengers = Passenger.objects.all()
        context = {"trains": trains, "passengers": passengers}
        return render(request, "railway/add_ticket.html", context)


def add_passenger(request):
    if request.method == "POST":
        name = request.POST.get("passenger")
        age = request.POST.get("age")
        email = request.POST.get("email")

        passenger1 = Passenger(name=name, age=age, email=email)
        passenger1.save()

        return redirect("home")
    else:
        return render(request, "railway/add_passenger.html")


def login1(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return redirect("login")
    else:
        return render(request, "railway/login.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.create_user(username=username, password=password)
        return redirect("home")
    else:
        return render(request, "railway/register.html")


def logout1(request):
    logout(request)
    return redirect("login")


def delete_ticket(request, id):
    
    Ticket.objects.get(id=id).delete()
    return redirect("ticketlist")
