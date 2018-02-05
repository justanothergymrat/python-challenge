##############
##    imports
##############
import os
import csv

##############
##   variables
##############
# * directory set outside of git folder to avoid uploading anything large and having to spend
#   hours with seth again.

#toggle for data files
budget_data_1 = os.path.join("..","..","resources","budget_data_1.csv")
budget_data_2 = os.path.join("..","..","resources","budget_data_2.csv")

budget_output = os.path.join("..","..","resources","pybank.csv")
budget_output_txt = os.path.join("..","..","resources","pybank.txt")

budget_data_1_month = []
budget_data_1_revenue = []
budget_data_1_delta = []

budget_data_1_revenue_sum = 0
previousMonth = 0
budget_data_1_delta_sum = 0
avg_delta = 0


budgetResult = []

with open(budget_data_1, 'r', newline="") as csv_infile:
    csvreader = csv.reader(csv_infile, delimiter=",")


##############
##       read
##############
#extract values to play with
    for row in csvreader:
        if row[0] != "Date":
            budget_data_1_month.append(row[0])
            budget_data_1_revenue.append(row[1])
  

##############
##      maths
##############
# sum:
for item in budget_data_1_revenue:
    if type(item) is str:
        item = int(item)
    budget_data_1_revenue_sum += item

#avg change in rev:
for  x in range((len(budget_data_1_revenue))):
    if x > 0:
        previousMonth = int(budget_data_1_revenue[x - 1])
        budget_data_1_delta.append(int(budget_data_1_revenue[x]) - previousMonth)
        # print("previous month: " + str(previousMonth) + " , current month: " + str(budget_data_1_revenue[x]) + 
        #     " , difference: " + str(int(budget_data_1_revenue[x])-previousMonth) + " .")
    next
#sum it (cause we aren't using pandas........):
for item in budget_data_1_delta:
    if type(item) is str:
        item = int(item)
    budget_data_1_delta_sum += item
#divide
avgDelta = budget_data_1_delta_sum / len(budget_data_1_delta)
#crossreference it
maxIndex = budget_data_1_delta.index(max(budget_data_1_delta))
minIndex = budget_data_1_delta.index(min(budget_data_1_delta))

##############
##      output
##############
budgetResult = zip(budget_data_1_month,budget_data_1_revenue)

#to terminal
print("\nFinancial Analysis\n",
"-------------------------\n",
"Total Months: " + str(len(budget_data_1_month)) + "\n",
"Total Revenue: " + '${:,.2f}'.format((budget_data_1_revenue_sum)) + "\n",
"Average Revenue Change: " + '${:,.2f}'.format((avgDelta)) + "\n",
"Greatest Increase in Revenue: " + str(budget_data_1_month[maxIndex + 1]) + " (" + '${:,.2f}'.format((max(budget_data_1_delta))) + ")\n",
"Greatest Decrease in Revenue: " + str(budget_data_1_month[minIndex + 1]) + " (" + '${:,.2f}'.format((min(budget_data_1_delta))) + ")\n"
)
# prep for output

# csv output below commented out:

# analysis = ["Financial Analysis",
# "-------------------------\n",
# "Total Months: " + str(len(budget_data_1_month)) + "\n",
# "Total Revenue: " + '${:,.2f}'.format((budget_data_1_revenue_sum)) + "\n",
# "Average Revenue Change: " + '${:,.2f}'.format((avgDelta)) + "\n",
# "Greatest Increase in Revenue: " + str(budget_data_1_month[maxIndex + 1]) + " (" + '${:,.2f}'.format((max(budget_data_1_delta))) + ")\n",
# "Greatest Decrease in Revenue: " + str(budget_data_1_month[minIndex + 1]) + " (" + '${:,.2f}'.format((min(budget_data_1_delta))) + ")\n"
# ]

# #create output file
# with open(budget_output, 'w', newline="") as csv_outfile:
#     csvwriter = csv.writer(csv_outfile, delimiter=',')
#     csvwriter.writerows(budgetResult)
    
# #append analysis  
# with open(budget_output, 'a', newline="") as csv_outfile:
#     csvwriter = csv.writer(csv_outfile, delimiter=',')
#     csvwriter.writerow(analysis)

#using text files cause why not
print("\nAnalysis exported to .txt file!\n")
with open(budget_output_txt,'w') as text_file:
    print(f"Financial Analysis\n",
"-------------------------\n",
"Total Months: " + str(len(budget_data_1_month)) + "\n",
"Total Revenue: " + '${:,.2f}'.format((budget_data_1_revenue_sum)) + "\n",
"Average Revenue Change: " + '${:,.2f}'.format((avgDelta)) + "\n",
"Greatest Increase in Revenue: " + str(budget_data_1_month[maxIndex + 1]) + " (" + '${:,.2f}'.format((max(budget_data_1_delta))) + ")\n",
"Greatest Decrease in Revenue: " + str(budget_data_1_month[minIndex + 1]) + " (" + '${:,.2f}'.format((min(budget_data_1_delta))) + ")\n",
file = text_file)
    print(f" -----------------\n",
    "Data to follow:\n",
    "-----------------\n",
    file = text_file)
    for item in budgetResult:
        text_file.write(str(item)+"\n")