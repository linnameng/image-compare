#!/usr/bin/env python
import csv
import subprocess
import time
from decimal import Decimal

def extract_total_difference(output):
	output = output.partition("Total:")[2].split()[0]
	if (output == None):
		return "Invalid"
	return round(Decimal(output),2)

metric = "MAE"
image_folder_path = "images"
csv.register_dialect('myDialect', delimiter = ',', skipinitialspace=True)
csv_file  = open("compare.csv", "rb")
augmented_csv_file = open("compare-output.csv", "w");
reader = csv.reader(csv_file, dialect="myDialect")

# Skip first line (columns)
reader.next()
writer = csv.writer(augmented_csv_file)
writer.writerow(["image1","image2","similar","elapsed"])

for row in reader:
	image1 = image_folder_path+"/"+row[0]
	image2 = image_folder_path+"/"+row[1]

	# let user define metric
	start_time = time.time()
	output = subprocess.check_output(["gm","compare","-metric",metric,image1,image2])
	elapsed_time = time.time() - start_time

	split_output = output.splitlines();
	total_difference = extract_total_difference(output)

	writer.writerow(row+[total_difference]+[round(elapsed_time,3)])

csv_file.close()

