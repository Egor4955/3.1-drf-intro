from django.urls import path
from measurement.views import *

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorUpView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
