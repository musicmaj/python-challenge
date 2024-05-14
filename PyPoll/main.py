import csv
import pathlib
# This import counter collection came as a suggestion from my tutor, Anna Poulakos
from collections import Counter

with pathlib.Path('PyPoll/Resources/election_data.csv').open() as csvfile:
    reader = csv.reader(csvfile)
    csv_header = next(reader)
    raw = [row for row in reader]
    
    total_votes = len(raw)
    candidate_names = list([elem[2] for elem in raw])
    candidate_counts = Counter(candidate_names)
    

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    
    winner = ""
    most_votes = 0
    for name, votes in candidate_counts.items():
        vote_percentage = votes/total_votes * 100
        # I got this loop to check for the winner from my tutor, Anna Poulakos
        if votes > most_votes:
            winner, most_votes=name, votes
        print(f"{name}: {vote_percentage:.3f}% ({votes})")
    
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# export to text file
with open("PyPoll/analysis/election_data.txt", "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    winner = ""
    most_votes = 0
    for name, votes in candidate_counts.items():
        vote_percentage = votes/total_votes * 100
        if votes > most_votes:
            winner, most_votes=name, votes
        file.write(f"{name}: {vote_percentage:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
