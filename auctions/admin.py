from django.contrib import admin

from auctions.models import User, Listing, User_Activity, Bidding, Comment, Category, Closed

# Register your models here.
admin.site.register(User)
admin.site.register(Listing)
admin.site.register(User_Activity)
admin.site.register(Bidding)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Closed)