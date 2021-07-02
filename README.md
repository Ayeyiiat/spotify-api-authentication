  # AYEYI'S SPOTIFY API DOCUMENTATION
  
  ## GENERAL OVERVIEW
  * Creating the spotify api connection.
  * Parsing data from your spotify developer's account.
  * Coalating this data into a dataframe in pandas and connecting to a database in mysql.
  * Creating a little program to collect artists' albums and number of tracks on each album.
  
  
  ### CREATING THE SPOTIFY CONNECTION
  1. Make sure to create a Spotify developer's account. You can use the link below;
    * https://developer.Spotify.com/dashboard/login
    
  2. Once the account is created, start an app and get your Client ID and Client Secret.
  
  3. Using these credentials, you can now establish a connection to the spotify api.
  

  ### PARSING DATA FROM THE API
  1. Read the GET/POST request documentation on the spotify developer's account.
  
  2. This is necessary in order to get the correct url depending on what kind of information you want to extract.
  
  3. If you want an artist or a track ID, simply open the spotify player app for music, choose that artist or track, press the three dots that appear next to it and in your web browser, copy the last string or text.
  
  
  ### STORING DATA COLLECTED FROM API INTO A PD DATAFRAME AND CONNECTING TO A DATABASE
  1. Make sure spotipy and pandas are *installed*. You can use the terminal commands below;
    * sudo pip3 intall spotipy
    * sudo pip3 intall pandas
  
  2. Create a database in mysql. You can use the terminal command below pressing enter after each command;
    * mysql
    * CREATE DATABASE databasename;
    * exit;
    
  3. You can easily now connect your dataframe to this database.
  
  
  ### THE PROGRAM ITSELF
  This current program, requests for a user's chosen artist's ID, connects to my created spotify-api-developer's account and creates a dataframe with the chosen artist's name, album names and number of tracks on each album. This is then saved into a database called favorite_ghanaian_artists.
  
  