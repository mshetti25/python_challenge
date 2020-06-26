import os
import csv

csvpath = os.path.join('..', 'python_challenge', 'PyPoll','Resources', 'election_data.csv')
#reading csv file
with open(csvpath) as filepath:
    csvreader = csv.reader(filepath, delimiter = ',')

    csvheader = next(csvreader) #removing header
    final = list(csvreader) 
    #initialize total months and total to 0
    count = 0
    total = 1
    count = len(final)
    output_path = os.path.join('..', 'python_challenge', 'PyPoll','Analysis', 'PyPoll.txt')
    f = open(output_path, "w")
    f.write("Election Results \n")
    f.write("---------------------------------------------- \n")
    f.write(f"Total Months : {count} \n")
    f.write("---------------------------------------------- \n")

    print("Election Results")   
    print("-----------------------------------------")        
    print(f"Total Votes : {count}")
    print("-----------------------------------------")   
    Candidates_dict = {}
    for col in final:
         if col[2] not in Candidates_dict:
             Candidates_dict[col[2]] = 1
         else:
            Candidates_dict[col[2]] += 1
    maxi = max(Candidates_dict.values()) 
    for key in Candidates_dict:
        per_total = round(Candidates_dict[key]/count * 100, 3)
        print (f"{key}: {per_total}% ({Candidates_dict[key]})")
        f.write(f"{key}: {per_total}% ({Candidates_dict[key]}) \n")
        if Candidates_dict[key] == maxi:
            Winner = key
    print("-----------------------------------------")
    print(f"Winner: {Winner}")     
    print("-----------------------------------------")
    f.write("----------------------------------------- \n")
    f.write(f"Winner: {Winner} \n")
    f.write("----------------------------------------- \n")
    f.close()


