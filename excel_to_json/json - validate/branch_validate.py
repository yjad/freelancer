import json
line_no = 1
#file_name= "D:\\Yahia\DTS\\2- Projects\\CR2\\3- Execution - Digital Banking\\Translation\\MA Files\\Locations\\atm-ar.json"
file_name = "C:\\Users\\YJAD\\Documents\\branch-ar.json"
#with open(file_name) as f:
        #read_data = f.readline()
        #for line in f:
        #        print (str(line_no) +"- ", line)
        #       line_no += 1
        #d = json.load(f)
        #for line in d:
        #print (str(line_no) +"- ", line)
        #        line_no += 1
        #        #print(d)

#        print (d["id"])
#f.closed

with open(file_name, 'r') as myfile:
    data=myfile.read()
myfile.close
# parse file
obj = json.loads(data)

#for o in obj:
#    print (o['id'])
#    if o['id'] == "3":
#        print(json.dumps(o, indent=4))
#        print('--------------------')

	
for o in obj:
    print(json.dumps(o, indent=4))
    #print (o['id'])
    #if o['id'] == "3":
    #   print(json.dumps(o, indent=4))
    #        print('--------------------')

