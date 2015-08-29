from django.shortcuts import render, render_to_response
import json
from django.http import HttpResponse
# Create your views here.

def home(request):
	k = {'status': 'hardik chu h'}
        #return HttpResponse(json.dumps(k))
	return render_to_response('home.html')
