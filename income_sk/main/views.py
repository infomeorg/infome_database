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
from main.models import organisations , fragmentname



def imguruploader(request):
	print request.FILES
	#a = request.FILES['file1']
	#print a.read()
	client_id = 'ad3002cdda698d8'
	#encoded_string = base64.b64encode(a.read())
	#print "the base 64 string for the corresponding image is",encoded_string
	headers = {"Authorization": "Client-ID %s"%(client_id)}
	print headers
	#file = cStringIO.StringIO(base64.b64decode(request.FILES['file1']))
	api_key = '37ee388bf32de161bb82e3852124c0af4ae40f19'


	#url = "https://api.imgur.com/3/upload.json"

	name = request.POST['customer_name']
	p = fragmentname(name = name)
	q = organisations.objects.get_or_create(name = name)[0]
	p.save()
	print name



	knowmore = request.POST['knowmore']
	q.knowmore = knowmore
	print knowmore

	aboutme = request.POST['description']
	q.description = aboutme
	print aboutme


	fileurl = []
	for i in xrange(1,4):
		url = "https://api.imgur.com/3/upload.json"
		if ('file'+str(i)) in request.FILES:
			image = request.FILES.get('file'+str(i), None)
			encoded_string = base64.b64encode(image.read())

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
			img = json.loads(j1.text)["data"]["link"]
			print img
			fileurl.append(img)

			print fileurl


	q.img1 = fileurl[0]
	q.img2 = fileurl[1]
	q.img3 = fileurl[2]
	q.save()


	return HttpResponse("your file was uploaded successfully")
            







def index(request):
	return render(request,'main/upload.html')



def apidetails(request):
	
	uid = request.GET.get("identifier")
	print uid  


	p = fragmentname.objects.get_or_create(identifier = uid)[0]
	name = p.name
	print name

	q = organisations.objects.get(name = name)
	image1  = q.img1 
	image2 = q.img2 
	image3 = q.img3 
	knowmore = q.knowmore 
	description = q.description
	print "this worked1"
	response_obj = json.dumps({"images":{"img1":image1 , "img2" : image2 , "img3" : image3}, "knowmore":knowmore , "description" :description})	

	

 







	

	return HttpResponse(response_obj)	

def apiuid(request):

	uid = request.GET.get("uid")

	q = fragmentname.objects.values_list('identifier' , flat = True )

	

	for b in q :

		if b == uid :
			a = "yes"
			break;

		else:
			a = "no"	


	response_obj = json.dumps(a)
	
	return HttpResponse(response_obj)	
