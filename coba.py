import requests

url = "https://api.covid19api.com/live/country/russia/status/confirmed"
    # A summary of new and total cases per country updated daily.
payload = {}
headers= {}
response = requests.request("GET", url, headers=headers, data = payload)

# print(response.text.encode('utf8'))
data = response.json()
print(type(data))#list
print(len(data))#19

datarusia = data[0]
print (type(datarusia)) # dict
print (len(datarusia)) #12
# print(datarusia)
list = []       
for a in datarusia:
    hasil = {}
    hasil['1'] = datarusia['Country']
    hasil['2'] = datarusia['Lat']
    # print (ulang_negara)
    list.append(hasil)
print(list) 

# # print(listnegara)
# print(type(listnegara))
# # print(len(listnegara))


