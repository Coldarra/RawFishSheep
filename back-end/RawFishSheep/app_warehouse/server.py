from decorator import *
from .views import *
from .models import *

def test(param):
  print(param)
  return{
    "ok":ok
  }

@service
def get_warehouseinfo(param):
  interface_id = "3000"
  print("GET_WAREHOUSEINFO")
  
@service
def append_warehouse(param):
  interface_id = "3001"
  print("APPEND_WAREHOUSE")

@service
def modify_warehouse(param):
  interface_id = "3002"
  print("MODIFY_WAREHOUSE")

def delete_warehouse(param):
  interface_id = "3003"
  print("DELETE_WAREHOUSE")

def get_cargoin_info(param):
  interface_id = "3010"
  print("GET_CARGOIN_INFO")

def append_cargoin(param):
  interface_id = "3011"
  print("APPEND_CARGOIN")

def delete_cargoin(param):
  interface_id = "3012"
  print("DELETE_CARGOIN")

def get_cargoout_info(param):
  interface_id = "3020"
  print("GET_CARGOIN_INFO")

def append_cargoout(param):
  interface_id = "3021"
  print("APPEND_CARGOIN")

def delete_cargoout(param):
  interface_id = "3022"
  print("DELETE_CARGOIN")

