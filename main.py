import csv

with open(r'C:\Users\SOHAIB MUHAMMAD\OneDrive\Documents\GitHub\Python-automation\data\dirty_cafe_sales.csv' , mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)