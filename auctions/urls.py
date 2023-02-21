from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_listing", views.new_listing, name="new_listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("categories", views.categories, name="categories"),
    path("categories/<str:id>", views.category_list, name="category_list"),
    path("items/<str:id>", views.list_item, name="list_item"),
    path("items/<str:id>/edit", views.edit_item, name="edit_item"),
    path("items/<str:id>/delete", views.delete_item, name="delete_item"),
    path("items/<str:id>/bid", views.bid, name="bid"),
    path("items/<str:id>/comment", views.comment, name="comment"),
    path("closed", views.closed, name="closed"),
    path("bids_won", views.bids_won, name="bids_won"),
    path("closed/<str:id>", views.closed_item, name="closed_item")
]
