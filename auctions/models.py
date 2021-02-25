from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

from django.db.models.fields import DateField, DateTimeField


class User(AbstractUser):
    pass

    def __str__(self):
        return f"{self.username}"

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=4000)
    imageurl = models.URLField(max_length=400, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    listdate = DateTimeField(auto_now=True, auto_now_add=False)
    initialprice = models.DecimalField(max_digits=10, decimal_places=2, default=00.00)
    bidinprogress = models.BooleanField(default=True)
    winner = models.ForeignKey(User, default=None, blank=True, null=True, on_delete=models.CASCADE, related_name="bids_won")

    def __str__(self):
        return f"Listing: {self.title} by {self.author}"
    
class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_bids")
    bidamount = models.DecimalField(max_digits=10, decimal_places=2)
    biduser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bids")

    def __str__(self):
        return f"Bid by {self.biduser}: {self.bidamount} for {self.listing}"
    
class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_comments")
    commentuser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    comment = models.TextField(max_length=4000)
    commentdate = DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f"Comment by {self.commentuser} on {self.listing} : {self.comment}"
