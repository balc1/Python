import json
import tkinter as tk
from tkinter import messagebox

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

    def main(self):
        root = tk.Tk()
        root.title("Prison Information System")
        def add_prisoner_from_input():
            first_name = entry_first_name.get()
            last_name = entry_last_name.get()
            crime = entry_crime.get()
            birth_date = entry_birth_date.get()
            entry_date = entry_entry_date.get()
            sentence = int(entry_sentence.get())

            prisoner = Prisoner(first_name, last_name, crime, birth_date, entry_date, sentence)
            self.add_prisoner(prisoner)
            update_prisoner_listbox()

        def view_prisoners_from_input():
            text_prisoners.delete("1.0", tk.END)
            for prisoner in self.prisoners:
                text_prisoners.insert(tk.END, f"{prisoner}\n")

        def save_prisoners_from_input():
            file_name = entry_file_name.get()
            self.save_prisoners(file_name)
            messagebox.showinfo("Save Prisoners", "Prisoners saved successfully.")

        def remove_prisoner_from_input():
            first_name = entry_remove_first_name.get()
            last_name = entry_remove_last_name.get()
            self.remove_prisoner(first_name, last_name)
            update_prisoner_listbox()
            messagebox.showinfo("Remove Prisoner", f"Prisoner {first_name} {last_name} has been successfully removed.")

        def load_prisoners_from_input():
            file_name = entry_file_name.get()
            self.load_prisoners(file_name)
            update_prisoner_listbox()
            messagebox.showinfo("Load Prisoners", "Prisoners loaded successfully.")

        def update_prisoner_listbox():
            listbox_prisoners.delete(0, tk.END)
            for prisoner in self.prisoners:
                listbox_prisoners.insert(tk.END, f"{prisoner.first_name} {prisoner.last_name}")

        root = tk.Tk()
        root.title("Prison Information System")

        frame_main = tk.Frame(root)
        frame_main.pack(padx=20, pady=20)

        label_file_name = tk.Label(frame_main, text="Enter the saved file name:")
        label_file_name.grid(row=0, column=0)
        entry_file_name = tk.Entry(frame_main)
        entry_file_name.grid(row=0, column=1)

        button_load_prisoners = tk.Button(frame_main, text="Load Prisoners", command=load_prisoners_from_input)
        button_load_prisoners.grid(row=0, column=2)

        frame_add_prisoner = tk.Frame(frame_main)
        frame_add_prisoner.grid(row=1, column=0, columnspan=3, pady=10)

        label_first_name = tk.Label(frame_add_prisoner, text="First Name:")
        label_first_name.grid(row=0, column=0)
        entry_first_name = tk.Entry(frame_add_prisoner)
        entry_first_name.grid(row=0, column=1)

        label_last_name = tk.Label(frame_add_prisoner, text="Last Name:")
        label_last_name.grid(row=0, column=2)
        entry_last_name = tk.Entry(frame_add_prisoner)
        entry_last_name.grid(row=0, column=3)

        label_crime = tk.Label(frame_add_prisoner, text="Crime:")
        label_crime.grid(row=1, column=0)
        entry_crime = tk.Entry(frame_add_prisoner)
        entry_crime.grid(row=1, column=1)

        label_birth_date = tk.Label(frame_add_prisoner, text="Birth Date:")
        label_birth_date.grid(row=1, column=2)
        entry_birth_date = tk.Entry(frame_add_prisoner)
        entry_birth_date.grid(row=1, column=3)

        label_entry_date = tk.Label(frame_add_prisoner, text="Entry Date:")
        label_entry_date.grid(row=2, column=0)
        entry_entry_date = tk.Entry(frame_add_prisoner)
        entry_entry_date.grid(row=2, column=1)

        label_sentence = tk.Label(frame_add_prisoner, text="Sentence (days):")
        label_sentence.grid(row=2, column=2)
        entry_sentence = tk.Entry(frame_add_prisoner)
        entry_sentence.grid(row=2, column=3)

        button_add_prisoner = tk.Button(frame_add_prisoner, text="Add Prisoner", command=add_prisoner_from_input)
        button_add_prisoner.grid(row=3, column=0, columnspan=4)

        button_view_prisoners = tk.Button(frame_main, text="View Prisoners", command=view_prisoners_from_input)
        button_view_prisoners.grid(row=3, column=0)

        button_save_prisoners = tk.Button(frame_main, text="Save Prisoners", command=save_prisoners_from_input)
        button_save_prisoners.grid(row=3, column=1)

        frame_remove_prisoner = tk.Frame(frame_main)
        frame_remove_prisoner.grid(row=4, column=0, columnspan=3, pady=10)

        label_remove_first_name = tk.Label(frame_remove_prisoner, text="Enter the first name of the prisoner to be removed:")
        label_remove_first_name.grid(row=0, column=0)
        entry_remove_first_name = tk.Entry(frame_remove_prisoner)
        entry_remove_first_name.grid(row=0, column=1)

        label_remove_last_name = tk.Label(frame_remove_prisoner, text="Enter the last name of the prisoner to be removed:")
        label_remove_last_name.grid(row=0, column=2)
        entry_remove_last_name = tk.Entry(frame_remove_prisoner)
        entry_remove_last_name.grid(row=0, column=3)

        button_remove_prisoner = tk.Button(frame_remove_prisoner, text="Remove Prisoner", command=remove_prisoner_from_input)
        button_remove_prisoner.grid(row=1, column=0, columnspan=4)

        listbox_prisoners = tk.Listbox(frame_main, width=60)
        listbox_prisoners.grid(row=5, column=0, columnspan=3, pady=10)

        scrollbar = tk.Scrollbar(frame_main, orient=tk.VERTICAL)
        scrollbar.grid(row=5, column=3, pady=10, sticky="ns")
        listbox_prisoners.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox_prisoners.yview)

        text_prisoners = tk.Text(frame_main, width=60, height=10)
        text_prisoners.grid(row=7, column=0, columnspan=3, pady=10)

        root.mainloop()

if __name__ == "__main__":
    prison_system = PrisonInfoSystem()
    prison_system.main()