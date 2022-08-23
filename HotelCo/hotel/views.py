from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
from django import forms
from django.contrib.auth.decorators import login_required
import datetime
from django.core.paginator import Paginator


def index(request):
    return render(request, "hotel/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "hotel/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "hotel/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "hotel/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "hotel/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "hotel/register.html")


def option(request):
    if request.method == "POST":
        choice = Choice()
        myhotels = MyHotels.objects.all()
        choice.city = request.POST.get('city')
        choice.duration = request.POST.get('duration')
        choice.checkin = request.POST.get('checkin')
        choice.checkout = request.POST.get('checkout')
        choice.save()

        return render(request, "hotel/option.html", {
            "choice": choice,
            "myhotels": myhotels
        })
    return render(request, "hotel/index.html")


@login_required()
def focus(request, id):
    ask = Choice.objects.all().last().duration
    focused_product = MyHotels.objects.get(id=id)
    price=focused_product.price
    total = price*ask
    booking = Booking()
    booking.hotelname = focused_product.hotelname
    booking.type = focused_product.type
    booking.duration = ask
    booking.price = total
    booking.save()
    return render(request, "hotel/focus.html", {
        "focused_product": focused_product,
        "total": total,
    })


@login_required()
def booking(request):
    bookings = Booking.objects.all()
    return render(request, "hotel/booking.html", {
        "bookings": bookings
    })