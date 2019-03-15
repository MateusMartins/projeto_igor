from search import get_coordenadas, get_timestamp
from geopy.geocoders import Nominatim
from geographiclib.geodesic import Geodesic

def app():
    #mariadb_connection = database.mariadb_connection()
    #cursor = mariadb_connection.cursor()
    geod = Geodesic.WGS84
    geolocator = Nominatim(user_agent="specify_your_app_name_here", timeout=None)
    longitude = []
    latitude = []
    adress = []
    timestamp = []
    time = 0

    path = '/home/mateus/Área de Trabalho/trabalhos/projeto_igor/json_location/location_history.json'
    latitude, longitude = get_coordenadas(path, longitude, latitude)
    timestamp = get_timestamp(path, timestamp)

    for _ in range(len(latitude)):
        adress.append(geod.Inverse(-23.669857, -46.699378, latitude[_], longitude[_]))
        rua = geolocator.reverse("{}, {}".format(str(latitude[_]), str(longitude[_])))
        #print("{}, {:.3f} m".format(rua.address, adress[_]['s12']))

        if adress[_]['s12'] < 257:
            if _ != len(timestamp) - 1:
                time += (timestamp[_] - timestamp[_ + 1])
                print(time)
        else:
            print(time)
    
            
app()
