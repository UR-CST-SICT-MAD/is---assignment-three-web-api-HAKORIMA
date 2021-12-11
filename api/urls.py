from django.urls import path,include
from .views import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken import views
urlpatterns = [
    path('hotels',HotelListView.as_view()),
    path('hotels_by_district/<str:district>',hotels_by_district,name='hotels_by_district'),
    path('hotels_by_owner/<str:owner>',hotels_by_owner,name='hotels_by_owner'),
    path('delete_hotel/<int:hotelID>/',csrf_exempt(delete)),
    path('update_hotel/<id>/',HotelUpdateView.as_view()),
    path('create_hotel/',csrf_exempt(create_hotel)),
    path('api-token-auth/', views.obtain_auth_token)
]