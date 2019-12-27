# Import csv
import os
import csv

# join path
budget_csv = os.path.join("Resources", "budget_data.csv")


# create lists
total_months =[]
total_profit = []
monthly_profit_change = []

# Open Csv
with open(budget_csv, newline="") as csvfile:
    
    # store data in csvreader variable 
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip header 
    header = next(csvreader)

    
    # Iterate through rows 
    for row in csvreader:
       
        # Append the total months and total profit to their corresponding lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # Iterate through the profits to get the monthly change in profits
    for i in range(len(total_profit)-1):
        
        # Take the change between months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
      
# Get the max and min of the monthly profit change         
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Get corresponding month to max and min above, +1 because the corresponding month is the next month
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

#print results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

#output text file 
file = open("output.txt", "w")    
file.write("Financial Analysis")
file.write("\n")
file.write("----------------------------")
file.write("\n")
file.write(f"Total Months: {len(total_months)}")
file.write("\n")
file.write(f"Total: ${sum(total_profit)}")
file.write("\n")
file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
file.write("\n")
file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
file.write("\n")
file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
file.close()
