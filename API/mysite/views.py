from django.shortcuts import render
import requests
import json

def home(request):
    url = "https://api.covid19api.com/summary"
    # A summary of new and total cases per country updated daily.
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)
    # print(response.text.encode('utf8'))
    data = response.json()
    case = []
    result = {}
    result['newconfirmed'] = data['Global']['NewConfirmed']
    result['totalconfirmed'] = data['Global']['TotalConfirmed']
    result['newdeaths'] = data['Global']['NewDeaths']
    result['totaldeaths'] = data['Global']['TotalDeaths']
    result['newrecovered'] = data['Global']['NewRecovered']
    result['totalrecovered'] = data['Global']['TotalRecovered']
    case.append(result)
   

    datanegara = data['Countries']
    # print(datanegara)
    # print(len(datanegara))
    rus=datanegara[140]
    # print(rus)
    # print(type(rus))
    case2 = []
    result2 = {}
    result2['Country'] = rus['Country']
    result2['CountryCode'] = rus['CountryCode']
    result2['NewConfirmed'] = rus['NewConfirmed']
    result2['TotalConfirmed'] = rus['TotalConfirmed']
    result2['NewDeaths'] = rus['NewDeaths']
    result2['TotalDeaths'] = rus['TotalDeaths']
    result2['NewRecovered'] = rus['NewRecovered']
    result2['NewTotalRecoveredConfirmed'] = rus['TotalRecovered']
    result2['Date'] = rus['Date']
    case2.append(result2)


    response2= requests.get("https://api.apify.com/v2/key-value-stores/1brJ0NLbQaJKPTWMO/records/LATEST?disableRedirect=true")

    datarusia= response2.json()
    infectedByRegion=(datarusia['infectedByRegion'])
    tomsk = (infectedByRegion[32])
    case3 = []
    result3 = {}
    result3['region'] = tomsk['region']
    result3['isoCode'] = tomsk['isoCode']
    result3['infected'] = tomsk['infected']
    result3['recovered'] = tomsk['recovered']
    result3['deceased'] = tomsk['deceased']
    case3.append(result3)
    # print(case3)

    # print(infectedByRegion)
    case4 = []
    for reg in infectedByRegion:
        result_reg = {}
        result_reg['region'] = reg['region']
        result_reg['isoCode'] = reg['isoCode']
        result_reg['infected'] = reg['infected']
        result_reg['recovered'] = reg['recovered'] 
        result_reg['deceased'] = reg['deceased']
        case4.append(result_reg)
    print(type(case4))

   
    context= {
        'Title' : 'Home',
        'case' : case,
        'case2' : case2,
        'case3':case3,
        'case4' : case4,
    }
    return render (request, 'index.html', context)


'''
Tomsk
Использовать сервис: Google Yandex
Вы искали: томск
Координаты:
56.484640°, 84.947649° Перевести в другие системы координат
N56.484640°, E84.947649°
56°29.08'N, 84°56.86'E
56°29'4.7040"N, 84°56'51.5364"E
Широта: 56.484640 N, Долгота: 84.947649 E (G) (O) (Я)
Высота над уровнем моря: 0.0 м.


Country:	Russia
Oblast:	Tomsk
Lat/Long:	56°29'N / 84°57'E
Elevation:	79m
Currency:	Russian Ruble (RUB)
Languages:	Russian
'''
