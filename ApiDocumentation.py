# importing requests
import requests  

# link
url = 'http://api.citybik.es/v2/networks' 
# capitalize - firs letter upercase
user = input('City:  ').capitalize()
# requesting site
response = requests.get(url)

# reading json content
json_content = response.json()
networks = json_content['networks']

# taking information i want, which is in dict
for item in networks:
  if user == item['location']['city']:    
    company = item['company'][0]
    city = item['location']['city']
    country_index = item['location']['country']
    latitude = item['location']['latitude']
    longitude = item['location']['longitude']

class Info:

  def __init__(self, company, city, country_index, latitude, longitude):
    self.company = company
    self.city = city
    self.country_index = country_index
    self.latitude = latitude
    self.longitude = longitude
    
  def setter(self):
    print(f'Company: {self.company}\nCity: {self.city}\nCountry index:  {self.country_index}\nLatitude:  {self.latitude}\nLongitude:  {self.longitude}')

# saving information in object    
s = Info(company, city, country_index, latitude, longitude)  
s.setter()
