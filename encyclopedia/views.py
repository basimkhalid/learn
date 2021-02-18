from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from markdown2 import Markdown

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
            return HttpResponseRedirect(reverse("encyclopedia:showpage", kwargs={'title': title}))
        else:
            return render(request, "encyclopedia/addpage.html", {
                "form":form
            })
    return render(request, "encyclopedia/addpage.html", {
        "form":NewEntryForm()
    })

def showpage(request, title):
    markdowner = Markdown()
    rawpagecontent = util.get_entry(title)
    if rawpagecontent is None:
        rawpagecontent = "This entry Does not exist. [Add new Entry](/addpage)"
    pagecontent = markdowner.convert(rawpagecontent)
    return render(request, "encyclopedia/showpage.html", {
        "title": title,
        "pagecontent":pagecontent
    })

def editpage(request, title):
    rawpagecontent = util.get_entry(title)
    form = NewEntryForm({
        "entrytitle": title,
        "entrycontent":rawpagecontent
    })
    return render(request, "encyclopedia/addpage.html", {
        "form":form
    })

