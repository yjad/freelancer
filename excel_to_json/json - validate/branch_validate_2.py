import json
file_name = "list_billers.txt"

with open(file_name, 'r') as myfile:
    data=myfile.read()
myfile.close
# parse file
brs = json.loads(data)
#print(json.dumps(brs['id'], indent=4))
# for b in brs:
#     #print(json.dumps(b, indent=4))
#     print (b['id'], b['title'], "city: ", b['address']['city'], "street:", b['address']['street'])

fp= open('list_biller.json', 'wt')
json.dump(brs,fp, indent=4)

print (brs)