# test_client.py

import requests

BASE_URL = 'http://localhost:5000/data'

def send_data(client_id, asset_name, quantity, data=None):
    payload = {
        'client_id': client_id,
        'asset_name': asset_name,
        'quantity': quantity,
        'data': data
    }
    response = requests.post(BASE_URL, json=payload)
    return response.json()

def get_data():
    response = requests.get(BASE_URL)
    return response.json()

# Beispielhafte Nutzung
if __name__ == '__main__':
    print("Sende Daten an den Server...")
    send_data('client1', 'RohstoffA1', 50, {'location': 'Lager A', 'quality': 'High'})
    send_data('client2', 'RohstoffB2', 75, {'location': 'Lager B', 'quality': 'Medium'})
    
    print("Abrufen der Daten vom Server...")
    data = get_data()
    print(data)

    # Fehlerbehandlung hinzufügen
    try:
        print("Abrufen der Daten vom Server...")
        data = get_data()
        print(data)
    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Abrufen der Daten: {e}")
    except ValueError as e:
        print(f"Fehler beim Dekodieren der JSON-Antwort: {e}")