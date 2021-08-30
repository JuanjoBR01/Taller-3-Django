from ..models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement_id(pk):
    measure = Measurement.objects.get(id = pk)
    return measure

def edit_measurement(pk):
    measure = Measurement.objects.get(id = pk)
    measure.place = "Lio the GOAT"
    measure.save()
    return measure

def delete_measurement(pk):
    Measurement.objects.filter(id=pk).delete()
    