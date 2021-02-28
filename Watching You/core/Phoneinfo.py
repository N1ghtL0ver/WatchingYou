import requests, json


def _GetPhoneInfo():

    """" Argument and parser """

    phone = input('[~] Enter Phone Number: ')
    try:
        data = requests.get('https://htmlweb.ru/geo/api.php?json&telcod=' + phone).json()
        print('\nPhone Information:' + '\nCountry:', data["country"]["english"]
        + '\nLocation: ' + data['country']['location']
        + '\nCity:', data['country']['english']
        + '\nLatitude', data['capital']['latitude'])
        print('Longitude', data['capital']['longitude'])
    except KeyboardInterrupt:
        print('Program Stopped!')
    except requests.exceptions.ConnectionError as e:
        print ("[~] check your internet connection!")

