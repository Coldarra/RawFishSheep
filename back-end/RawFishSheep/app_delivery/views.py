from .models import *
from decorator import *
from django.shortcuts import render
from django.http import HttpResponse

import sys
sys.path.append('../')


@get
def test(request):
    return HttpResponse('OK')

@get
# @corier
def undistribution(request):
    interface_id = "6010"

    try:
        Delivery.objects.filter()