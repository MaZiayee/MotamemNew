from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,JsonResponse
from website.models import Customer, Service, FAQ
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import CustomerSerializer, ServiceSerializer, FAQSerializer, MessageSerializer
# Create your views here.

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def api_Customers_list(request):
    if request.method == "GET":
        Customers = Customer.objects.all()
        serializer = CustomerSerializer(Customers,many=True)
        return Response(serializer.data)
    

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def api_Services_list(request):
    if request.method == "GET":
        Services = Service.objects.all()
        serializer = ServiceSerializer(Services,many=True)
        return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def api_FAQ_list(request):
    if request.method == "GET":
        FAQs = FAQ.objects.all()
        serializer = FAQSerializer(FAQs,many=True)
        return Response(serializer.data)
    
 

class ApiMessage(APIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)