def to_rna(dna_strand):
    #Being dna_strand a full str without spaces nor other symbols
    return dna_strand.translate(str.maketrans("GCTA", "CGAU"))