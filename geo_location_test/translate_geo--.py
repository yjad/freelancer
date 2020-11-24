from geopy.geocoders import Nominatim
#from uszipcode import ZipcodeSearchEngine
#import time
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
    
    with open(r"C:\Users\yahia\Downloads\ex.csv", "r", encoding="utf8") as csv_file:
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
            
    # if v_type == 0:       # empty line
        # print (line_no, "Empty Line")
        # return v_type, "Empty Line"
        # pass
    # if v_type == 1:
       # s = "------- Location:"
       #print (line_no, s, row[location_idx.index("loc")].strip())
       #s = "---- Location: " + row[location_idx.index("loc")].strip()
       # return v_type, row[location_idx.index("loc")].strip()      
    # elif v_type == 2:
        # s = "==== text Address:"
        # print (v, location_idx, location_idx.index("text"))
        # s = s + row[location_idx.index("text")].strip()
        # return v_type, address
        # print (line_no, s, address)
        # continue
        # location = get_location_by_address(address)
        # if not location:
            # s = f"Address not found: {address}"
        # else:
            # s = f"{address}, Location: {location}"
    # if v_type == 3:
        #s = "****** has both location and text location ****"
        # s = "both Coordinates & text address: " + row[location_idx.index("loc")].strip()
        # address = row[location_idx.index("text")].strip()
        # print (line_no, s, " &&& ", address)
        # continue
        # location = get_location_by_address(address)
        # if not location:
            # s = s + " ==>" + f"Address not found: {address}, use " + row[location_idx.index("loc")].strip()
        # else:
            # latitude = location["lat"]
            # longitude = location["lon"]
            # s = s + "==>" + f"{address}, Location: {latitude},{longitude}"
    # if v_type > 3:
        # s = process_multi_address(row, location_idx)
        # s= "XXXXX - multi text address:" + s
        #print (line_no, s)
        # s = f"{v_type} - {[v.strip() for v in row ]}"
        # continue
        
    
        # fp.write(f"{i}- {s} - {[v.strip() for v in row ]}, {[s for s in location_idx]}\n")
        # fp.write(f"{i}- {s} - {[v.strip() for v in row ]}\n")
    return v_type, location_idx
    
def process_file():
    desc = ["Empty: ", "Location: ", 'Address: ', "Both Location & address:", 'zip_code', "Others:", "*****"]
    fp = open("out.txt", "wt", encoding = 'utf8')
    rows = read_csv_1()
    for i, row in enumerate(rows):
        row_status, location_idx = process_row (row)
        # if row_status == 0:
            # continue
        # elif row_status == 1:   # location
            # s = row[location_idx.index("loc")].strip()
        # elif row_status == 2:   # address
            # s = "'" + row[location_idx.index("text")].strip()+ "'"
        # elif row_status == 3:    # location & address
            # location = row[location_idx.index("loc")].strip()
            # address = row[location_idx.index("text")].strip()
            # s = location + "--" + "'" + address + "'"
        # elif location_idx.count("zip_code"):    # zip code
            # s = row[location_idx.index("zip_code")].strip()
        # elif row_status > 4:  # location & address
            # s = process_multi_address(row, location_idx)
            # s = "XXXXX - multi text address:" 
            # for j, r in enumerate(location_idx):
                # if r in ['loc', 'text']:
                    # s = s + "'" + row[j].strip() + "'"        
        print (i+1, ": ", row_status)        
        fp.write(f"{i+1}: {row_status} - {[v.strip() for v in row ]} === {location_idx}\n")    
        # if i > 300:
            # break
    
    fp.close()
        
        
        
# def read_csv():
    # with open(os.path.join(os.path.join(folder, f))) as csv_file:
    # fp = open("out.txt", "wt", encoding = 'utf8')
    # with open(r"C:\Users\yahia\Downloads\ex.csv", "r", encoding="utf8") as csv_file:
        # csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        
    # fp.close()
    
def process_multi_address(row, location_idx):
    addresses=[]
    for i in range (0, len (location_idx)):
        if location_idx[i] == "text":
            addresses.append(row[i].strip())
            
    coordinates_1 = get_location_by_address(addresses[0])
    if not coordinates_1:
        s = " ==>" + f"Address not found: {addresses[0]}"
    else:
        s = "==>" + f"{addresses[0]}, Location: {coordinates_1}\n"

    coordinates_2 = get_location_by_address(addresses[1])
    if not coordinates_2:
        s = s + " ==>" + f"Address not found: {addresses[1]}"
    else:
        s = s + "==>" + f"{addresses[1]}, Location: {coordinates_2}"
    return s
    
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

# def get_location_by_zip_code(zip_code):
    # search = ZipcodeSearchEngine()
    # zip_data = search.by_zipcode(zip_code)
    # if zip_data:
        # return "{zip_data[latitude[}, {zip_data[longitude]}"
    # else:
        # return None
        
        
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
