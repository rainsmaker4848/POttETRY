import pymorphy2
import vow_count as one
morph = pymorphy2.MorphAnalyzer()
def smth_prove(word):
    prove = morph.parse(word)[0]
    if (prove.tag.POS == 'NPRO' or prove.tag.POS == 'PREP' or prove.tag.POS == 'CONJ' or prove.tag.POS == 'PRCL' or prove.tag.POS == 'INTJ'):
        return(one.vow_c(word), 0)
    if (prove.tag.POS == 'NUMR'):
        return (0, 1)
    return(0, 0)