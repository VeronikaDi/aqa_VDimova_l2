from pathlib import Path
import csv


path_to_file1 = Path('r-m-c.csv')
path_to_file2 = Path('rmc.csv')
path_to_file_for_results = Path('result_after_test_1.csv')

with open(path_to_file1, 'r') as file1:
    reader1 = csv.reader(file1)
    data1 = list(reader1)

with open(path_to_file2, 'r') as file2:
    reader2 = csv.reader(file2)
    data2 = list(reader2)

combined_data = data1 + data2
unique_data = []
seen = set()

for row in combined_data:
    row_tuple = tuple(row)
    if row_tuple not in seen:
        seen.add(row_tuple)
        unique_data.append(row)

with open(path_to_file_for_results, 'w', newline='') as file_with_results:
    writer = csv.writer(file_with_results)
    writer.writerows(unique_data)

