from django.shortcuts import render
from django.http import HttpResponse

import time
import os
from django.conf import settings
import cStringIO
import sys



import base64
import json
import requests

from base64 import b64encode
from main.models import mall , codingninja , fragmentname



def imguruploader(request):
	#try:
	print request.FILES
	a = request.FILES['file1']
	#print a.read()
	client_id = 'ad3002cdda698d8'
	encoded_string = base64.b64encode(a.read())
	#print "the base 64 string for the corresponding image is",encoded_string
	headers = {"Authorization": "Client-ID %s"%(client_id)}
	print headers

	url = "https://api.imgur.com/3/upload.json"
	#file = cStringIO.StringIO(base64.b64decode(request.FILES['file1']))
	api_key = '37ee388bf32de161bb82e3852124c0af4ae40f19'

	url = "https://api.imgur.com/3/upload.json"

	j1 = requests.post(
	    url, 
	    headers = headers,
	    data = {
	        'key': api_key, 
	        'image': encoded_string,
	        'type': 'base64',
	        'name': '1.jpg',
	        'title': 'Picture no. 1'
	    }
	)
	print j1
	fileurl=json.loads(j1.text)["data"]["link"]
	print fileurl
	q = codingninja.objects.get_or_create(pk = 1)[0]
	q.img1 = fileurl
	q.save()







		#return HttpResponse(j1.text)
	#except Exception as e:
		#print e
		#print "there was an exception"

	return HttpResponse("your file was uploaded successfully")

	



def index(request):
	return render(request,'main/upload.html')



def apidetails(request):
	
	uid = request.GET.get("identifier")
	print uid  


	p = fragmentname.objects.get_or_create(identifier = uid)[0]
	name = p.name
	print name


	if name == 'mall':
		q = mall.objects.get(name = "" )[0]
		image1  = q.img1 
		image2 = q.img2 
		image3 = q.img3 
		knowmore = q.knowmore 
		print "this worked1"
		response_obj = json.dumps({"image":{"1":image1 , "2" : image2 , "3" : image3}, "knowmore":knowmore})	

	elif name == 'codingninja':
		q = codingninja.objects.get_or_create(pk = 1)[0]
		print q
		image1  = q.img1 
		image2 = q.img2 
		image3 = q.img3 
		knowmore = q.knowmore 
		print "this worked2"
		response_obj = json.dumps({"image":{"1":image1 , "2" : image2 , "3" : image3}, "knowmore":knowmore})		

 







	

	return HttpResponse(response_obj)	