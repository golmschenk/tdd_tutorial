from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse


def persona_login(request):
    authenticate(assertion=request.POST['assertion'])
    return HttpResponse()
