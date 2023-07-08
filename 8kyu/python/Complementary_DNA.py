def DNA_strand(dna):
    str_output =''
    for i in dna:
        if i =='A':
            str_output += 'T'
        elif i =='T':
            str_output += 'A'
        elif i =='G':
            str_output += 'C'
        elif i == 'C':
            str_output += 'G'
        else:
            return output
