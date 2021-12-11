from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import json
from rest_framework.authtoken.models import Token
from django.http import HttpResponse, JsonResponse
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, GenericAPIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.conf import settings
from django.contrib.auth.models import User
# Create your views here.

class HotelListView(ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

def create_hotel(request):
    if request.method=="POST":
        try:
            user = Token.objects.get(key=request.headers['Authorization']).user
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            hotel=Hotel()
            hotel.name=body['name']
            hotel.location=body['location']
            hotel.rating=body['rating']
            hotel.owner=body['owner']
            hotel.image1=body['image1']
            hotel.image2=body['image2']
            hotel.image3=body['image3']
            hotel.save()
            data = {
                    'message': 'Hotel successfully created!',
                    
                }
            dump = json.dumps(data)
            return HttpResponse(dump, content_type='application/json')
        except Token.DoesNotExist:
            data = {
                'message': 'You are not authorized to create an hotel!',
                
            }
            dump = json.dumps(data)
            return HttpResponse(dump, content_type='application/json')

def delete(request,hotelID):
    
    try:
        user = Token.objects.get(key=request.headers['Authorization']).user
        hotel=Hotel.objects.filter(id=hotelID).exists()
        if hotel:
            my_hotel=Hotel.objects.get(id=hotelID)
            my_hotel.delete()
            data = {
                'message': 'Hotel deleted successfully!!',
                
            }
            dump = json.dumps(data)
            return HttpResponse(dump, content_type='application/json')
        else:
            data = {
                'message': 'There is no hotel with that id!!',
                
            }
            dump = json.dumps(data)
            return HttpResponse(dump, content_type='application/json')
    except Token.DoesNotExist:
        data = {
            'message': 'You are not authorized to delete!',
            
        }
        dump = json.dumps(data)
        return HttpResponse(dump, content_type='application/json')

class  HotelUpdateView(UpdateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    lookup_field = 'id'

def hotels_by_district(request,district):
    hotels = Hotel.objects.filter(location__icontains=district)
    my_hotels=[]
    for hotel in hotels:
        data = {
            'name': hotel.name,
            'owner': hotel.owner,
            'rating': hotel.rating,
            'location': hotel.location,
            'image1': hotel.image1,
            'image2': hotel.image2,
            'image3': hotel.image3,
        }
        my_hotels.append(data)
    dump = json.dumps(my_hotels)
    return HttpResponse(dump, content_type='application/json')

    

def hotels_by_owner(request,owner):
    hotels = Hotel.objects.filter(owner__icontains=owner)
    my_hotels=[]
    for hotel in hotels:
        data = {
            'name': hotel.name,
            'owner': hotel.owner,
            'rating': hotel.rating,
            'location': hotel.location,
            'image1': hotel.image1,
            'image2': hotel.image2,
            'image3': hotel.image3,
        }
        my_hotels.append(data)
    dump = json.dumps(my_hotels)
    return HttpResponse(dump, content_type='application/json')