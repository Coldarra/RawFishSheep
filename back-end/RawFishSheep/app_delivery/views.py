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
@corier
def undistribution(request):
    interface_id = "6010"

    try:
        resp = {
            "order": Order.objects.filter(status="1", isdelete="0")
        }
        return pack(interface_id, "0", "成功", resp)
    except:
        return pack(interface_id, "60102", "查询无果")

@post
@corier
def distribution(request):
    interface_id = "6011"
    user_id = request.p
    try: