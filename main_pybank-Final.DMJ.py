# Import Modules
import os
import csv

date = []
profitloss = []
new_date = []
combined = []
new_data = []
p_month = []
c_month = []
chng_history = []

plsum = 0
total_chng = 0

# Set path for file
csvfile = os.path.join("Resources", "budget_data.csv")

# Open and read csv
    # Read through each row of data after the header
with open(csvfile, mode="r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 
    for row in csvreader:    
        date.append(row[0])
        profitloss.append(row[1])

 #Request 1) The total number of months included in the dataset 
    count_months = len(date) - 1
    
    p_month = (profitloss[1:count_months])
    c_month = (profitloss[2:])  

#Request 2) The net total amount of "Profit/Losses" over the entire period
    for profitloss in profitloss[1:]:
        plsum = plsum + int(profitloss)
          
#Request 3) The average of the changes in "Profit/Losses" over the entire period       
    combined = [p_month, c_month]
    i = 0
    for month in p_month:
        chng = int(c_month[i]) - int(p_month[i]) 
        i+=1
        chng_history.append(chng)
        total_chng = total_chng + chng
    avg = round((total_chng) / (count_months - 1),2)

#Request 4) The greatest increase in profits (date and amount) over the entire period 
    great_inc = max(chng_history)
    new_date = (date[2:])
    new_data = [new_date, chng_history]
   
    j = 0
    for j in chng_history:
        if great_inc == int(j):
            j_row = (chng_history.index(j))
            great_inc_date = (new_date[j_row])
   
 #Request 5) The greatest decrease in losses (date and amount) over the entire period
    great_decr = min(chng_history)   

    k = 0
    for k in chng_history:
        if great_decr == int(k):
            k_row = (chng_history.index(k))
            great_decr_date = (new_date[k_row])   
       
#================================================================================================
myFile = open('pybank_analysis.txt', 'w')  
with myFile:  
 
#Title
    print("Financial Analysis")
    print("---------------------------")
    myFile.write("Financial Analysis\n")
    myFile.write("---------------------------\n")

#Request 1) The total number of months included in the dataset 
    print("Total Months: " + str(count_months))
    myFile.write("Total Months: " + str(count_months) + "\n")

#Request 2) The net total amount of "Profit/Losses" over the entire period
    print("Total: $" + str(plsum))
    myFile.write("Total: $" + str(plsum)+ "\n")
#Request 3) The average of the changes in "Profit/Losses" over the entire period 
    print("Average Change: $" + str(avg))
    myFile.write("Average Change: $" + str(avg) +"\n")

#Request 4) The greatest increase in profits (date and amount) over the entire period 
    print("Greatest Increase in Profits: " + str(great_inc_date) + " ($" + str(great_inc) + ")")
    myFile.write("Greatest Increase in Profits: " + str(great_inc_date) + " ($" + str(great_inc) + ")\n")

#Request 5) The greatest decrease in losses (date and amount) over the entire period
    print("Greatest Decrease in Profits: "+ str(great_decr_date) + " ($" + str(great_decr) + ")")
    myFile.write("Greatest Decrease in Profits: "+ str(great_decr_date) + " ($" + str(great_decr) + ")\n")
