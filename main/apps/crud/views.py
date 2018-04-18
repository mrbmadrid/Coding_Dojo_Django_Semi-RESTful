# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import User

# Create your views here.

def index(request):
	return render(request, "crud/users.html", {"users":User.objects.all()})

def show(request, id):
	return render(request, "crud/user.html", {"user":User.objects.get(id=id)})

def add(request):
	if request.POST:
		User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
		return redirect(index)
	else:
		return render(request, "crud/new.html")

def delete(request, id):
	User.objects.get(id=id).delete()
	return redirect(index)

def edit(request, id):
	if request.POST:
		user = User.objects.get(id=id)
		user.first_name = request.POST['first_name']
		user.last_name = request.POST['last_name']
		user.email = request.POST['email']
		user.save()
		return redirect(index)
	else:
		return render(request, "crud/edit.html", {"user":User.objects.get(id=id)})