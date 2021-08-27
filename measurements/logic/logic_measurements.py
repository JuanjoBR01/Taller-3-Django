from ..models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement_id(id):
    measure = Measurement.objects.filter(pk = id)
    return measure

def edit_measurement(id):
    newMeasure = Measurement.objects.filter(pk = id).update(place = 'Ay mi madre, el bicho al United')
    return newMeasure

def delete_measurement(id):
    Measurement.objects.filter(pk=id).delete()
    