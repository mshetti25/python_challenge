import os
import csv

csvpath = os.path.join('..', 'python_challenge', 'PyBank','Resources', 'budget_data.csv')
#reading csv file
with open(csvpath) as filepath:
    csvreader = csv.reader(filepath, delimiter = ',')

    csvheader = next(csvreader) #removing header
    final = list(csvreader) 
    #initialize total months and total to 0
    count = 0
    total = 0
    for col in final:
        count = count+1 #Calculate total months
        total += int(col[1]) #Calculate Total

    firstele = int(final[0][1]) 
    
    lastel = int(final[-1][1])
    # calculate Average Change
    avg = (lastel - firstele)/(count - 1)    
    rounded_avg = round(avg,2)

    max = 0
    min = int(final[1][1]) - int(final[0][1])
    #finding minimum and maximum change in profits
    for i in range(1, count-1):
        diff = int(final[i][1]) - int(final[i-1][1])
        if diff < min:
            min = diff
            mini = final[i][0]
        if diff > max:
            max = diff
            maxi = final[i][0]
    
        
print(f"Total Months : {count}")
print(f"Total : ${total}")
print(f"Average Change : ${rounded_avg}")
print(f"Greatest increase in profit : {maxi} ($ {max})")
print(f"Greatest decrease in profit : {mini} ($ {min})")

#Path for output file
ot_path = os.path.join('..', 'python_challenge', 'PyBank','Analysis', 'PyBank.txt')

# writing output in text file

f = open(ot_path, "w")
f.write(f"Total Months : {count} \n")
f.write(f"Total : ${total} \n")
f.write(f"Average Change : ${rounded_avg} \n")
f.write(f"Greatest increase in profit : {maxi} ($ {max}) \n")
f.write(f"Greatest decrease in profit : {mini} ($ {min}) \n    ")
f.close()


