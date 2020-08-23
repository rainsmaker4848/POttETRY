import digital_comparing as one
import trash_prove as two
import num2t4ru as three
def separator(f_name):
    f_input = open(f_name, "r")
    f_output = open(f_name[:-4]+'_digitalized.txt', "w")
    list1=list()
    previous=-1
    number = 0 
    connect_count = 0
    for line in f_input:
        list1 = line.split()  
        for number in range(len(list1)):
            if list1[number] in '-,.!?;:': #учет знаков препинания
                f_output.write(list1[number]+' ')  
            else:
                trash,num=two.smth_prove(list1[number]) #узнаем, что за штучечка
                if (num==1): #Если числительное
                    f_output.write(list1[number] +' ') #выписываем число
                else:
                    if len(list1[number]) <  3 and trash!=0 and (list1[number][0].isupper()==False and list1[number][0] in 'уеоаыэяию'): #проверка на частицы (что не влияют на ритмику (не считаем их ударения))
                        connect_count = connect_count + trash
                    else:       
                        f_output.write(three.num2text(one.dig_c(list1[number], connect_count, previous))+' ') #Это обычное слово, просто подберем рифмованное число
                        previous = one.dig_c(list1[number], connect_count, previous)
                        print(previous)
                        connect_count = 0 #сбрасываем счетчик несчитаемых слогов
        f_output.write('\n')            
    f_input.close()
    f_output.close()
    return ('excellent work')

print(separator('bla.txt')) 