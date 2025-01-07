import csv
import tscribe

tscribe.write("Input/1.json", format="csv",  save_as="Output/output1.csv")

Transcript = []
with open('Output/output1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        Transcript.append([row[3],row[4]])

for line in Transcript:
    print(f"{line[0]}: {line[1]}")