def extra_letter(a, b):
    dic = {} #словарь
    for num in b:
        if num in dic: # подсчитываем сколько раз встретилась буква в строке b
            dic[num] += 1
        else:
            dic[num] = 1
    for rub in a:  # удаляем все совпадающие буквы со строкой a
        if rub in dic:
            dic[rub] -= 1
    for char in dic:  # вывод той самой буквы
        if dic[char] > 0:
            return char
