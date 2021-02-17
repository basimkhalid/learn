from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path('addpage', views.addpage, name="addpage"),
    path('pages/<str:title>', views.showpage, name="showpage")
]
