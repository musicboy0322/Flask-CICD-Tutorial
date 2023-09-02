import requests as re

def getWeatherData(city) :

    targetUrl = f'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-79B24CF8-E1B6-46D3-AF3D-3D8402669EB2&limit=100&locationName={city}&elementName=Wx,PoP,MinT,MaxT'

    result = re.get(targetUrl).json()

    return result
