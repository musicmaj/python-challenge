# Using the pathlib as recommended by my tutor as a best practice and preferred method over the os method since Python 3
import csv
import pathlib

with pathlib.Path('PyBank/Resources/budget_data.csv').open() as csvfile:
    reader = csv.reader(csvfile)
    csv_header = next(reader)

    raw = [row for row in reader]
    data_tuples = [(m, int(p)) for m,p in raw]
    data = dict(data_tuples)

    total_months = len(data.keys())
    total_pandl = sum(data.values())
    # I had help and utilized code with the help of my tutor, Anna Poulakos, and stack overflow for this section
    deltas = {}
    for x in range(len(data_tuples) -1):
        deltas[data_tuples[x + 1][0]] = data_tuples[x+1][1] - data_tuples[x][1]
    
    average_delta = sum(deltas.values()) / len(deltas)

    greatest_increase = max(deltas.values())
    greatest_increase_month = list(deltas.keys())[list(deltas.values()).index(greatest_increase)]

    greatest_decrease = min(deltas.values())
    greatest_decrease_month = list(deltas.keys())[list(deltas.values()).index(greatest_decrease)]
  
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months:  {total_months}")
    print(f"Total: ${total_pandl}")
    print(f"Average Change: ${average_delta:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# export to a text file
with open("PyBank/analysis/financial_analysis.txt", "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months:  {total_months}\n")
    file.write(f"Total: ${total_pandl}\n")
    file.write(f"Average Change: ${average_delta:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
    file.close()