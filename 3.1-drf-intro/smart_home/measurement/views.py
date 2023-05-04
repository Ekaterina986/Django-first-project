# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Measurement, Sensor
from .serializers import MeasurementSerializer, SensorDetailSerializer

class MeasurementView(APIView):
    def get(self, request):
        measurements = Measurement.objects.all()
        ms =MeasurementSerializer(measurements, many=True)
        return Response(ms.data)

    def post(self, request):
        Response({'Content-Type': 'application/json'})

    def patch(self, request, pk):
        measurement_object = self.get_object(pk)
        serializer = MeasurementSerializer( measurement_object, data=request.data,
                                         partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(code=201, data=serializer.data)
        return JsonResponse(code=400, data="wrong parameters")


class MeasurementExView(RetrieveAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer





