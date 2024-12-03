from transcription import validation,transcription
from translation import translation
user_input=input("Enter a DNA sequence:").upper()

if validation(user_input):
    print("This is a valid sequence")
    rna_sequence=transcription(user_input)
    print('RNA sequence is '+rna_sequence)
    amino_acid_sequence=translation(rna_sequence)
    print('Aminno  sequence is '+amino_acid_sequence)
else:
    print("This is invalid sequence")    
    
 