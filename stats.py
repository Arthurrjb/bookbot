def get_num_words(text):
    palavras=text.split()
    num_words=len(palavras)
    return num_words

def get_num_char(text):
    dic_letra_num={}
    text_letters=set()
    minusculas=text.lower()
    for char in minusculas:
        if char.isalpha():
            text_letters.add(char)
    for char in text_letters:
        n = minusculas.count(char)
        dic_letra_num.update({char:n})
    return dic_letra_num

def sort_dict(dic_letra_num):
    lista_dict = []
    for char in dic_letra_num:
        lista_dict.append({"char":char,"num":dic_letra_num[char]})
    # lista_dict.sort(reverse=True,key=lista_dict['num'])
    lista_dict.sort(reverse=True, key=sort_on)
    for dict in lista_dict:
        print(f"{dict['char']}: {dict['num']}")

def sort_on(items):
    return items["num"]