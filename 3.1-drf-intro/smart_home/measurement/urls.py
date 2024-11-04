from django.urls import path
from .views import SensorListCreateView, SensorRetrieveUpdateDeleteView, MeasurementCreateView

urlpatterns = [
    # path('sensors/', SensorListCreateView.as_view(), name='sensor-list-create'),
    # path('sensors/<int:pk>/', SensorRetrieveUpdateView.as_view(), name='sensor-retrieve-update'),
    path('sensors/', SensorListCreateView.as_view(), name='sensor-list-create'),    # Для списка и создания датчиков
    path('sensors/<int:pk>/', SensorRetrieveUpdateDeleteView.as_view(), name='sensor-detail'), # Для работы с конкретным датчиком
    path('measurements/', MeasurementCreateView.as_view(), name='measurement-create'),
]
