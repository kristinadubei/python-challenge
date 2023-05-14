# Modules
import os
import csv

# Path to budget_data file for analysis
bankdata_csv = os.path.join("Resources", "budget_data.csv")

# Lists for storing data and variables to store results
header_row = []
date = []
ProfLoss = []
by_period_change = []
period_count = 0
net_total = 0

# Open budget file as read
with open(bankdata_csv) as datafile:
    csvreader = csv.reader(datafile, delimiter=",")
    # Store headers and move to data rows for next steps
    header_row = next(datafile).split(",")

    for row in csvreader:
        # Count number of period/months
        period_count = period_count + 1
        # Sum the profit/loss to find net change
        net_total = net_total + int(row[1])
        # Copy the profit/loss data into list for further analysis
        ProfLoss.append(row[1])
        # Copy the period date info for further tracking of changes per period
        date.append(row[0])

# Remove first date as it cannot be compared to previos period
del date[0]

# For each next period (ignoring the first) calculate it's change by subtracting next period's value from current period
for i in range(len(ProfLoss)-1):
    # Store the changes values in the list
    by_period_change.append(int(ProfLoss[i+1]) - int(ProfLoss[i]))

# Calculate the average change
average_change = round(sum(by_period_change)/len(by_period_change), 2)

# Defined a function to look for max increase and the period correponding to max increase
def find_max_increase_and_date(dates, list):
    max = list[0]
    maxdate = dates[0]
    for i in range(len(list)-1):
        if list[i+1] > max:
            max = list[i+1]
            maxdate = dates[i+1]
    return maxdate, max

# Defined a finction to look for max decrease and the period corresponding to max decrease 
def find_max_decrease_and_date(dates, list):
    min = list[0]
    mindate = dates[0]
    for i in range(len(list)-1):
        if list[i+1] < min:
            min = list[i+1]
            mmindate = dates[i+1]
    return mindate, min

# Use max increase/max decrease functions and store their results in following lists
max_increase = find_max_increase_and_date(date, by_period_change)
max_decrease = find_max_decrease_and_date(date, by_period_change)

# Set variable for output file
output_file = os.path.join("analysis", "analysis.txt")

# Open the output file
with open(output_file, "w") as file:
    # Write the analysis inserting results
    file.writelines(["Financial Analysis\n", "---------------------------------\n", f"Total Months: {period_count}\n", f"Total Net Change: ${net_total}\n"])
    file.writelines([f"Average Change: ${average_change}\n", f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})\n", f"Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})\n"])

# Print results to terminal
print(" Financial Analysis\n", "---------------------------------\n", f"Total Months: {period_count}\n", f"Total Net Change: ${net_total}\n", f"Average Change: ${average_change}\n", f"Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})\n", f"Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})\n")

