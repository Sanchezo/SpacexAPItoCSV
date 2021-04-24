import requests # Import library that allows us to request data from API
import json # Import library that allows us to work with JSON files
from csv import writer #Import library that allows us to work with CSV files
def append_list_as_row(file_name, list_of_elem): #We create a function that allows us to save lists in seperate rows of CSV file
    
    with open(file_name, 'a+', newline='') as write_obj:
    
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)

apiendpoint="https://api.spacexdata.com/v3/launches" #API URL
response = requests.get(apiendpoint) #We request data from API
data = response.json() #We convert data that we received from API to a JSON file
for row in response.json(): #We convert the rows from JSON file into strings
    f_number = row.get('flight_number', None)
    name = row.get('mission_name', None)
    craft_id = row.get('rocket_id', None)
    craft_name = row.get('rocket_name', None)
    date_utc = row.get('launch_date_utc', None)
    link = row.get('video_link', None)
    data_list=[f_number,name,craft_id,craft_name,date_utc,link] #We put the strings into a list
    append_list_as_row('flights.csv', data_list) #We save the list as a row in CSV
#Made by Jakub Kapidura with the help of resources from the Internet
    

   

