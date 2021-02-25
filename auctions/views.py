from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.contrib.auth.decorators import login_required

from .models import User


def index(request):
    return render(request, "auctions/index.html", {
        "all_listings": Listing.objects.all().order_by('-listdate')
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("auctions:index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("auctions:index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("auctions:index"))
    else:
        return render(request, "auctions/register.html")

def listingview(request, listing_id):
    listing = Listing.objects.get(pk=listing_id)
    try:
        maxbid = listing.listing_bids.order_by('-bidamount')[0]
    except:
        maxbid = None
    try:
        comments = listing.listing_comments.all().order_by('-commentdate')
    except:
        comments = None
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "maxbid" : maxbid,
        "comments" : comments
    })

@login_required(redirect_field_name='next', login_url='/login')
def newbid(request, listing_id):
    if request.method == "POST" and request.POST["newbidamount"]:
        listing = Listing.objects.get(pk=listing_id)
        bidamount = float(request.POST["newbidamount"])
        try:
            maxbid = listing.listing_bids.order_by('-bidamount')[0]
        except:
            maxbid = Bid(listing=listing, biduser=request.user, bidamount=0)
        if bidamount > float(maxbid.bidamount):
            newbid = Bid(listing=listing, bidamount=bidamount, biduser=request.user)
            newbid.save()

            bid_msg = "Your Bid is placed" 
            return HttpResponseRedirect(reverse("auctions:listing", args=(listing_id,)))

        else:
            bid_msg = "Bid amount should be higher than the current highest amount"
            return render(request, "auctions/listing.html", {
                "listing": listing,
                "maxbid" : maxbid,
                "bid_msg" : bid_msg
            })
    return HttpResponseRedirect(reverse("auctions:listing", args=(listing_id,)))

@login_required(redirect_field_name='next', login_url='/login')
def closebid(request, listing_id):
    pass