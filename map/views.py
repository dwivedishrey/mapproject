from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Search
from .forms import SearchForm
import folium
import geocoder
from time import sleep
from math import sin,cos,sqrt,atan2,radians
from django.contrib import messages



# Create your views here.
def distance_km(lat1,lng1):
    R=6373.0
    """lat=radians(lat)
    lng=radians(lng)"""
    lng1=radians(lng1)
    lat1=radians(lat1)
    dlon=lng1-82.170700
    dlat=lat1-26.767396
    a=(sin(dlat/2))**2+cos(26.767396)*cos(lat1)*(sin(dlon/2))**2
    c=2*atan2(sqrt(a),sqrt(1-a))
    global distance
    distance=R*c
    return distance
def order(request):
    if distance<6:
        print('30min')
        messages.info(request,'Your order will be deliver in 30 min')
        return redirect('index.html')
    else:
        print('45min')
        messages.info(request,'Your order will be deliver in 45 min')
        return redirect('index.html')
    
   
    
    

def index(request):
    
    if request.method == 'POST':
        form = SearchForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SearchForm()
    
    """address1=Search.objects.all().last()
    location = geocoder.osm()
    lat = location.lat
    lng = location.lng
    country = location.country
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SearchForm()"""
    address2=Search.objects.all().last()
    location1= geocoder.osm(address2.destination)
    lat1 = location1.lat
    lng1 = location1.lng
    country = location1.country
    """if lat == None or lng == None:
        address1.delete()
        return HttpResponse('You address input is invalid')"""
    if lat1 == None or lng1 == None:
        address2.delete()
        return HttpResponse('You address input is invalid')

    # Create Map Object
    m = folium.Map(location=[26.75, 82.05], zoom_start=11)
    icon1=folium.Icon(icon_color='red',icon='circle')
    folium.Marker([26.767396, 82.170700], tooltip='Click for more',
                  popup=country,icon=icon1).add_to(m)
    folium.Marker([lat1, lng1], tooltip='Click for more',
                  popup=country).add_to(m)
    folium.PolyLine(([26.767396,82.170700],[lat1,lng1])).add_to(m)
    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm': m,
        'form': form,

        
    
    }
    
    distance_km(lat1,lng1)
    order(request)
    return render(request, 'index.html',context)
    

