from rest_framework import serializers
from measurement.models import Sensor, Measurement


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['sensor_id', 'temperature', 'created_at', 'image']


class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    def to_representation(self, instance):
        '''
        переопределил метод, так как при GET-запросе
        датчиков в измерениях отображалось поле sensor_id
        и поле image даже если изображение не было
        загружено.
        '''
        response = super().to_representation(instance)
        for measurement in response['measurements']:
            if measurement['image'] is None:
                del measurement['image']
            del measurement['sensor_id']
        return response

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
        # fields = '__all__'
