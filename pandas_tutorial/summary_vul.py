import pandas as pd
import numpy as np

#DATA_FILE = r"C:\Users\yahia\Downloads\2020-11-09-data_export.csv"
DATA_FILE = r"C:\Users\yahia\Documents\Qradar\09-2020 - Copy\HQ-BRANCHES-LEGACY-SERVERS-LINUX.csv"

QRADAR_header = ["name","criticalDetails","concern","vulnerabilities","numHosts","solution","ipaddress",
        "assetName","risk","description","runSchedule","vulnerability","cveid"]
#df = pd.read_csv(data_file, header = 0, names = QRADAR_header, sep = ",")



def summary_vul(data_file, no_header, seperator):

    if no_header:
        df = pd.read_csv(data_file, header = 0, names = QRADAR_header, sep = seperator)
    else:
        df = pd.read_csv(data_file, sep = seperator)
    
    # print_stats(df)
    print_risk_stats(df)
    
    
def print_det(df):
    print ('-' * 30, "High risks detils", '-' * 30)
    det = df.loc[df.risk == 'High', ['ipaddress', 'vulnerability']]
    #iterate_by_row(det)

    
def print_by_col(det):
    for  col_name, item in det.iteritems():
        print ("Col Name:", col_name)
        for x in item:
            print (type(x), x)
    
    
def print_by_row(det):
    i = 1
    for  index, row in det.iterrows():
        print (i, "- ", index[0], index[1], ":", [x for x in row])
        i +=1



def print_stats(df):
    server_vul_by_risk = df.groupby(["name", "ipaddress","risk"])["name"].count()
    print (server_vul_by_risk)
   
    for  index, value in server_vul_by_risk.items():
        #print (index, value, ":", [x for x in value])
        print (index, ":", value)
    print ("------------------------------")
    #print ([x for x in server_vul_by_risk.items()])

def print_risk_stats(df):
    df['High Risk'] = np.where(df.risk == 'High', "High",None)
    df['Mid Risk'] = np.where(df.risk == 'Medium', "Mid",None)
    df['Low Risk'] = np.where(df.risk == 'Low', "Low",None)
    df['Warning Risk'] = np.where(df.risk == 'Warning', "Warning",None)
    xx = df.groupby(["name", "ipaddress"])[['High Risk', 'Mid Risk', 'Low Risk', 'Warning Risk']].count()
    # print ("-"* 50,"\n", xx.head(50))
    # xx.describe()
    print_by_row(xx)
        
summary_vul(r"C:\Users\yahia\Documents\Qradar\09-2020 - Copy\HQ-BRANCHES-LEGACY-SERVERS-LINUX.csv"
                                , no_header = False, seperator = ";")
# summary_vul(r"C:\Users\yahia\Downloads\2020-11-09-data_export.csv", no_header = False, seperator = ",") 
