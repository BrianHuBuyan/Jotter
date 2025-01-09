import csv
import tscribe


def Json2txt(file_name):
    inputfile = f"Input/{file_name}.json"
    outputfile = f"Output/{file_name}"

    tscribe.write(inputfile, format="csv",  save_as= f"{outputfile}.csv")

    Transcript = []
    with open(f"{outputfile}.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            Transcript.append([row[3],row[4]])


    with open(f"{outputfile}.txt", "w") as file:
        for line in Transcript:
            file.write(f"{line[0]}: {line[1]}")  
            file.write("\n")

# input = "Input/Retrieval_test3"
# output = "Output/Retrieval_test3"
Json2txt("Retrieval_test4")