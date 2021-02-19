from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from markdown2 import Markdown
from django.shortcuts import redirect
import random

from . import util


def index(request):
    if request.method == "POST":
        query = request.POST.get('q')
        entrylist = util.list_entries()
        ##Refresh Home if search is empty
        if not query:
            return render(request, "encyclopedia/index.html", {
                "entries": util.list_entries()
                })
        else:
            ##Check for exact match
            for entry in entrylist:
                if query.lower() == entry.lower():
                    return redirect('encyclopedia:showpage', query)
            ## for partial match
            searchresults = [s for s in map(str.lower, entrylist) if query.lower() in s]
            print(searchresults)
            return render(request, "encyclopedia/index.html", {
                "entries": searchresults
            })
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

class NewEntryForm(forms.Form):
    entrytitle = forms.CharField(label="Title")
    entrycontent = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}), label="Content")

class EditEntryForm(forms.Form):
    entrycontent = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}), label="Content")

def addpage(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["entrytitle"]
            content = form.cleaned_data["entrycontent"]
            rawpagecontent = util.get_entry(title)
            if rawpagecontent is not None:
                return render(request, "encyclopedia/pageexists.html", {
                "title":title
                })
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
    if request.method == "POST":
        form = EditEntryForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["entrycontent"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("encyclopedia:showpage", kwargs={'title': title}))
        else:
            return render(request, "encyclopedia/editpage.html", {
                "form":form,
                "title":title
            })
    else:
        rawpagecontent = util.get_entry(title)
        form = EditEntryForm({
            "entrycontent":rawpagecontent
        })
        return render(request, "encyclopedia/editpage.html", {
            "form":form,
            "title":title
        })

def randompage(request):
    entries = util.list_entries()
    title = random.choice(entries)
    markdowner = Markdown()
    rawpagecontent = util.get_entry(title)
    pagecontent = markdowner.convert(rawpagecontent)
    return render(request, "encyclopedia/showpage.html", {
        "title": title,
        "pagecontent":pagecontent
    })
