import json, traceback, re, random
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.contrib import messages
from django.template import RequestContext
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render, redirect, render_to_response
from company.models import *


# Create your views here.
def index(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        context = locals()
        templates = 'index.html'
        return render(request, templates, context)
    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('message')

        con = Message()
        con.name = name
        con.email = email

        n.message = msg
        context = {
            'success': "You Request has been Submitted Successfully,We will get back to you soon!!!",
        }
        templates = 'index.html'
        return render(request, templates, context)


def contact(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        context = locals()
        templates = 'ContactUs.html'
        return render(request, templates, context)
    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('message')

        con = Message()
        con.name = name
        con.email = email
        con.message = msg
        context = {
            'success': "You Request has been Submitted Successfully,We will get back to you soon!!!",
        }
        templates = 'ContactUs.html'
        return render(request, templates, context)


def market(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        context = locals()
        templates = 'Market.html'
        return render(request, templates, context)


def services(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        context = locals()
        templates = 'Services.html'
        return render(request, templates, context)


def about(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        context = locals()
        templates = 'AboutUs.html'
        return render(request, templates, context)
