import requests # Import library that allows us to request data from API
import json # Import library that allows us to work with JSON files
from csv import writer #Import library that allows us to work with CSV files
class SpaceXHTTPError(Exception):
    pass 
def append_list_as_row(file_name, list_of_elem): #We create a function that allows us to save lists in seperate rows of CSV file
    
    with open(file_name, 'a+', newline='') as write_obj:
    
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)
url="https://api.spacexdata.com/v3/launches"
def getdata(url):
    try:
        response = requests.get(url) #We request data from API
        return response.json() #We convert data that we received from API to a JSON file
    except requests.exceptions.HTTPError:
        raise SpaceXHTTPError("Unable to get the data")
data=getdata(url)
for row in data: #We convert the rows from JSON file into strings
    f_number = row.get('flight_number', None)
    name = row.get('mission_name', None)
    craft = row.get('rocket', None)
    patch=row.get("links",None)
   
    date_utc = row.get('launch_date_utc', None)
    
    data_list=[f_number,name,craft.get('rocket_id',None),craft.get('rocket_name',None),patch.get('video_link',None),date_utc] #We put the strings into a list
    append_list_as_row('flights.csv', data_list) #We save the list as a row in CSV
#Made by Jakub Kapidura with the help of resources from the Internet