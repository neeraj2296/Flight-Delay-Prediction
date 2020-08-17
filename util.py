import json
import numpy as np

__AIRLINE = None
__Columns = None
__DESTINATION_AIRPORT = None
__ORIGIN_AIRPORT = None


def load_saved_artifacts():
    global __AIRLINE
    global __Columns
    global __DESTINATION_AIRPORT
    global __ORIGIN_AIRPORT
    with open("./artifacts/Columns.json", "r") as f:
        __Columns = json.load(f)['data_columns']
    with open("./artifacts/AIRLINE.json", 'r+') as f:
        __AIRLINE = json.load(f)['AIRLINE']
    with open("./artifacts/ORIGIN_AIRPORT.json", "r+") as f:
        __ORIGIN_AIRPORT = json.load(f)['ORIGIN_AIRPORT']
    with open("./artifacts/DESTINATION_AIRPORT.json","r+") as f:
        __DESTINATION_AIRPORT = json.load(f)['DESTINATION_AIRPORT']

def get_columns():
    print("loaded columns")
    load_saved_artifacts()
    return __Columns


def get_Airlines():
    load_saved_artifacts()
    return __AIRLINE


def get_Origin():
    load_saved_artifacts()
    return __ORIGIN_AIRPORT


def get_Dest():
    load_saved_artifacts()
    return __DESTINATION_AIRPORT


if __name__ == '__main__':
    print("util is working!!")
    pass
