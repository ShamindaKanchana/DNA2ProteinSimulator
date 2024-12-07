import tkinter as tk
from transcription import validation, transcription
from translation import translation
from visualization import visualize_seq  

root = tk.Tk()
root.geometry("500x500")
root.title("DNA2Protein Simulator")

# GUI Components
label = tk.Label(root, text="Enter DNA sequence", font=('Arial', 18))
label.pack(padx=40, pady=20)

textbox = tk.Text(root, height=3, width=40, font=('Arial', 15))
textbox.pack()


nucleotide_colors = {"A": "red", "T": "blue", "G": "green", "C": "yellow"}

result_label = tk.Label(root, text="", font=('Arial', 12), fg="blue", wraplength=400)
result_label.pack(pady=20)

def process_input():
    user_input = textbox.get("1.0", tk.END).strip().upper()

    if validation(user_input):
       
        rna_sequence = transcription(user_input)
        amino_acid_sequence = translation(rna_sequence)
        result_label.config(text=f"RNA: {rna_sequence}\nProtein: {amino_acid_sequence}")

      
    else:
        result_label.config(text="Invalid DNA sequence!")

def dna_process_visualize():
    user_input = textbox.get("1.0", tk.END).strip().upper()
    visualize_seq(user_input, nucleotide_colors)

    

submit = tk.Button(root, text="Submit", font=('Arial', 10), command=process_input)
submit.pack()

visualize= tk.Button(root, text="Visualize", font=('Arial', 10), command=dna_process_visualize)
visualize.pack()

root.mainloop()
