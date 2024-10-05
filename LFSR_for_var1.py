#Функция LFSR принимает на вход инициальное значение,
# характеристический многочлен и длину необходимой последовательности

def LFSR(initial_state, polinom, text_len):
    shift = [] #Список для сдвига
    output = [] #Список, в который записывается выходной поток
    len_init = len(initial_state)
    count = -1

    #Цикл, который будет работать до момента, 
    # когда последовательность будет той же длины, что и шифруемый текст
    while count != text_len:
        #Обновление счетчика
        count += 1
        #Проверка на первое вхождение в цикл
        if count == 0:
            shift = initial_state[:]
            count += 1
        
        #Запись в выходной поток последнего бита 
        # и вызов функции для генерации крайнего левого бита
        output.append(shift[len_init-1])
        new_bit = NewBit(polinom, shift)
        # print(shift, '    ', output[-1])

        #Сдвиг каждого бита вправо
        for i in range(len_init-2, -1, -1):
            shift[i+1] = shift[i]
        
        #Запись сгенерированного бита
        shift[0] = new_bit

    output.reverse()
    # print('\n\nOutput: ', output, '\nPeriod: ', len(output))
    return output

#На вход данной функции подается многочлен, 
# для определения битов, которые будут генерировать новый 
# и текущее состояние регистра
def NewBit(polinom, shift):
    #Запись в переменную бита, 
    # который соответствует самой большой степени многочлена
    nbit = shift[polinom[0]-1]

    #Перебор битов, соответствующих каждой последующей степени многочлена 
    # и поочередная операция XOR
    for i in range(1, len(polinom)):
        nbit = nbit^shift[polinom[i]-1]

    return nbit