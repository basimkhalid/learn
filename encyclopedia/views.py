from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

class NewEntryForm(forms.Form):
    entrytitle = forms.CharField(label="Title")
    entrycontent = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}), label="Content")

def addpage(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["entrytitle"]
            content = form.cleaned_data["entrycontent"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("encyclopedia:index"))
        else:
            return render(request, "encyclopedia/addpage.html", {
                "form":form
            })
    return render(request, "encyclopedia/addpage.html", {
        "form":NewEntryForm()
    })

