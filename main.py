import json
import requests
from cahche import cache_connection, check_cached, create_cache
from dotenv import load_dotenv
import os


load_dotenv()


API_KEY = os.getenv('WEATHER_API_KEY')

Location = 'Istanbul,Turkey'
BaseURL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'

unit = 'metric'
location ='Istanbul,Turkey'
StartDate = '2025-04-19'
EndDate = '2025-04-20'
ContentType = 'json'
Include = 'hours'

ApiQuery = BaseURL + location

if len(StartDate):
    ApiQuery += '/' + StartDate
    if len(EndDate):
        ApiQuery += '/'+EndDate

ApiQuery += '?'

if len(unit):
    ApiQuery+= '&unitGroup=' + unit

if len(ContentType):
    ApiQuery += '&contentType=' + ContentType

if len(Include):
    ApiQuery += '&include=' + Include

ApiQuery += '&key='+ API_KEY



r = cache_connection()

cached_key = f'weather_{location}_{StartDate}_{EndDate}'

weather_data = check_cached(r, cached_key)

if weather_data :
    print('loaded from cache')

else:   
    print('using api')

    response = requests.get(ApiQuery)
    if response.status_code == 200:
        print('api request succesful')
        weather_data = response.json()

        create_cache(r , cached_key , weather_data, exp_time=36000)
        print('cached the data')

    else:
        print(f'your status code is {response.status_code}')


if weather_data:
    print(json.dumps(weather_data, indent=4))


        
def crate_json_folder():

    with open('folder.json' , 'w') as f:
        json.dump(weather_data , f , indent=4)


crate_json_folder()