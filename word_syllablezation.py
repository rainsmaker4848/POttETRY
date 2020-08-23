from russtress import Accent
import vow_count as one
def w_syll(word):
    accent = Accent()
    accented_text = accent.put_stress(word)
    accented_text=accented_text.rsplit(None, 1)[-1]
    vow_1 = accented_text.find('\'')
    if vow_1==-1 :  
        vow_1=1
    return (vow_1, one.vow_c(word))