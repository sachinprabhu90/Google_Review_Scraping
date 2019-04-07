import pandas as pd
import googlemaps
import pprint
from api_key import my_api_key

#declaring client using API_KEY
API_KEY=my_api_key()
gmaps=googlemaps.Client(API_KEY)

places_result = gmaps.places_nearby(location='12.9716,77.5946',radius='50000',type='store')

#pprint.pprint(places_result)

store_name=[]
store_viscinity = []
customer_name=[]
customer_rating=[]
reviews=[]

for place in places_result['results']:
    my_place_id=place['place_id']
    my_fields=['name','type','vicinity','review']
    place_details=gmaps.place(place_id=my_place_id,fields=my_fields)
    #print(place_details['result'].keys())
    try:
        for review in place_details['result']['reviews']:
            #if place['name']=='Trends' or place['name']=='Reliance Trends':
                store_name.append(place['name'])
                store_viscinity.append(place['vicinity'])
                customer_name.append(review['author_name'])
                customer_rating.append(review['rating'])
                reviews.append(review['text'])
    except KeyError:
            pass
df_out=pd.DataFrame()
df_out['store_name']=store_name
df_out['store_addr']=store_viscinity
df_out['customer_name']=customer_name
df_out['customer_rating']=customer_rating
df_out['reviews']=reviews

print('Trends' in store_name)

df_out.to_csv('scraped.csv')
