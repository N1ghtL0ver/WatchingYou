import requests, json


def _GetIPInfo():
    """" Argument and parser """
    ip = input('[~] Enter IP-Address: ')
    try:
        data = requests.get('http://ip-api.com/json/' + ip).json()
        print(f'IP-Information\n' + '\nCountry:', data["country"]
        + '\nCountry Code:', data["countryCode"]
        + '\nRegion:', data["region"]
        + '\nRegion Name:', data["regionName"]
        + '\nCity:', data["city"]
        + '\nISP:', data["isp"]
        + '\nORG:', data["org"]
        + '\nAS:', data["as"]
        + '\nIP:', data["query"]
        + '\nZip:', data["zip"]
        + '\nLatitude:', data["lat"])
        print('Longitude', data["lon"])

    except KeyboardInterrupt:
        print('[!] Program Stopped')
    
    except requests.exceptions.ConnectionError as e:
        print ("[~] check your internet connection!")



