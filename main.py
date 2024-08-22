import hashlib

# A simple class to represent the voting system
class VotingSystem:
    def __init__(self):
        # Initialize candidates dictionary without predefined names
        self.candidates = {
            'A': {"name": "", "votes": 0},
            'B': {"name": "", "votes": 0},
            'C': {"name": "", "votes": 0}
        }
        self.votes = []

    def set_candidate_names(self):
        print("Please enter the names for the candidates:")
        for party in self.candidates.keys():
            candidate_name = input(f"Enter candidate name for Party {party}: ")
            self.candidates[party]["name"] = candidate_name

    def cast_vote(self, party_name):
        if party_name in self.candidates:
            vote = hashlib.sha256(party_name.encode()).hexdigest()
            self.votes.append(vote)
            print(f"Vote cast successfully for {self.candidates[party_name]['name']}!")
        else:
            print("Invalid party. Please try again.")

    def tally_votes(self):
        for vote in self.votes:
            for party, candidate_info in self.candidates.items():
                if vote == hashlib.sha256(party.encode()).hexdigest():
                    candidate_info["votes"] += 1

    def display_results(self):
        print("Election Results:")
        for party, candidate_info in self.candidates.items():
            print(f"{candidate_info['name']} (Party {party}): {candidate_info['votes']} votes")

    def run_election(self):
        print("Welcome to the Electronic Voting System")
        
        # Set candidate names at the start
        self.set_candidate_names()

        print("\nYou can vote for the following candidates:")
        for party, candidate_info in self.candidates.items():
            print(f"Party {party}: {candidate_info['name']}")
        
        while True:
            print("\nOptions:")
            print("1. Cast a vote")
            print("2. Tally votes and show results")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                party_name = input("Enter party name (A, B, C): ").upper()
                self.cast_vote(party_name)
            elif choice == "2":
                self.tally_votes()
                self.display_results()
                break
            elif choice == "3":
                print("Exiting the voting system.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    voting_system = VotingSystem()
    voting_system.run_election()
