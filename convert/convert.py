import csv

# Define the LST file and the output CSV file paths
lst_file_path = "path of your file.lst"
csv_file_path = 'output1.csv'

# Read the LST file
with open(lst_file_path, 'r') as lst_file:
    lines = lst_file.readlines()



# Process the data lines
data = []
for line in lines[0:]:
    data.append(line.strip().split())

# Write to CSV
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    # Write the header
    # writer.writerow(headers)
    # Write the data rows
    writer.writerows(data)

print("Conversion complete: 'output.csv' created.")
