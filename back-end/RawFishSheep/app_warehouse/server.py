from decorator import *
from .views import *
from .models import *

def test(param):
  print(param)
  return{
    "ok":ok
  }

@admin
@service
def get_warehouseinfo(param):
  request = None
  interface_id = "3000"
  print("GET_WAREHOUSEINFO")
  