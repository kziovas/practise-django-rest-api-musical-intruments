from uuid import UUID
from django.shortcuts import render
from django.http.response import JsonResponse
from django.http.request import HttpRequest
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from Instruments.services import InstrumentsService
from rest_framework.decorators import api_view
from Instruments.services import InstrumentsService


# Application views live here
class InstrumentViewSet(viewsets.ModelViewSet):

    instrument_service = InstrumentsService()

    def list(self, request: HttpRequest):
        data = {}

        try:
            data = self.instrument_service.get_instruments()
            return JsonResponse(data, status=status.HTTP_200_OK, safe=False)
        except Exception as exc:
            return JsonResponse(
                {"Status": f"Error: {exc}"},
                status=status.HTTP_400_BAD_REQUEST,
                safe=False,
            )

    def create(self, request):
        instrument_data = JSONParser().parse(request)
        data = {}
        print(instrument_data)

        try:
            data = self.instrument_service.add_instrument(instrument_data)
            return JsonResponse(data, status=status.HTTP_201_CREATED, safe=False)
        except Exception as exc:
            return JsonResponse(data, status=status.HTTP_400_BAD_REQUEST, safe=False)

    def retrieve(self, request, pk: UUID = None):
        data = {}

        try:
            data = self.instrument_service.get_instrument_by_id(pk)
            return JsonResponse(data, status=status.HTTP_200_OK, safe=False)
        except Exception as exc:
            return JsonResponse(
                {"Status": f"Error: {exc}"},
                status=status.HTTP_404_NOT_FOUND,
                safe=False,
            )

    def update(self, request, pk: UUID = None):
        instrument_data = JSONParser().parse(request)
        data = {}

        try:
            data = self.instrument_service.update_instrument_by_id(pk, instrument_data)
            return JsonResponse(data, status=status.HTTP_200_OK, safe=False)
        except Exception as exc:
            return JsonResponse(
                {"Status": f"Error: {exc}"},
                status=status.HTTP_404_NOT_FOUND,
                safe=False,
            )

    def destroy(self, request, pk: UUID = None):
        data = {}
        try:
            data = self.instrument_service.delete_instrument_by_id(pk)
            return JsonResponse(data, status=status.HTTP_200_OK, safe=False)
        except Exception as exc:
            return JsonResponse(
                {"Status": f"Error: {exc}"},
                status=status.HTTP_404_NOT_FOUND,
                safe=False,
            )
