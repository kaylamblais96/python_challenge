# PyBank

# Modules
import os 
import csv

# Set the path for the file relative to the designed directory structure
csv_path = os.path.join("Resources", "budget_data.csv")

# Print current working directory for debugging
print(f"Current working directory: {os.getcwd()}")
print(f"CSV path: {csv_path}")

# Check if the file exists
if not os.path.exists(csv_path):
    print(f"File does not exist: {csv_path}")
else:
    # Initialize variables
    total_months = 0
    total_profit_losses = 0
    previous_profit_losses = 0
    monthly_changes = []
    months = []

    # Read the CSV file
    with open(csv_path, encoding='UTF-8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        
        # Skip the header row
        next(csv_reader)
        
        # Loop through the rows in the file
        for row in csv_reader:
            # Append the month to the months list
            months.append(row[0])
            
            # Calculate the total number of months
            total_months += 1
            
            # Calculate the net total amount of "Profit/Losses"
            current_profit_losses = int(row[1])
            total_profit_losses += current_profit_losses
            
            # Calculate the changes in "Profit/Losses" and store in the list
            if total_months > 1:
                monthly_change = current_profit_losses - previous_profit_losses
                monthly_changes.append(monthly_change)
            
            # Update the previous_profit_losses for the next iteration
            previous_profit_losses = current_profit_losses

    # Calculate the average change in "Profit/Losses"
    average_change = sum(monthly_changes) / len(monthly_changes)

    # Calculate the greatest increase and decrease in profits
    greatest_increase = max(monthly_changes)
    greatest_decrease = min(monthly_changes)

    # Find the corresponding months for the greatest increase and decrease
    greatest_increase_month = months[monthly_changes.index(greatest_increase) + 1]
    greatest_decrease_month = months[monthly_changes.index(greatest_decrease) + 1]

    # Prepare the results
    results = (
        "Financial Analysis\n"
        "---------------------------------------------------------\n"
        f"Number of Months in the Dataset: {total_months}\n"
        f"Total: ${total_profit_losses}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
        f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
    )

    # Print the results
    print(results)

    # Export the results to a text file
    output_path = os.path.join("Analysis", "financial_analysis.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as output_file:
        output_file.write(results)
