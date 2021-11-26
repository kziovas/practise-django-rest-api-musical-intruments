import uuid
from django.http.response import JsonResponse
from django.http.request import RAISE_ERROR, HttpRequest
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.parsers import JSONParser
from rest_framework import status
from models import Instrument
from serializers import InstrumentsSerializer
from injector import singleton, inject

@singleton
class InstrumentsService():

    def get_instrument_by_id(self,id: uuid.UUID):
        try:
            instruments = Instrument.objects.get(pk=id)
            serializer = InstrumentsSerializer(instruments)

        except Instrument.DoesNotExist as exc:
            raise NotFound(f"No items where found with the given id {id}")
        
        return serializer.data


    def update_instrument_by_id(self,id: uuid.UUID, instrument_data: dict):
        try:
            instruments = Instrument.objects.get(pk=id)
            serializer = InstrumentsSerializer(instruments, data=instrument_data)

            if serializer.is_valid():
                serializer.save()
            else:
                raise ValidationError("The data provided for updating an instrument are not valid")

        except Instrument.DoesNotExist as exc:
            raise NotFound(f"No items where found with the given id {id}")
        
        return serializer.data

    def delete_instrument_by_id(self,id: uuid.UUID):
        try:
            instruments = Instrument.objects.get(pk=id)
            serializer = InstrumentsSerializer(instruments)
            instruments.delete()

        except Instrument.DoesNotExist as exc:
            raise NotFound(f"No items where found with the given id {id}")
        
        return serializer.data


    def get_instruments_by_type(self, instrument_type: str):
        if instrument_type is not None:
            instruments = Instrument.objects.all()
            instruments.filter(instrument_type__icontains=instrument_type)
            serializer = InstrumentsSerializer(instruments, many=True)
        else:
            raise ValueError("Value type None is not acceptable for 'instrument_type'")

        return serializer.data

    def add_instrument(self, instrument_data: Instrument):
        serializer = InstrumentsSerializer(data=instrument_data)

        if serializer.is_valid():
            serializer.save()
        else:
            raise ValidationError("The data provided for registering a new instrument are not valid")