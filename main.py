def NumProv(n):
    temp = True
    while temp == True:
        if n.isdigit():
            return int(n)
        else:
            print('Введите адекватное число, не более 32-ух')
            n = input()

def BukProv(n):
    temp = True
    while temp == True:
        n1 = n.replace(' ', '')
        n1 = n1.replace(',', '')
        n1 = n1.replace('!', '')
        n1 = n1.replace('?', '')
        n1 = n1.replace(':', '')
        n1 = n1.replace('.', '')
        if n1.isalpha():
            return n
        else:
            print('Введите адекватный текст')
            n = input()

def sdvig(tex, nu):
    t1 = ''
    for i in tex:
        if i in alf:
            t1 += alf[alf.find(i)+ nu]
        elif i in Uppalf:
            t1 += Uppalf[Uppalf.find(i)+ nu]
        elif i in alfENG:
            t1 += alfENG[alfENG.find(i)+ nu]
        elif i in UppalfENG:
            t1 += UppalfENG[UppalfENG.find(i)+ nu]
        else:
            t1 += i
    return t1


print('Шифр цезаря. Зашифруй текст!!')
yes = 'yes'
while yes == 'yes':
    text = input('Напиши текст \n')
    text = BukProv(text)
    shi = (input('нужно шифровать? или Дешифровать? shi|defshi \n')).lower()
    um = 1
    if shi == 'defshi':
        um = -1
    num = input('Укажи количество позиций сдвига текста. Число не более 32-ух \n')
    num = NumProv(num) * um
    alf = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
    Uppalf = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    alfENG = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    UppalfENG = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(sdvig(text,num))
    yes = (input('Еще будет шифрвать? yes|no \n')).lower()
