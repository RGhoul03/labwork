from Gen_gamma import Output_stream
from Text_processing import Text_to_bit

def Encryption(Text):
    #Переводим текст в биты. Генерируем ключ шифрования
    Open_text = Text_to_bit(Text)
    Gamma = Output_stream(len(Open_text))

    #Выполняем побитовый XOR для получения зашифрованного текста
    Cipher_text = []
    for i in range(len(Open_text)):
        Cipher_text.append(Open_text[i]^Gamma[i])

    Cipher_text = ''.join(map(str, Cipher_text))
    print(Open_text, '\n', Gamma, '\n', Cipher_text, '\n\n')
    return Cipher_text

Text = str(input('Input your text: '))
Cipher_text = Encryption(Text)

print('Cipher_text: ', Cipher_text)