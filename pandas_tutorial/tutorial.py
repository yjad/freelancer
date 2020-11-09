import pandas as pd
import matplotlib.pyplot as plt

def load_sample_data():
    data = {
        'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
        'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai','Manchester', 'Cairo', 'Osaka'], 'age': [41, 28, 33, 34, 38, 31, 37],
        'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
        }
        
    row_labels = [101, 102, 103, 104, 105, 106, 107]
    df = pd.DataFrame(data = data, index = row_labels)

    print (df)

def load_linux_csv():
    df = pd.read_csv(r"HQ-LINUX.csv", sep = ";")
    return df

def plot_data():
    df.plot()
    plt.show()

def print_all_data():
    for row_label, row in df.iterrows():
        print(row_label, row, sep='\n', end='\n\n')
    
# print (df.describe())

# filtering data

# filter_ = df['name'].where(cond=df['py-score'] >= 80, other=0.0)

# print ("----- filter: df['name'].where(cond=df['py-score'] >= 80, other=0.0)\n", filter_)
# print ("----- df.where(cond=df['py-score'] >= 80): \n", df.where(cond=df['py-score'] >= 80))
# print ("----- df.where(cond=df['py-score'] >= 80): \n", df.where(cond=df['py-score'] >= 80))
# print ("-----df[df['py-score'] >= 80]\n", df[df['py-score'] >= 80])

df = load_linux_csv()
pd.set_option('display.max_rows',20)
print (df.describe())
print (df.head)
print (df.risk)