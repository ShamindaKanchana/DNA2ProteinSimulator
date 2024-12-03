def translation(rna_sequence):
    CODON_TO_AMINO_ACID = {
    "UUU": "Phe", "UUC": "Phe",          # Phenylalanine
    "UUA": "Leu", "UUG": "Leu",          # Leucine
    "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
    "AUU": "Ile", "AUC": "Ile", "AUA": "Ile",  # Isoleucine
    "AUG": "Met",                        # Methionine (Start Codon)
    "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",  # Valine
    "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",  # Serine
    "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",  # Proline
    "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",  # Threonine
    "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",  # Alanine
    "UAU": "Tyr", "UAC": "Tyr",          # Tyrosine
    "UAA": "Stop", "UAG": "Stop",        # Stop Codons
    "UGA": "Stop",
    "CAU": "His", "CAC": "His",          # Histidine
    "CAA": "Gln", "CAG": "Gln",          # Glutamine
    "AAU": "Asn", "AAC": "Asn",          # Asparagine
    "AAA": "Lys", "AAG": "Lys",          # Lysine
    "GAU": "Asp", "GAC": "Asp",          # Aspartic Acid
    "GAA": "Glu", "GAG": "Glu",          # Glutamic Acid
    "UGU": "Cys", "UGC": "Cys",          # Cysteine
    "UGG": "Trp",                        # Tryptophan
    "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",  # Arginine
    "AGU": "Ser", "AGC": "Ser",          # Serine
    "AGA": "Arg", "AGG": "Arg",          # Arginine
    "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"   # Glycine
    }
    amino_acid_sequence=''
    if len(rna_sequence)%3==0:
        for i in range(0,len(rna_sequence),3):
            amino_acid_sequence+=CODON_TO_AMINO_ACID[rna_sequence[i:i+3]]+'-'
        return amino_acid_sequence 
    else:
        print('Cannot convert to amino acid')
