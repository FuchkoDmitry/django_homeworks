from django.urls import path

from measurement.views import CreateSensorView, SensorView, AddMeasurement

urlpatterns = [
    path('sensors/', CreateSensorView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurements/', AddMeasurement.as_view())
]
