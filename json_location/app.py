import sys
sys.path.insert(0, '/home/mateus/Área de Trabalho/trabalho/projeto_igor/')
from json_location.search import get_coordenadas, get_timestamp, get_senac_time
from json_location.input import input_table

def app():
    longitude = []
    latitude = []
    adress = []
    timestamp = []
    tempo = 0

    path = '/home/mateus/Área de Trabalho/trabalho/projeto_igor/json_location/location_history.json'
    latitude, longitude = get_coordenadas(path, longitude, latitude)
    timestamp = get_timestamp(path, timestamp)
    tempo = get_senac_time(adress, latitude, longitude, tempo, timestamp)
    return input_table(tempo)

print(app())
