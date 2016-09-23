#utf-8
# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.
#
# def index(request):
#     return HttpResponse("Hello world")

from django.shortcuts import render, HttpResponse
from .models import User

# Create your views here.
def index(request):
   print (">>>>>>>>")

   user = ""
   p = ""

   for row in User.objects.all():
       print (row.username)
       print (row.password)
       print(row.อาจารย์อยาได้อะไรค้าบ)
       user += '<br />' + row.username+' '+' '+row.อาจารย์อยาได้อะไรค้าบ+'<br/>'
       p   += '<br />'+' '+row.password+'<br/>'
   print ("<<<<<<<<")

   return HttpResponse("Hello django : " +user+p)
   # return render(request, 'Hello django : ' + user+p )