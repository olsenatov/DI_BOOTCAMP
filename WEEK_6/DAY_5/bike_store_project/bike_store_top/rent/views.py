from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from datetime import datetime
from django.db.models.functions import TruncMonth
from .models import Rental, Customer, Vehicle, Rental_Station, VehicleAtRentalStation
from .serializers import RentalSerializer, CustomerSerializer, VehicleSerializer, RentalStationSerializer

# Create your views here. 
class RentalAPIView(APIView):
   
    def get(self, request, pk=None):
        if pk:
            rental = Rental.objects.get(pk=pk)
            serializer = RentalSerializer(rental)
            
        rentals = Rental.objects.order_by('-rental_date','return_date', ) 
        serializer = RentalSerializer(rentals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RentalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        rental = Rental.objects.get(pk=pk)
        serializer = RentalSerializer(rental, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        rental = Rental.objects.get(pk=pk)
        rental.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CustomerAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            customer = Customer.objects.get(pk=pk)
            serializer = CustomerSerializer(customer)
            
        rentals = Customer.objects.order_by('last_name') 
        serializer = CustomerSerializer(rentals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VehicleAPIView(APIView):
   def get(self, request, pk=None):
        if pk:
            vehicle = Vehicle.objects.get(pk=pk)
            serializer = VehicleSerializer(vehicle)
        else:
            vehicles = Vehicle.objects.values('vehicle_type').annotate(vehicle_count=Count('id'))
            serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data) 
    
   def put(self, request, pk):
        vehicle = Vehicle.objects.get(pk=pk)
        serializer = VehicleSerializer(vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   def delete(self, request, pk):
        vehicle = Vehicle.objects.get(pk=pk)
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
   def post(self, request):
        serializer = VehicleSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RentalStationAPIView(APIView):
   def get(self, request, pk=None):
       
        if pk:
            rent_st = Rental_Station.objects.get(pk=pk) 
            serializer = RentalStationSerializer(rent_st)
        rent_sts = Rental_Station.objects.get() 
        serializer = RentalStationSerializer(rent_sts, many=True)
        return Response(serializer.data) 
    
   def post(self, request):
        serializer = RentalStationSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class RentalStationDetailAPIView(APIView):
   def get(self, request, station_id):
            try:
                rent_st = Rental_Station.objects.get(id=station_id)
            except Rental_Station.DoesNotExist:
                return Response({"message": "Rental station not found"}, status=status.HTTP_404_NOT_FOUND)
        
            serializer = RentalStationSerializer(rent_st)
            return Response(serializer.data)
        
class VehicleDistributeAPIView(APIView):
    def get(self, request):
        rent_sts = Rental_Station.objects.all()
        distrib_stats = []

        for station in rent_sts:
            vehicles_pstation = VehicleAtRentalStation.objects.filter(rent_st=station)
            stats = {
                "station_name": station.name,
                "total_vehicles": vehicles_pstation.count(),
            }
            distrib_stats.append(stats)

        return Response(distrib_stats)
    
    def post(self, request):
        unallocated_vehicles = VehicleAtRentalStation.objects.filter(departure_date__isnull=True)
        rent_sts = Rental_Station.objects.all()
        vehicles_pstation = len(unallocated_vehicles) // len(rent_sts)
        for station in rent_sts:
            assign_vehicles = unallocated_vehicles[:vehicles_pstation]
            unallocated_vehicles = unallocated_vehicles[vehicles_pstation:]
            for vehicle in assign_vehicles:
                vehicle.rent_sts = station
                vehicle.save()
        return Response({"message": "Vehicles distributed successfully"})
    
#### daily challenge day5
class MonthlyRentalStatsAPIView(APIView):
    def get(self, request):
        rental_stats = Rental.objects.annotate(month=TruncMonth('rental_date')) \
            .values('month') \
            .annotate(rental_count=Count('id')) \
            .order_by('month')

        monthly_stats = {}
        for entry in rental_stats:
            month_year = entry['month'].strftime('%Y-%m')
            rental_count = entry['rental_count']
            monthly_stats[month_year] = rental_count

        return Response(monthly_stats)
    
class PopularRentalStationAPIView(APIView):
    def get(self, request):
        rental_station_stats = Rental_Station.objects.annotate(rental_count=Count('rentals')) \
            .values('name', 'rental_count') \
            .order_by('-rental_count')

        popular_station_stats = {}
        for entry in rental_station_stats:
            station_name = entry['name']
            rental_count = entry['rental_count']
            popular_station_stats[station_name] = rental_count

        return Response(popular_station_stats)
    
class PopularVehicleTypeAPIView(APIView):
    def get(self, request):
        vehicle_type_stats = Vehicle.objects.values('vehicle_type') \
            .annotate(rental_count=Count('rentals')) \
            .order_by('-rental_count')

        popular_vehicle_type_stats = {}
        for entry in vehicle_type_stats:
            vehicle_type = entry['vehicle_type']
            rental_count = entry['rental_count']
            popular_vehicle_type_stats[vehicle_type] = rental_count

        return Response(popular_vehicle_type_stats)