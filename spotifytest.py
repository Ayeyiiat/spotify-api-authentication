import spotipy, sqlalchemy, os
import requests
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import matplotlib
import matplotlib.pyplot as plt



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

def build_dataframe():
  #Converting to a pandas dataframe
  col_names = ["Artist's Name", "Album Name", "Number of tracks"]
  return pd.DataFrame(columns = col_names)
  
def load_dataframe(value, name):
  df = build_dataframe()
  i = 0
  while i < len(value['items']):
    df.loc[len(df.index)] = [name['name'], value["items"][i]["name"], value["items"][i]["total_tracks"]]
    i += 1
  return df

def saveSQLtoFile(filename, database_name):
    os.system('mysqldump -u root -pcodio '+database_name+' > '+ filename)
    
def loadSQLfromFile(filename, database_name):
    #create database if it does not exist
    os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS '+database_name+';"')
    os.system("mysql -u root -pcodio "+database_name+" < " + filename)

def createEngine(database_name):
    return create_engine('mysql://root:codio@localhost/'+database_name+'?charset=utf8', encoding='utf-8')
    
def saveDatasetToFile(database_name, table_name, filename, dataframe):
    dataframe.to_sql(table_name, con=createEngine(database_name), if_exists='replace', index=False)
    saveSQLtoFile(filename, database_name)

def loadDataset(database_name, table_name, filename, name, update=False):
    loadSQLfromFile(filename, database_name)
    df = pd.read_sql_table(table_name, con=createEngine(database_name))
    column_name = "Number of tracks"
    return statistics(df)
    
    
def histogram(df, column_name):
  df.hist(column = column_name)
  plt.show()
  
def boxplot(df, column_name, name):
  fig = plt.figure()
  box  = fig.add_subplot()
  box.boxplot(x = df[column_name], vert = False)
  box.set_xlabel(column_name)
  box.set_title("Distribution of "+ name['name'] +"'s albums")
  plt.show()
  
#Some data visualization
def statistics(df):
  print(df['Number of tracks'].mean())
  print(df[["Album Name", "Number of tracks"]].describe())

def main():
  print(" Welcome, you can use this program to get your favorite artist's album details.")
  print(" Please make sure that the database, favorite_ghanaian_artists is created using mysql in the terminal.")
  print(f''' 1. Open your spotify app
 2. Search for your artist and click the three dots near his/her name.
 3. Click the link in the window search bar.
 4. Copy the id that comes after the last slash and this is the artist id you need.
 5. Verify the program by checking inside the database if the right information was saved.''')
  database_name = 'favorite_artists'
  table_name = 'data'
  filename = 'spotifydata.sql'
  saveSQLtoFile(filename, database_name)
  loadSQLfromFile(filename, database_name)
  build_dataframe()
  user_input = gatherInput()
  value, name = build_url(str(user_input))
  dataframe = load_dataframe(value, name)
  saveDatasetToFile(database_name, table_name, filename, dataframe)
  loadDataset(database_name, table_name, filename, name, update=False)
  print("Your data has been represented on a graph. Please take a look at it")
  

main()
