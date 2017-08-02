from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import UserProfile, Question
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.views.generic import View
from django.views import generic
from ans.forms import TeamForm, LoginForm, QSForm
from django.db import IntegrityError
from django.contrib.auth.models import User
import json
from django.core import serializers
from django.contrib.auth.decorators import login_required



# Create your views here.

def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/main/')
	if request.POST:
		form=LoginForm(request.POST)
		if form.is_valid():	
			data=form.cleaned_data
			username = data['name']
			password = data['password']
			user = auth.authenticate(username=username, password=password)
				
			if user is not None:
				if user.is_active:
					auth.login(request,user)
					return HttpResponseRedirect('/qs/1')
				
				else:
					state = "Your account is not active, please contact the site admin."
					return render(request,'register.html', {'form':form, 'state':state })
				
			else:
				state = "Your username and/or password were incorrect."
				return render(request,'register.html', {'form':form, 'state':state})
		else:
			return render(request,'register.html', {'form':form, 'state':state})
		
	else:
		form=LoginForm(request.GET)
		return render(request,'register.html', {'form':form})


def register(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/main/')
	if request.method=='POST': 
			data=request.POST
			u=User()
			up=UserProfile()
			u.username=data['name']
			u.set_password(data['password'])
			try:
				u.save()
			except IntegrityError:
				state="Duplicacy in Username"
				return render(request,'register.html',{'state':state})
			up.name=data['name']
			up.phone=data['phone']
			up.email=data['email']
			up.user=u
			up.save()

			return HttpResponseRedirect('/login/')
	else:
		form=TeamForm(request.GET)
		return render(request,'register.html',{'form':form})

@login_required
def logoutView(request):
	auth.logout(request)
	return HttpResponseRedirect('/login/')



@login_required
def question(request,number):

	u=UserProfile.objects.get(user=request.user)
	if request.method=='POST':
		question=Question.objects.get(number=number)
		data=request.POST
		if data['answer'] == question.answer:
			u.score+=question.marks	
		u.save()
	score=u.score
	
	form=QSForm(request.GET)
	return render(request,'qs_page.html',{'form':form, 'score':score,'number': number})