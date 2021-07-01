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

def gatherInput():
  user_input = input("Please paste the artist_id here: ")
  return user_input

#returning the albums of favorite artist
def build_url(artist_id):
  r = requests.get(BASE_URL + 'artists/' + artist_id + '/albums?include_groups=album&market=US', headers = headers)
  value = r.json()
  res = requests.get(BASE_URL + 'artists/' + artist_id, headers=headers)
  name = res.json()
  return value, name

def build_dataframe(value, name):
  #Converting to a pandas dataframe
  col_names = ["Artist's Name", "Album Name", "Number of tracks"]
  df = pd.DataFrame(columns = col_names)
  i = 0
  while i < len(value['items']):
    df.loc[len(df.index)] = [name['name'], value["items"][i]["name"], value["items"][i]["total_tracks"]]
    i += 1
  print(df)
  return df

def write_to_sql(df):
  #Creating database
  #CREATE DATABASE IF NOT EXISTS favorite_ghanaian_artists;
  engine = create_engine('mysql://root:codio@localhost/favorite_ghanaian_artists')
  #Creating and sending data to SQLtable from my dataframe
  return df.to_sql('favorite_ghanaian_artists', con=engine, if_exists='replace', index=False)
  

def main():
  print(" Welcome, you can use this program to get your favorite artist's album details.")
  print(" Please make sure that the database, favorite_ghanaian_artists is created using mysql in the terminal.")
  print(f''' 1. Open your spotify app
 2. Search for your artist and click the three dots near his/her name.
 3. Click the link in the window search bar.
 4. Copy the id that comes after the last slash and this is the artist id you need.
 5. Verify the program by checking inside the database if the right information was saved.''')
  user_input = gatherInput()
  value, name = build_url(str(user_input))
  df = build_dataframe(value, name)
  write_to_sql(df)
  

main()
