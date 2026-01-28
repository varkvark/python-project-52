# trigger_error.py
from django.http import HttpResponse

def trigger_error(request):
    raise Exception("A test error to check the Rollbar! If you see this, all works!")
