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
