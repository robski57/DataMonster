import urllib.request
import simplejson as json
import csv


locu_API = '3fd7fca64cadab3a10bc1a5b31fa04f3e2a8a475'


def locu_search(query):
    api_key = locu_API
    city = query.replace(' ', '%20')  # space is identified by %20
    url = 'https://api.locu.com/v1_0/venue/search/?locality=' + city + '&api_key=' + api_key
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    #encoding = response.info().get_content_charset('UTF-8')
    data = json.loads(response)#.read().decode(encoding))

    for item in data['objects']:
        print(item['name'], item['phone'])


    locu_search('San Fransico')

    # Headers mut be identical to the headers pull from API
    '''headers = ['name', 'locality', 'street_address', 'cuisines', 'region',
               'long', 'phone', 'postal_code', 'categories', 'has_menu',
               'country', 'lat', 'id', 'website_url', 'resource_uri'
               ]

    csv_file_name = 'Locu_Data_Push.csv'

    # newline avoid the extra blank row when you import the data
    with open(csv_file_name, 'w', newline='') as file:
        file_csv = csv.DictWriter(file, headers)
        file_csv.writeheader()
        file_csv.writerows(data['objects'])'''

    #locu_search('San Fransico')




