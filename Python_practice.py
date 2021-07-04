import csv
import os
#load election results raw data from csv
File_to_load = os.path.join("Resources", "election_results.csv")
with open(File_to_load, "r") as election_data:
    file_reader = csv.reader(election_data)
    #for row in file_reader: 
    headers = next(file_reader)
    print(headers)


File_to_save =  os.path.join("Analysis", "election_analysis.txt")
with open(File_to_save, "w") as txt_file:
    txt_file.write("hello world!")

#open output text document in write mode