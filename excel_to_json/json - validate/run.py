from fawry_billers import fawry_billers_excel

#print_values("", billers)

#list_billers(billers['biller_records'])
#print (billers['biller_records'])
#list_billers(billers['biller_records'])
#list_biller_info(billers['biller_records'], 'biller_information')
file_name = r'E:\Yahia-Home\Python\src\json - validate\response.json'
fawry_billers_excel(file_name)
print ('output file:', file_name +".xlsx" )
