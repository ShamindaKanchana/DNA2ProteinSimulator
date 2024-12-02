


def validation(sequence):
    valid=True
    for i in sequence:
        if i=='A' or i=='G' or i=='T' or i=='C':
            valid=True
        else:
            valid=False
            break
    if(valid):
        return True


def transcription(sequence):
    nuc={'A':'U','T':'A','G':'C','C':'G'}
    transcripted_seq=''
    for i in sequence:
        transcripted_seq+=nuc[i]
    return transcripted_seq    
        