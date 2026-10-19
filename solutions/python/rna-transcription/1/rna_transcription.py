def to_rna(dna_strand):
    rna = ""
    for nucleotide in dna_strand:
        if nucleotide == "G":
            rna += "C"
        if nucleotide == "C":
            rna += "G"
        if nucleotide == "T":
            rna += "A"
        if nucleotide == "A":
            rna += "U"
    return rna