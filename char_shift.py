"""Функции для сдвига латинских букв на определённое число позиций"""


def circle_char_shift(char: chr, n: int=1) -> chr:
    """Функция совершает сдвиг либо по строчным, либо по прописным буквам"""
    result = ''
    if  not chr(ord(char) + n).isalpha():
        result = chr(ord(char) + n - 26)
    else:
        result = chr(ord(char) + n)
        
    return result


def alphabet_char_shift(char: chr, n: int=1) -> chr:
    """Функция соврешает сдвиг по обоим видам букв(Z->a, z->A)"""
    #Находится в разработке

    #if char.islower():
    #     return circle_char_shift(char, n).upper()
    # else:
    #     return circle_char_shift(char, n).lower()
    
print(alphabet_char_shift('x'))
