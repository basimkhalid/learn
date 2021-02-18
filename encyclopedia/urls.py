from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path('addpage', views.addpage, name="addpage"),
    path('wiki/<str:title>', views.showpage, name="showpage"),
    path('edit/<str:title>', views.editpage, name="editpage")
]
