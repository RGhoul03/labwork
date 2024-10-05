from LFSR_for_var1 import LFSR
import random

#Данная функция обрабатывает выходные потоки каждого РСЛОС 
# для формирования гамма последовательности

def Output_stream(text_len):
    #Генерация инициальных значений длиной 80 бит
    in_st1 = generate_binary_list()
    in_st2 = generate_binary_list()

    #Если инициальные состояния одинаковы, 
    # то второе инициальное состояние будет генерироваться 
    # пока не станет отличным от первого
    if in_st1 == in_st2:
        while in_st1 == in_st2:
            in_st2 = generate_binary_list()
    
    polinom1 = [80, 9, 4, 2]
    polinom2 = [80, 5, 3, 2, 1]

    #Генерация последовательностей нужной длины
    LFSR1 = LFSR(in_st1, polinom1, text_len)
    LFSR2 = LFSR(in_st2, polinom2, text_len)

    Gamma = []

    #Генерация двух битов для первого такта
    bit1 = random.randint(0,1)
    bit2 = random.randint(0,1)

    Len = len(LFSR1)
    #Побитовое вычисление гамма потока по схеме.
    for i in range(Len):
        AND = bit1&bit2
        XOR = LFSR1[i]^LFSR2[i]^AND
        Gamma.append(XOR)
        bit2 = bit1
        bit1 = XOR

    Gamma.reverse()
    return Gamma

def generate_binary_list():
    # Генерируем список из 0 и 1
    binary_list = [random.choice([0, 1]) for i in range(80)]
    
    # Проверяем, чтобы в списке были хотя бы один 1
    if sum(binary_list) == 0:
        # Если нет 1, то заменяем случайный элемент на 1
        binary_list[random.choice([0, 1])] = 1
    
    return binary_list