import os
import csv

#path to collect data from the resource folder
csvpath = os.path.join('Resources', 'budget_data.csv')

#created variables
total_months = 0
total_profit = 0
net_change_list = []
months_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 10000000]
previous_loss_profit = 0
net_total = 0
monthly_change = 0
profit = []
file_to_output = "textfile.txt"
average_change = 0

#open and read csv
with open(csvpath) as csvfile:
  
  csvreader = csv.reader(csvfile, delimiter=",")
  
  csv_header= next(csvreader)


  #calculate total number of months in the dataset
    #loop through the total months 
  for rows in csvreader:
    total_months = total_months + 1

    #calculate the net total profit/loss
    net_total+= int(rows[1])

    #calculate the change in profit/loss
    if total_months > 1: 
      monthly_change = int(rows[1]) - previous_loss_profit
      previous_loss_profit = int(rows[1])
    
    months_change_list.append(monthly_change)

   #read through each row of data 
  #date.append(row[0])
    #profit.append(rows[1])

  
    #print(total_months)

#check the greatest increase/decrease in profits
    #if total_months > 1:
      #monthly_change = int(rows[1]) - previous_loss_profit
      #monthly_change.append(monthly_change)
# Check for greatest increase and decrease in profits
    if monthly_change > greatest_increase[1]:
      greatest_increase[0] = rows[0]
      greatest_increase[1] = monthly_change

    if monthly_change < greatest_decrease[1]:
      greatest_decrease[0] = rows[0]
      greatest_decrease[1] = monthly_change

    # Update previous profit/loss
    

    # Calculate average change
    if len(months_change_list) > 0:
      average_change = sum(months_change_list[1:]) / len(months_change_list[1:])
      average_change = round(average_change,2)

print(months_change_list)

# Prepare the analysis results
analysis_results = (
f"\nFinancial Analysis\n"
f"----------------------------\n"
f"Total Months: {total_months}\n"
f"Total: ${net_total}\n"
f"Average Change: ${average_change:.2f}\n"
f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the analysis results
print(analysis_results)

# Write the analysis results to a text file
with open(file_to_output, "w") as txtfile:
    txtfile.write(analysis_results)
