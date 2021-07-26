from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse

from .task import *
# Create your views here.
from django.core.mail import send_mail



def index(request):
    send_mail_task.delay()
    return HttpResponse("hello celry")