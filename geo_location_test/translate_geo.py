from geopy.geocoders import Nominatim
# from uszipcode import ZipcodeSearchEngine
from uszipcode import SearchEngine
import time
from pprint import pprint
import csv
import sys



app = Nominatim(user_agent="tutorial")

def is_float(v):
    try:
        f=float(v)
    except ValueError:
        return False
    return True
      
      
def is_coordinate(loc):
    v = loc.split(",")
    if len (v) ==2 and is_float(v[0]) and is_float(v[1]):
        return v[0], v[1]
    else:
        return None, None
        
def is_zip_code(s):
    s = s.strip()
    return (s.isnumeric() and len (s) == 5)
        
def get_location(row):
    lat, lon = is_coordinate(v)
    if lat:
        print (i, j, "location:", v)
    else:
        print (i, j, "text location:", v)
        location = get_location_by_address(v)
        if location:
            latitude = location["lat"]
            longitude = location["lon"]
            print(f"address: {v}, Lat: {latitude}, Long: {longitude}")
        else:
             print ("Address could not be found:", v) 
        

def read_csv_1():
    
    with open(r"ex.csv", "r", encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        for i, row in enumerate(csv_reader):
            yield row
    
    
def process_row(row):
    
    v_type = 0
    location_idx = [''] * len(row)
    for j, v in enumerate(row):
        v = v.strip()
        # print (j, v)
        if not v or v == "NULL" or v.lstrip('-').isnumeric():
            if is_zip_code(v):
                v_type += 100
                location_idx[j] = "zip_code"
            else:
                continue
        else:
            lat, lon = is_coordinate(v)
            if lat:
                v_type +=1
                #print (i, j, "location:", v)
                location_idx[j] = "loc"
            else:
                v_type += 10
                location_idx[j] = "text"
                #print (i, j, "text location:", v)
            
    
    return v_type, location_idx
    
def process_file():
    desc = ["Empty: ", "Location: ", 'Address: ', "Both Location & address:", 'zip_code', "Others:", "*****"]
    fp = open("out.txt", "wt", encoding = 'utf8')
    rows = read_csv_1()
    for i, row in enumerate(rows):
        row_status, location_idx = process_row (row)   
        print (i+1, ": ", row_status) 
        # if row_status not in [0, 1, 11, 101]:
        #if row_status in [20]:
        zip_code = ""
        location = ""
        if row_status in [100, 110, 101]:
            zip_code = "zip code: " + str(get_location_by_zip_code(row[location_idx.index("zip_code")].strip()))
        if row_status in [10, 110]:
            location = "location: " + str(get_location_by_address(row[location_idx.index("text")].strip()))
            #fp.write(f"{i+1}: {row_status} - {[v.strip() for v in row ]} === {location_idx}\n")    
        if row_status in [10, 100, 110, 101]:
            fp.write(f"{i+1}: {row_status} - {[v.strip() for v in row ]} ===> {location} {zip_code}\n")    
        if i > 300:
            break
    
    fp.close()
    
def get_location_by_address(address):
    """This function returns a location as raw from an address
    will repeat until success"""
    time.sleep(1)
    try:
        location_raw = app.geocode(address).raw
        latitude = location_raw["lat"]
        longitude = location_raw["lon"]
        coordinates = f"{latitude}, {longitude}"
        return coordinates
    except AttributeError:
        return None # invalid location
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        return get_location_by_address(address)
        
        
        
def get_address_by_location(latitude, longitude, language="en"):
    """This function returns an address as raw from a location
    will repeat until success"""
    # build coordinates string to pass to reverse() function
    coordinates = f"{latitude}, {longitude}"
    # sleep for a second to respect Usage Policy
    time.sleep(1)
    try:
        return app.reverse(coordinates, language=language).raw
    except:
        return get_address_by_location(latitude, longitude)

def get_location_by_zip_code(zip_code):
    search = SearchEngine()
    zip_data = search.by_zipcode(zip_code)
    if zip_data:
        zc = zip_data.to_dict()
        return f"{zc['lat']}, {zc['lng']}"
    else:
        return None
        
        
if False:
    # address = "Makai Road, Masaki, Dar es Salaam, Tanzania"
    address = " Portland, Oregon"
    location = get_location_by_address(address)
    latitude = location["lat"]
    longitude = location["lon"]
    print(f"address: {address}, Lat: {latitude}, Long: {longitude}")
    # print all returned data
    pprint(location)

if False:
    # define your coordinates
    latitude = 36.723
    longitude = 3.188
    # get the address info
    address = get_address_by_location(latitude, longitude)
    # print all returned data
    pprint(address)
    
# read_csv()
process_file()
