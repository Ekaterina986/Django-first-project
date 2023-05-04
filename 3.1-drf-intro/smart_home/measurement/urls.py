from django.urls import path
from .views import MeasurementView, SensorView, MeasurementExView

urlpatterns = [
    path ('Measurement/', MeasurementView.as_view()),
    path ('MeasurementEx/<pk>/', MeasurementExView.as_view()),


    path ('Sensor/', SensorView.as_view()),

]
