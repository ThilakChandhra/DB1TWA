from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *

def insert_topic(request):
    tn=input("Enter Name : " )
    T1=Topic.objects.get_or_create(topic_name=tn)[0]
    T1.save()
    return HttpResponse("Topic is createdn successfully!....")

def insert_webpage(request):
    tn=input("Enter TN : ")
    name=input("Enter Name : ")
    url=input("Enter URL : ")
    T2=Topic.objects.get_or_create(topic_name=tn)[0]
    T2.save()
    WO=WebPage.objects.get_or_create(topic_name=T2,name=n,url=url)
    return HttpResponse("WebPage is created successfully!....")