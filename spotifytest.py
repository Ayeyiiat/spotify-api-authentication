import spotipy
import requests

#Spotify authentication setup
#Get your own ID and secret after creating a spotify developer account and starting a new app
CLIENT_ID = 'should be secret'
CLIENT_SECRET ='should be secret'

AUTH_URL = 'https://accounts.spotify.com/api/token'
auth_response = requests.post(AUTH_URL, {
  'grant_type' : 'client_credentials',
  'client_id' : CLIENT_ID,
  'client_secret' : CLIENT_SECRET,
})

print(auth_response.status_code)
auth_response_data = auth_response.json()
print(auth_response_data)

access_token = auth_response_data['access_token']


#Get rema's music details
token = "Bearer{token}".format(token=access_token)
print(token)

headers = {
  "Authorization" : token
}
BASE_URL = 'https://api.spotify.com/v1/'

#returning audio features of an artist's song
track_id = '46pWGuE3dSwY3bMMXGBvVS'
r = requests.get(BASE_URL + 'audio-features/' + track_id_id, headers = headers)
print(r.json())
