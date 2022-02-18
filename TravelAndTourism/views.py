from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,FileResponse

def landingpage(request):
	return HttpResponse("<center><h1>Heroku-Django Landing Page</h1></center>")