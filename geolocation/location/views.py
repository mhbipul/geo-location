from django.shortcuts import render
import requests
import json

# Create your views here.
def index(request):
    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)
    res = requests.get('http://ip-api.com/json/'+ip_data["ip"])
    location_data_1 = res.text
    location_data = json.loads(location_data_1)
    return render(request, 'index.html',{'data': location_data})
