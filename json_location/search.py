from geopy.geocoders import Nominatim
from geographiclib.geodesic import Geodesic
import json

def get_coordenadas(path, longitude, latitude):
    
    with open(path, 'r') as file:
        data = json.load(file)
        for _ in range(len(data['location_history'])):
                longitude.append(data['location_history'][_]['coordinate']['longitude'])
                latitude.append(data['location_history'][_]['coordinate']['latitude'])
    
    return latitude, longitude

def get_timestamp(path, timestamp):
    
    with open(path, 'r') as file:
        data = json.load(file)
        for _ in range(len(data['location_history'])):
                timestamp.append(data['location_history'][_]['creation_timestamp'])
    
    return timestamp

def get_senac_time(adress, latitude, longitude, tempo, timestamp):
        geod = Geodesic.WGS84
        #geolocator = Nominatim(user_agent="specify_your_app_name_here", timeout=None)
        for _ in range(len(latitude)):
                adress.append(geod.Inverse(-23.669857, -46.699378, latitude[_], longitude[_]))
                #rua = geolocator.reverse("{}, {}".format(str(latitude[_]), str(longitude[_])))
                #print("{}, {:.3f} m".format(rua.address, adress[_]['s12']))
                if adress[_]['s12'] < 257:
                        if _ != len(timestamp) - 1:
                                tempo += (timestamp[_] - timestamp[_ + 1])
        
        return tempo
