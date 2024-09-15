# PyPoll

# Modules
import os 
import csv

# Set the correct path 
csv_path = os.path.join("Resources", "election_data.csv")

# Check if the file exists
if not os.path.exists(csv_path):
    print(f"File does not exist: {csv_path}")
else:
    # Initialize a dictionary to store the candidate vote counts
    candidate_votes = {}

    # Read the CSV file
    with open(csv_path, encoding='UTF-8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        
        # Skip the header row
        next(csv_reader)
        
        # Loop through the rows in the file
        for row in csv_reader:
            # Extract the candidate name from each row
            candidate_name = row[2]
            
            # If the candidate is already in the dictionary, increment their vote count
            if candidate_name in candidate_votes:
                candidate_votes[candidate_name] += 1
            # If the candidate is not in the dictionary, add them with a vote count of 1
            else:
                candidate_votes[candidate_name] = 1

    # Calculate the total number of votes cast
    total_votes = sum(candidate_votes.values())

    # Prepare the results
    results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        results += f"{candidate}: {percentage:.3f}% ({votes})\n"

    results += "-------------------------\n"
    winner = max(candidate_votes, key=candidate_votes.get)
    results += f"Winner: {winner}\n"
    results += "-------------------------\n"

    # Print the results
    print(results)

    # Export the results to a text file
    output_path = os.path.join("Analysis", "election_results.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as output_file:
        output_file.write(results)


