from django.shortcuts import render
import requests
import datetime


def tempApp(request):
    city=request.GET.get("city")
    key='ea6d4f0325737d837ab1e3ab6a014a6e'  # search on weather api login ayyi my api id copy and paste here
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}" # login to weather api and scroll down click on current and forecast weather and open it and copy the url with city name
    a = datetime.datetime.now()
    response=requests.get(url)
    resp=response.json()
    # print(resp) for getting the dbug result
    
    

    
    payload = {
        "city" : resp['name'],
        'weather':resp['weather'][0]['main'],
        "kelvin" :(int(resp['main']['temp'])),#Kelvin
        "celcius" :(int(resp['main']['temp']))-273,
        "weatherIcon" :resp["weather"][0]['icon'],
        "country" : resp["sys"]["country"],
    }
    context={
        "resp":payload
    }
    
     
    return render(request,"index.html",context)