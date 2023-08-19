"""
URL configuration for bike_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rent.views import RentalAPIView, CustomerAPIView, VehicleAPIView, RentalStationAPIView, RentalStationDetailAPIView, VehicleDistributeAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/rent/rentals/', RentalAPIView.as_view(), name='all_rentals'),
    path('api/rent/rentals/<int:pk>/', RentalAPIView.as_view(), name='id_rental'),
    path('api/rent/customers/', CustomerAPIView.as_view(), name='all_customers'),  
    path('api/rent/customers/add/', CustomerAPIView.as_view(), name='add_customer'), 
    path('api/rent/vehicles/<int:pk>/', VehicleAPIView.as_view(), name='id_vehicle'),
    path('api/rent/vehicles/', VehicleAPIView.as_view(), name='all_vehicles'),  
    path('api/rent/vehicles/add/', VehicleAPIView.as_view(), name='add_vehicles'), 
    path('api/rent/station/', RentalStationAPIView.as_view(), name='all_stations'),  
    path('api/rent/station/add/', RentalStationAPIView.as_view(), name='add_station'), 
    path('api/rent/station/<int:station_id>/', RentalStationDetailAPIView.as_view(), name='id_station'),
    path('api/rent/station/distribution/', VehicleDistributeAPIView, name='vehicle_distribution'), 
    path('api/rent/station/distribute/', VehicleDistributeAPIView.as_view(), name='distribute_vehicles'),
   
]
