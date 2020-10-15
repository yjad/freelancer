import xml.etree.ElementTree as ET
import json

FILE_NAME = r'E:\Yahia-Home\Python\src\Freelancer\xml2json\data\test.xml'
root = ET.parse(FILE_NAME).getroot()

# for type_tag in root.findall('bar/type'):
#     value = type_tag.get('foobar')
#     print(value)

# print ("root:", root.text, "tag:", root.tag, "attrib:", root.attrib)

catalog_arr = []
for child in root:
    #print (f"child tag:{child.tag}, attrib:{child.attrib}, text:{child.text}")
    #print (f"child tag:{type(child.tag)}, attrib:{type(child.attrib)}, value:{type(child.text)}")
    #print (50*"-")
    dict_x = child.attrib
    for x in child:
        dict_x[x.tag] = x.text
        #print ("tag:",x.tag, "attrib:", x.attrib, "text:", x.text)

        # if type (x.attrib) == dict:
        #     for item in x.attrib:
        #         print (item, x[item])

    dict_y = {child.tag:dict_x}
    # print (dict_x)
    # print (dict_y)
    # print(20 * "-")
    catalog_arr.append(dict_y)

catalog = {root.tag:catalog_arr}
print(json.dumps(catalog, indent=4))
#input("press any key to continue")
