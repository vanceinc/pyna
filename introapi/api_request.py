import requests
import time
import pprint

def get_iss_pos():
    url = "http://api.open-notify.org/iss-now.json"
    r = requests.get(url)
#print(r.text)
#print(r.status_code)

    j_data = r.json()
    print(j_data)
    ts = j_data['timestamp']
    iss_pos = j_data['iss_position']
    return {'time': ts, 'lat':iss_pos['latitude'], 'log': iss_pos['longitude']}

def main():
    positions = []
    for i in range(10):
        print(f"Data point: {i}")
        positions.append(get_iss_pos())
        time.sleep(1)
    pprint.pprint(positions)

if __name__ == "__main__":
    main()

