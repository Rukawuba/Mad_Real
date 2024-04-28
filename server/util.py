
import json
import pickle
import sklearn
import numpy as np


___locations = None
__data_columns = None
__model = None



def get_estimated_price(location, sqm, baths, rooms):
    try: 
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1  

    x = np.zeros(len(__data_columns))
    x[0] = sqm
    x[1] = baths
    x[2] = rooms
    if loc_index >= 0:
        x[loc_index] = 1 
    
    return round(__model.predict([x])[0],2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations 


    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model

    with open("./artifacts/Madrid_home_prices.pickle",'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts... done")



if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('Goya',270,2,2))
    print(get_estimated_price('Ibiza',100,3,3))
