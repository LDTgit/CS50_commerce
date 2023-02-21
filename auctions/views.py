from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import date

from .models import User, Listing, User_Activity, Bidding, Comment, Category, Closed


def index(request):
    listings = Listing.objects.filter(active=True).all()
    return render(request, "auctions/index.html", {
        "listings": listings
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
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def categories(request):
    categories = Category.objects.all()
    return render(request, "auctions/categories.html", {
        "categories":categories
    })

def category_list(request, id):
    if id == "none":
        listings = Listing.objects.filter(category=None).all()
    else:
        category = Category.objects.get(id=id)
        listings = Listing.objects.filter(category=category).all()
    return render(request, "auctions/category_list.html", {
        "listings":listings.filter(active=True).all()
    })

@login_required
def new_listing(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "auctions/new_listing.html", {
            "categories": categories
        })
    elif request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        starting_bid = request.POST["starting_bid"]
        photo = request.POST["photo"]
        author = request.user
        post_date = date.today()
        try:
            category=None
            if "category" in request.POST:
                category_id = request.POST["category"]
                category=Category.objects.get(id=category_id)
            list_item =Listing.objects.create(title=title, description=description, starting_bid=starting_bid, photo=photo, category=category, author=author, post_date=post_date, active=True)
            list_item.save()
        except IntegrityError as ex:
            print(ex)
            return render(request, "auctions/new_listing.html", {
                "message": "Listing already exists."
            })
    return redirect("index")

@login_required
def delete_item(request, id):
    listing = Listing.objects.get(id=id)
    listing.delete()
    return redirect("index")


def list_item(request, id):
    listing = Listing.objects.get(id=id)
    bids = Bidding.objects.filter(listing_bid=id).all()
    listing_comments = Comment.objects.filter(listing_id=id).all()
    user = request.user
    if user.is_authenticated:
        watched_item = User_Activity.objects.filter(current_user=user).all()
        liked = False
        if watched_item.filter(watched_id=id).all():
            liked = True
    else:
        liked = False
    current_price = 0
    current_price_user = ""
    for bid in bids:
        if bid.bid > current_price:
            current_price = bid.bid
            current_price_user = bid.user_id
    return render(request, "auctions/list_item.html", {
        "listing": listing,
        "bids": bids,
        "current_price": current_price,
        "current_price_user": current_price_user,
        "listing_comments":listing_comments,
        "liked":liked
    })

@login_required
def edit_item(request, id):
    listing = Listing.objects.get(id=id)
    user=request.user
    author = listing.author
    post_date = listing.post_date
    categories = Category.objects.all()
    category = None
    if listing.category != None:
        category = listing.category.category_title
    if request.method == "GET":
       return render(request, "auctions/edit_item.html", {
        "listing": listing,
        "listings":Listing.objects.all(),
        "categories":categories,
        "category":category
    })
    elif request.method == "POST" and user==author:
        title = request.POST["title"]
        description = request.POST["description"]
        starting_bid = request.POST["starting_bid"]
        photo = request.POST["photo"]
        try:
            new_category=None
            if "category_id" in request.POST:
                category_id = request.POST["category_id"]
                new_category=Category.objects.get(id=category_id)
            new_list_item =Listing(id=id, title=title, description=description, starting_bid=starting_bid, photo=photo, category=new_category, author=author, post_date=post_date, active=True)
            new_list_item.save()
        except IntegrityError:
            return render(request, "auctions/new_listing.html", {
                "message": "An error occured. Please try again."
            })
    return redirect("index")

@login_required
def bid(request, id):
    listing = Listing.objects.get(id=id)
    listing_comments = Comment.objects.filter(listing_id=id).all()
    bids = Bidding.objects.filter(listing_bid=listing).all()
    author = request.user
    watched_item = User_Activity.objects.filter(current_user=author).all()
    liked = False
    if watched_item.filter(watched_id=id).all():
        liked = True
    bidding = int(request.POST["bidding"])
    biggest_bid=int(listing.starting_bid)
    biggest_bid_user = None
    for bid in bids:
        if bid.bid >= biggest_bid:
            biggest_bid=bid.bid
            biggest_bid_user=bid.user_id

    if bidding >= listing.starting_bid and bidding >= biggest_bid:
        try:
            title = listing.title
            description = listing.description
            starting_bid=listing.starting_bid
            photo = listing.photo
            category = listing.category
            listing_author = listing.author
            post_date = listing.post_date
            new_bid = Bidding(user_id=author, listing_bid=listing, bid=bidding)
            new_bid.save()
            update_listing = Listing(id=id, title=title, description=description, starting_bid=starting_bid, photo=photo, category=category, author=listing_author, post_date=post_date, current_price = bidding, active=True)
            update_listing.save()
        except IntegrityError:
            return render(request, "auctions/list_item.html", {
                "id" : id,
                "message": "An error occured. Please send your offer again."
            })
    else:
        return render(request, "auctions/list_item.html", {
                "id" : id,
                "listing":listing,
                "bids": bids,
                "current_price": biggest_bid,
                "current_price_user": biggest_bid_user,
                "listing_comments":listing_comments,
                "liked":liked,
                "message": "Yout bid must be greater than listed price."
            })
    return redirect("list_item", id=id)

@login_required
def watchlist(request):
    user = request.user
    watched_list = User_Activity.objects.all()
    w_listings = watched_list.filter(current_user = user).all()
    
    if request.method == "GET":
       return render(request, "auctions/watchlist.html", {
        "w_listings":w_listings
    })
    elif request.method == "POST":
        id = request.POST["id"]
        user = request.user
        listing = Listing.objects.get(id=id)
        if "add" in request.POST:
            try: 
                new_watched = User_Activity(current_user=user, watched = listing)
                new_watched.save()    
            except IntegrityError:
                return render(request, "auctions/watchlist.html", {
                    "message": "An error occured. Try adding this listing again."
                })
        elif "remove" in request.POST:
            try:  
                instance = User_Activity.objects.filter(current_user = user).get(watched_id=id)
                instance.delete()    
            except IntegrityError:
                return render(request, "auctions/watchlist.html", {
                    "message": "An error occured. Try deleting this listing again."
                })
    return render(request, "auctions/watchlist.html", {
                "w_listings":w_listings
            })

@login_required    
def comment(request, id):
    listing = Listing.objects.get(id=id)
    author = request.user
    try: 
        received_comment = request.POST["received_comment"]
        new_comment = Comment(user_comm=author, listing_id=listing, comment=received_comment)
        new_comment.save()
    except IntegrityError:
        return render(request, "auctions/list_item.html", {
            "id" : id,
            "message": "You have already commented on this listing."
        })
    return redirect("list_item", id=id)

@login_required
def closed(request):
    user = request.user
    listings = Closed.objects.filter(user_closed = user).all()
    return render(request, "auctions/closed_list.html", {
        "listings":listings
    })

@login_required
def bids_won(request):
    user = request.user
    listings = Closed.objects.filter(winner=user).all()
    return render(request, "auctions/closed_list.html", {
        "listings":listings
    })

@login_required
def closed_item(request, id):
    listing_closed = Listing.objects.get(id=id)
    user_closed = request.user
    bids = Bidding.objects.filter(listing_bid=listing_closed).all()
    biggest_bid=int(listing_closed.starting_bid)
    biggest_bid_user = None
    for bid in bids:
        if bid.bid >= biggest_bid:
            biggest_bid=bid.bid
            biggest_bid_user=bid.user_id
    winner = biggest_bid_user
    if request.method == "GET":
        listing_comments = Comment.objects.filter(listing_id=id).all()
        clisting = Closed.objects.get(listing_closed = listing_closed)
        return render(request, "auctions/closed_item.html", {
        "id":id,
        "listing":clisting,
        "listing_comments":listing_comments
        })
    elif request.method == "POST":
        try: 
            new_closed_listing = Closed(winner=winner, user_closed=user_closed, listing_closed=listing_closed)
            new_closed_listing.save()
            modify_listing = Listing(id=listing_closed.id, title=listing_closed.title, description=listing_closed.description, starting_bid=listing_closed.starting_bid, photo=listing_closed.photo, category=listing_closed.category, author=listing_closed.author, post_date=listing_closed.post_date, current_price = listing_closed.current_price, active=False)
            modify_listing.save()
            instance = User_Activity.objects.filter(watched=listing_closed).all()
            instance.delete()
        except IntegrityError:
            return render(request, "auctions/closed_item.html", {
                "id" : id,
                "message": "An error occured. Try again."
            })
    return redirect('closed')
