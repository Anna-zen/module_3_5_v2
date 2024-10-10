

def get_multiplied_digits(number):
    # Преобразуем число в строку для удобства обработки
    str_number = str(number)

    if len(str_number) > 1:
        first = int(str_number[0])
        #print (first)

        return first * get_multiplied_digits(int(str_number[1:]))


    else:
        first = int(str_number[0])
        if first > 0:
            return first
        else :
            print (' В этом шаге умножение на 0, игнорируем 0')
            first = 1
            return first




result = get_multiplied_digits ( 40000020 )

print(result)

