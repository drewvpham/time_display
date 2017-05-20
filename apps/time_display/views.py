from django.shortcuts import render, HttpResponse
from datetime import datetime
import time

# Create your views here.
# datetime.now()
def index(request):
    context = {
        "somekey": datetime.now().strftime("%b %d, %Y %I:%M:%S %p"),
    }

    return render(request, 'time_display/index.html', context)
