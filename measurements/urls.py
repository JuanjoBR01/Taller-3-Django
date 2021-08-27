from measurements.logic.logic_measurements import delete_measurement
from django.urls import path
from . import views
urlpatterns = [ 
    path('list/',views.get_measurements, name='measurementsList'),
    path('byId/', views.get_measurement_by_id, name = 'measurementById'),
    path('editById/', views.edit_measurement_id, name = 'editMeasurement'),
    path('deleteById/', views.delete_measurement_id, name = 'deleteMeasurement')
]