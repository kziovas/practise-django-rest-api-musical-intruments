import uuid
from django.http.response import JsonResponse
from django.http.request import RAISE_ERROR, HttpRequest
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.parsers import JSONParser
from rest_framework import status
from Instruments.models import Instrument
from Instruments.serializers import InstrumentsSerializer
from django.shortcuts import get_object_or_404


class InstrumentsService:
    def __init__(self):
        self.instruments = Instrument.objects.all()

    def get_instrument_by_id(self, id: uuid.UUID):
        try:
            instruments = get_object_or_404(self.instruments, pk=id)
            serializer = InstrumentsSerializer(instruments)

        except Instrument.DoesNotExist as exc:
            raise NotFound(f"No items where found with the given id {id}")

        return serializer.data

    def update_instrument_by_id(self, id: uuid.UUID, instrument_data: dict):
        try:

            instruments = get_object_or_404(self.instruments, pk=id)
            serializer = InstrumentsSerializer(instruments, data=instrument_data)

            if serializer.is_valid():
                serializer.save()

            else:
                raise ValidationError(
                    "The data provided for updating an instrument are not valid"
                )

        except Instrument.DoesNotExist as exc:
            raise NotFound(f"No items where found with the given id {id}")

        self.instruments = Instrument.objects.all()
        return serializer.data

    def delete_instrument_by_id(self, id: uuid.UUID):
        try:

            instruments = get_object_or_404(self.instruments, pk=id)
            serializer = InstrumentsSerializer(instruments)
            instruments.delete()

        except Instrument.DoesNotExist as exc:
            raise NotFound(f"No items where found with the given id {id}")

        self.instruments = Instrument.objects.all()
        return serializer.data

    def get_instruments(self):
        serializer = InstrumentsSerializer(self.instruments, many=True)

        return serializer.data

    def add_instrument(self, instrument_data: Instrument):

        serializer = InstrumentsSerializer(data=instrument_data)

        if serializer.is_valid():
            serializer.save()
        else:
            raise ValidationError(
                "The data provided for registering a new instrument are not valid"
            )

        self.instruments = Instrument.objects.all()
        return serializer.data
