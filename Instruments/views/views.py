from django.shortcuts import render
from django.http.response import JsonResponse, 
from django.http.request import HttpRequest
from rest_framework.parsers import JSONParser
from rest_framework import status
from Instruments.services import instruments_service
from models import Instrument
from serializers import InstrumentsSerializer
from rest_framework.decorators import api_view
from services import InstrumentsService

# Application views live here
@api_view('GET')
def get_instruments_by_type(request:HttpRequest):
    instrument_service = InstrumentsService()
    instrument_type = request.GET.get("type", None)

    data={}
    try:    
        data = instrument_service.get_instruments_by_type(instrument_type)
        return JsonResponse(data,status=status.HTTP_200_OK, safe=False)
    except Exception as exc:
        return JsonResponse({"Status":f"Error: {exc}"},status=status.HTTP_400_BAD_REQUEST , safe=False)


@api_view('GET')
def get_instrument_by_id(request:HttpRequest, id):
    instrument_service = InstrumentsService()
 
    data={}
    try:    
        data = instrument_service.get_instrument_by_id(id)
        return JsonResponse(data,status=status.HTTP_200_OK, safe=False)
    except Exception as exc:
        return JsonResponse({"Status":f"Error: {exc}"},status=status.HTTP_404_NOT_FOUND , safe=False)


@api_view('PUT')
def update_instrument_by_id(request:HttpRequest, id):
    instrument_service = InstrumentsService()
    instrument_data = JSONParser().parse(request)
    
 
    data={}
    try:    
        data = instrument_service.update_instrument_by_id(id, instrument_data)
        return JsonResponse(data,status=status.HTTP_200_OK, safe=False)
    except Exception as exc:
        return JsonResponse({"Status":f"Error: {exc}"},status=status.HTTP_404_NOT_FOUND , safe=False)


@api_view('DELETE')
def delete_instrument_by_id(request:HttpRequest, id):
    instrument_service = InstrumentsService()
 
    data={}
    try:    
        data = instrument_service.delete_instrument_by_id(id)
        return JsonResponse(data,status=status.HTTP_200_OK, safe=False)
    except Exception as exc:
        return JsonResponse({"Status":f"Error: {exc}"},status=status.HTTP_404_NOT_FOUND , safe=False)


@api_view('POST')
def post_instrument(request: HttpRequest):
    instrument_service = InstrumentsService()
    instrument_data = JSONParser().parse(request)
    

    data={}
    try:
        data = instrument_service.add_instrument(instrument_data)
        return JsonResponse(data,status=status.HTTP_201_CREATED, safe=False)
    except Exception as exc:
        return JsonResponse(data,status=status.HTTP_400_BAD_REQUEST, safe=False)
        
        