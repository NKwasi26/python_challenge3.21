import os
import csv

# provide file path
file_path = os.path.join('Resources','election_data.csv')
output_path = 'election_analysis.txt'

# name variables
total_votes = 0
candidates_options = []
votes_dict ={}


with open(file_path) as csvfile:
  csv_reader = csv.reader(csvfile)


  #Read the header row
  csv_header = next(csv_reader)
  #Iterate through each row in the file starting after the header
  for row in csv_reader: 
    #calculate total votes
    total_votes +=1
    candidates= row[2]
    #list of candidates who won
    if candidates not in candidates_options:
      candidates_options.append(candidates)
      votes_dict[candidates]= 0
    votes_dict[candidates] +=1
         
print(votes_dict)   
#calculate percentages of votes won 
css_percentage = round(votes_dict["Charles Casper Stockham"]/total_votes * 100, 3)
ddg_percentage = round(votes_dict["Diana DeGette"]/total_votes * 100, 3)
rad_percentage = round(votes_dict["Raymon Anthony Doane"]/total_votes * 100, 3)

#determine winner
votes = [votes_dict["Charles Casper Stockham"], votes_dict["Diana DeGette"], votes_dict["Raymon Anthony Doane"]]
candidates = ["Charles Casper Stockham", "Diana DeGette","Raymon Anthony Doane"]
winner = candidates[votes.index(max(votes))]

   
#prepare output for print
output = ("\nElection Results\n"
          f"\n------------------------------'\n\n"
  f"Total Votes: {total_votes}\n"
  f"\n------------------------------'\n"
  f"Charles Casper Stockham: {css_percentage}% ({votes_dict['Charles Casper Stockham']})\n"
  f"Diana DeGette: {ddg_percentage}% ({votes_dict['Diana DeGette']})\n"
  f"Raymon Anthony Doane: {rad_percentage}% ({votes_dict['Raymon Anthony Doane']})\n"
  f"\n------------------------------\n"
  f"\nWinner: {winner}\n"
  f"\n------------------------------\n")

#print output
print(output)

#write to txtfile and save in output path
with open(output_path, "w") as txtfile: 
   txtfile.write(output)
 