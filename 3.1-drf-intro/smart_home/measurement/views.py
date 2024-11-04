from rest_framework import generics, status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer

# class SensorListCreateView(generics.ListCreateAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorSerializer
#
# class SensorRetrieveUpdateView(generics.RetrieveUpdateAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorDetailSerializer
#
class MeasurementCreateView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

# класс для получения всех датчиков и добавления датчика с кастомным ответом
class SensorListCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        sensor_name = serializer.data.get("name")
        custom_message = f"Датчик '{sensor_name}' успешно добавлен"

        return Response({"message": custom_message}, status=status.HTTP_201_CREATED)


# Класс для получения, обновления и удаления датчика
class SensorRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer