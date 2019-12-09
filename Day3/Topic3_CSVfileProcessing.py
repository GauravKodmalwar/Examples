# https://www.geeksforgeeks.org/working-csv-files-python/

import csv
filename = "FL_insurance_sample.csv"
fields = [] # title
rows = [] # rows

# reading csv file
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader) # extracting field names through first row

    for row in csvreader: # extracting each data row one by one
        rows.append(row)
    print("Total no. of rows: %d" % (csvreader.line_num)) # get total number of rows

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

#  printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    # parsing each column of a row
    for col in row:
        print("%10s" % col),
    print('\n')

# *************** writing to a CSV file ***************
import csv

fields = ['Name', 'Branch', 'Year', 'CGPA'] # field names

rows = [['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']] # data rows of csv file

filename = "university_records.csv" # name of csv file

# writing to csv file
with open(filename, 'w+', newline='\n') as csvfile:
    csvwriter = csv.writer(csvfile) # creating a csv writer object
    csvwriter.writerow(fields)     # writing the fields
    csvwriter.writerows(rows)    # writing the data rows