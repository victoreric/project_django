import requests

# url = "https://api.covid19api.com/live/country/russia/status/confirmed"
    # A summary of new and total cases per country updated daily.
# payload = {}
# headers= {}
# response = requests.request("GET", url, headers=headers, data = payload)
response= requests.get("https://api.apify.com/v2/key-value-stores/1brJ0NLbQaJKPTWMO/records/LATEST?disableRedirect=true")

datarusia= response.json() # data rusia/ utama
# print(type(data))# <class 'dictionary'>
# print(len(data)) #11
# print(datarusia.keys()) #dict_keys(['infected', 'tested', 'recovered', 'deceased', 'infectedByRegion', 'country', 'historyData', 'sourceUrl', 'lastUpdatedAtApify', 'lastUpdatedAtSource', 'readMe'])

infectedByRegion=(datarusia['infectedByRegion'])
# print(type(infectedByRegion)) # <class 'list'>
# print (len(infectedByRegion)) # 85
tomsk = (infectedByRegion[32]) # томская область
# print(type(tomsk)) #<class 'dict'>
# print (tomsk['region'])
# print(dir(tomsk))
# print(tomsk.items())
print ('region = ', tomsk['region'])
print ('isoCode = ', tomsk['isoCode'])
print ('infected = ', tomsk['infected'])
print ('recovered = ', tomsk['recovered'])
print ('deceased = ', tomsk['deceased'])







