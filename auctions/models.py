from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_title = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.category_title

    class Meta:
    # Gives the proper plural name for admin
        verbose_name_plural = "Categories"

class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=160)
    starting_bid = models.IntegerField()
    current_price = models.IntegerField( null = True, blank = True )
    photo = models.ImageField(upload_to='myphotos', null = True, blank = True)
    category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE, blank=False, null=True)
    author = models.ForeignKey(User, related_name='author',on_delete=models.CASCADE, blank = False, null = False)
    post_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return '{} posted by {}'.format(self.title, self.author)
   
   
class User_Activity(models.Model):
    id = models.AutoField(primary_key=True)
    current_user = models.ForeignKey(User, related_name='current_user',on_delete=models.CASCADE)
    watched = models.ForeignKey(Listing, blank=True, related_name="watched",on_delete=models.CASCADE)

    def __str__(self):
        return '{} added {} to the watchlist'.format(self.current_user, self.watched.title)    

    class Meta:
        verbose_name_plural = "Watched listings"

class Bidding(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, related_name='user_id',on_delete=models.CASCADE)
    listing_bid = models.ForeignKey(Listing, blank=True, related_name="listing_bid", on_delete=models.CASCADE)
    bid = models.IntegerField()

    def __str__(self):
        return 'User {} bid $ {} for {}'.format(self.user_id, self.bid, self.listing_bid.title)    


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user_comm = models.ForeignKey(User, related_name='user_comm',on_delete=models.CASCADE)
    listing_id = models.ForeignKey(Listing, blank=True, related_name="listing_id", on_delete=models.CASCADE)
    comment = models.CharField(max_length=120)
    def __str__(self):
        return 'User {} said {} regarding listing {}'.format(self.user_comm, self.comment, self.listing_id.title) 
    

class Closed(models.Model):
    id = models.AutoField(primary_key=True)
    user_closed = models.ForeignKey(User, related_name='user_closed',on_delete=models.CASCADE)
    listing_closed = models.ForeignKey(Listing, blank=True, related_name="listing_closed", on_delete=models.CASCADE)
    winner = models.ForeignKey(User, related_name='winner',on_delete=models.CASCADE)
    def __str__(self):
        return 'User {} won {} posted by {}'.format(self.winner, self.listing_closed.title, self.user_closed) 
    class Meta:
        verbose_name_plural = "Closed Listings"