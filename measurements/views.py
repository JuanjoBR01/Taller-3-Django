from variables.models import Variable
from django.shortcuts import render
from .logic.logic_measurements import get_all_measurements
from .logic.logic_measurements import get_measurement_id
from .logic.logic_measurements import edit_measurement
from .logic.logic_measurements import delete_measurement
from django.http import HttpResponse
from django.core import serializers

def get_measurements(request):
    measurements = get_all_measurements()
    measurements_list = serializers.serialize('json', measurements)
    return HttpResponse(measurements_list, content_type = 'application/json')

# Create your views here.
def get_measurement_by_id(request):
    measure = get_measurement_id(1)
    measure_list = serializers.serialize('json', measure)
    return HttpResponse(measure_list, content_type = 'application/json')

def edit_measurement_id(request):
    edit_measurement(1)
    measure = get_measurement_id(1)
    measure_list = serializers.serialize('json', measure)
    return HttpResponse(measure_list, content_type = 'application/json')

def delete_measurement_id(request):
    delete_measurement(4)
    measurements = get_all_measurements()
    measurements_list = serializers.serialize('json', measurements)
    return HttpResponse(measurements_list, content_type = 'application/json')



