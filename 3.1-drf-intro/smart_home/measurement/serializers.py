from rest_framework import serializers
from measurement.models import Sensor, Measurement


class AddMeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ('sensor_id', 'temperature', 'image')


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ('temperature', 'created_at')


class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


class SensorsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ('id', 'name', 'description')

