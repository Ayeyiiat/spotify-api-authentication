import spotipy, sqlalchemy
import requests
import pandas as pd
from sqlalchemy import create_engine

#Spotify authentication setup
#Get your own ID and secret after creating a spotify developer account and starting a new app

CLIENT_ID = '1f66716c00d24a4e8b6b264e4a8a7ca0'
CLIENT_SECRET ='c7fccfc423b749fc9268eb383d2c169b'

AUTH_URL = 'https://accounts.spotify.com/api/token'
auth_response = requests.post(AUTH_URL, {
  'grant_type' : 'client_credentials',
  'client_id' : CLIENT_ID,
  'client_secret' : CLIENT_SECRET,
})

auth_response_data = auth_response.json()

access_token = auth_response_data['access_token']

#Get rema's artist details
token = "Bearer {token}".format(token=access_token)

headers = {
  "Authorization" : token,
}
BASE_URL = 'https://api.spotify.com/v1/'

#returning the albums of an artist, Kidi
artist_id = '14PimM6ohO2gYftuwTam9V' #Can also pass as artist id
r = requests.get(BASE_URL + 'artists/' + artist_id + '/albums?include_groups=album&market=US', headers = headers)
value = r.json()

#Converting to a pandas dataframe
col_names = ["Artist's Name", "Album Name", "Number of tracks"]
df = pd.DataFrame(columns = col_names)

i = 0
while i < len(value['items']):
  df.loc[len(df.index)] = ['KiDi', value["items"][i]["name"], value["items"][i]["total_tracks"]]
  i += 1

#Creating an engine object
engine = create_engine('mysql://root:codio@localhost/favorite_ghanaian_artists')

#Creating and sending data to SQLtable from my dataframe
df.to_sql('favorite_ghanaian_artists', con=engine, if_exists='replace', index=False)