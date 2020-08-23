import word_syllablezation as one
import random
import num2t4ru as two
import tensorflow as tf
def dig_c(word, count, previous):
    stress1,syll1 = one.w_syll(word)
    if count != 0:
        syll1 = syll1+count-1
        stress1 = stress1+count-1
    buff1 = buff2 = previous
    if syll1 == 1: #однослоговые числа
        buff1 = random.choice([0,2,3,5,6,7,100])
        if (buff1 == previous):
              buff1 = random.choice([0,2,3,5,6,7,100])
        return(buff1)
    else:
        for number in range(20): #переборчик (топорно)
            st_num = two.num2text(number)
            stress2,syll2 = one.w_syll(st_num)
            #print(stress1, syll1)
            if stress2 == stress1 and syll2 == syll1 and number!=previous:
                return(number)
            else:
                if(syll2 == syll1 and number != previous): 
                    buff1=number
                if(stress2 == stress1):
                    buff2 = number
        if (buff1 != -1): #Количество слогов важнее! Чтоб не нарушать ритм!
            return(buff1)
        else:
            if buff2 < 0 or buff2 == previous:
                buff2 = random.randint(0,200) #Такого не бывало, но вдруг...
            return(buff2)

