# Функция меняет положения букв
word = "werty"
def reverseword(word):

    neword = '' # переменная в которую поместится результат
    i = 1
    while i != len(word)+1:
        neword = neword + word[i*(-1)] # умножаем на отриц. число чтоб добавлять буквы с конца
        i += 1                                     # переменой word
    return neword

print(reverseword("werty"))