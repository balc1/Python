import json

class Prisoner:
    def __init__(self, first_name, last_name, crime, birth_date, entry_date, sentence):
        self.first_name = first_name
        self.last_name = last_name
        self.crime = crime
        self.birth_date = birth_date
        self.entry_date = entry_date
        self.sentence = sentence

    def __str__(self):
        return f"First Name: {self.first_name}, Last Name: {self.last_name}, Crime: {self.crime}, " \
               f"Birth Date: {self.birth_date}, Entry Date: {self.entry_date}, Sentence: {self.sentence} days"

class PrisonerEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Prisoner):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)

class PrisonInfoSystem:
    def __init__(self):
        self.prisoners = []

    def add_prisoner(self, prisoner):
        self.prisoners.append(prisoner)

    def view_prisoners(self):
        for prisoner in self.prisoners:
            print(prisoner)

    def save_prisoners(self, file_name):
        with open(file_name, 'w') as file:
            json.dump(self.prisoners, file, indent=4, cls=PrisonerEncoder)
    
    def load_prisoners(self, file_name):
        with open(file_name, 'r') as file:
            prisoners_dict = json.load(file)
            self.prisoners = [Prisoner(**prisoner_dict) for prisoner_dict in prisoners_dict]   
            
    def remove_prisoner(self, first_name, last_name):
        for prisoner in self.prisoners:
            if prisoner.first_name == first_name and prisoner.last_name == last_name:
                self.prisoners.remove(prisoner)
                print(f"Prisoner {first_name} {last_name} has been successfully removed.")
                return
        print(f"Prisoner {first_name} {last_name} not found.")
        

def main():
    prison_system = PrisonInfoSystem()
    
    
    while True:
        print("1 - Add Prisoner")
        print("2 - View Prisoners")
        print("3 - Save Prisoners")
        print("4 - Remove Prisoner")
        print("5 - Load Data")
        print("6 - Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            crime = input("Crime: ")
            birth_date = input("Birth Date: ")
            entry_date = input("Entry Date: ")
            sentence = int(input("Sentence (days): "))

            prisoner = Prisoner(first_name, last_name, crime, birth_date, entry_date, sentence)
            prison_system.add_prisoner(prisoner)

        elif choice == "2":
            prison_system.view_prisoners()

        elif choice == "3":
            file_name = input("Enter the file name to save: ")
            prison_system.save_prisoners(file_name)
            break

        elif choice == "4":
            first_name = input("Enter the first name of the prisoner to be removed: ")
            last_name = input("Enter the last name of the prisoner to be removed: ")
            prison_system.remove_prisoner(first_name, last_name)
        
        elif choice == "5":
            file_name = input("Enter the saved file name: ")
            prison_system.load_prisoners(file_name)
            
        
        elif choice == "6":
            break
        
        else:
            print("Invalid choice. Please try again.")
            

if __name__ == "__main__":
    main()
