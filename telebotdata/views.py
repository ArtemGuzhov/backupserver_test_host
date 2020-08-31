from django.shortcuts import render
from .models import Telebotdata
from django.http import HttpResponse
from django.db import models
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.http import HttpResponseNotFound



url = 'https://api.telegram.org/bot1153858227:AAFscj1frq1msM384J1ltxj8F1djMN9WGdg/sendMessage'
# Create your views here.
@csrf_exempt
def chat_id(request):
    if request.method == 'POST':
        whitelist = request.POST['whitelist']
        payload = request.POST['payload']
        list_of_chat_id = Telebotdata.objects.all()
        
        for index in list_of_chat_id:
            requests.post(url,
                params={'chat_id': index.chat_id, 'text': payload}
            )
            print(index.chat_id)
        return HttpResponse("Запрос пришел!")
    else:
        raise Http404("Not allowed method")
        return HttpResponseNotFound('<h1>Page not found</h1>')

    if request.method == 'GET':
        print(request)      

