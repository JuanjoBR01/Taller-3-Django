from measurements.logic.logic_measurements import delete_measurement
from django.urls import path
from . import views
urlpatterns = [ 
    path('list/',views.get_measurements, name='measurementsList'),
    path('byId/<int:pk>/', views.get_measurement_by_id, name='get_measurement_by_id'),
    path('editById/<int:pk>/', views.edit_measurement_id, name = 'editMeasurement'),
    path('deleteById/<int:pk>/', views.delete_measurement_id, name = 'deleteMeasurement')
    
			
]