from django.urls import path

from . import views

app_name = "auctions"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/<int:listing_id>", views.listingview, name="listing"),
    path("newbid/<int:listing_id>", views.newbid, name="newbid"),
    path("closebid/<int:listing_id>", views.closebid, name="closebid"),
    path("addcomment/<int:listing_id>", views.addcomment, name="addcomment"),
    path("addlisting", views.addlisting, name="addlisting")
]
