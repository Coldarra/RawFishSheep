from django.shortcuts import render
from decorator import *
from django.http import HttpResponse
# Create your views here.

@get
def test(request):
    return HttpResponse('OK')
'''
@admin
@get
def get_info(request):
    interface_id = "3000"
'''