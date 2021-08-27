from django.http import HttpResponse

def home(request):
    return HttpResponse("Ay mi madre el bicho")