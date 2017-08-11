from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import CustomUser, Question
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.views.generic import View
from django.views import generic
from ans.forms import QSForm
from django.db import IntegrityError
from django.contrib.auth.models import User
import json
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from allauth.account.signals import user_signed_up



@login_required
def question(request,number):

	u=request.user
	if request.method=='POST':
		question=Question.objects.get(number=number)
		data=request.POST
		if data['answer'] == question.answer:
			u.score+=question.marks	
		u.save()
	score=u.score
	
	form=QSForm(request.GET)
	return render(request,'qs_page.html',{'form':form, 'score':score,'number': number})
