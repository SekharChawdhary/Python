import csv
with open("sample_data.csv", "r") as file_data:
    csv_reader = csv.reader(file_data)
    for row in csv_reader:
        if row[3].strip().lower() == 'banglore':
            print(row)
