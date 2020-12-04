from django.shortcuts import render
from django.http import HttpResponse

from . import forms
from pymongo import MongoClient

# Create your views here.

cluster = MongoClient("mongodb+srv://ameya:ak123@cluster0.csmbw.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["djangoDB"]
collection = db["djangoDB"]


def index(request):
    tp = {'tempPage':"First template page from views.py"}
    return render(request,'index.html',context = tp)

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)


        if form.is_valid():
            print("Validation Success")
            collection.insert({"name":form.cleaned_data['name'],"text": form.cleaned_data['text']})
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])
            form = forms.FormName()


    return render(request,'form_page.html',{'form':form})
