def Text_to_bit(Text):
    char_list = list(Text)
    
    code = []
    #Перебор каждого символа текста. 
    # Сначала символ переводится в десятичное значение ASCII кода. 
    # Затем десятичное значение трансформируется в двоичное 
    # и дополняется до 8ми битового представления нулями слева.
    for i in range(len(char_list)):
        code.append(ord(char_list[i]))
        code[i] = bin(code[i])[2:].zfill(8)
    
    #Здесь перебирается каждое 8ми битное значение, разбивается на биты 
    # и трансформируется из строки в число
    bits = [int(char) for binary in code for char in binary]
    
    return bits