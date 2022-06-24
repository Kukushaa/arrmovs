"""
This is a module, that can help you convert your INT num into an Array (and on the contrary)

There are 22 modules (main)

Enjoy

----------------------------------------------------------------------------------------------
Facebook: https://www.facebook.com/nika.beridze15
Instagram: https://www.instagram.com/nikaa_beroo
GitHub: https://github.com/Kukushaa
StackOverFlow: https://stackoverflow.com/users/19145314/kukushaa

Telegram: @raigetsu
----------------------------------------------------------------------------------------------
0.0.3 Version Changes:

TecnicalImprovements():
    0

ModuleChangeName():
    0

NewModules():
    1. __version__() --> print's version of your arrmovs
    
    2. help() --> Help menu

    3. StrToArr() --> You can return only numbers with an array from a text -->
    and you can choose what kind of type it can be (int or float)

    4. StrToArrFromFile() --> You can return only numbers with an array from a file text -->
    and you can choose what kind of type it can be (int or float)

----------------------------------------------------------------------------------------------
NIKA BERIDZE 2022®
KUKUSHAA®
BATUMI®
----------------------------------------------------------------------------------------------
"""

#Importing some modules
import random as rd
import math
import re

#----------------------------------------------------------------------------------------------

#Classes for Error message
class NumNotInArr(ValueError):
    pass

class NoZeroEntry(ValueError):
    pass

class NumNotInt(ValueError):
    pass

class ListNotList(ValueError):
    pass

class ModuleSetError(ValueError):
    pass

def ListErr(value: list):
    value.sort()

    while value[0] == 0:
        del value[0]

    if type(value) != list:
        raise NumNotInt("Enter only List")

    else:
        pass

    return 0

def NumError(value):
    if type(value) != int:
        raise NumNotInt("Enter only INT num")

    else:
        pass

    return 0

def ToBigFrom(fr: int, to: int):
    if fr > to:
        raise SyntaxError(f"{fr} is bigger than {to}")

    if fr == 0:
        raise NoZeroEntry("Invaid Entry: 0")

    else:
        pass

    return 0

def ModuleSetError(value):
    raise ModuleSetError("Only list or INT")

#----------------------------------------------------------------------------------------------

#version Case

version = '0.0.3'

#Main modules

def IntToArr(num: int):
    """
        With this module, you can convert your INT num to Array

        examle:
            import arrmov as arr

            num = 4395
            print(arr.IntToArr(num))


        Output:
            [4, 3, 9, 5]

    """

    NumError(num)

    split = [i for i in str(num)]
    array = []

    for i in split:
        for j in i.split():
            array.append(int(j))

    return array

def IntToArrSorted(num: int):
    """
        With this module, you can convert your INT num to Array and Sort it.

        examle:
            import arrmov as arr

            num = 12345
            print(arr.IntToArrSortedReverse(num))


        Output:
            [1, 2, 3, 4, 5]

    """

    NumError(num)

    split = [i for i in str(num)]
    array = []

    for i in split:
        for j in i.split():
            array.append(int(j))

    array.sort()

    return array

def IntToArrSortedReverse(num: int):
    """
        This module can convert your INT num to Array and Sort it Reverse.

        examle:
            import arrmov as arr

            num = 12345
            print(arr.IntToArrSortedReverse(num))


        Output:
            [5, 4, 3, 2, 1]

    """

    NumError(num)

    split = [i for i in str(num)]
    array = []

    for i in split:
        for j in i.split():
            array.append(int(j))

    array.sort(reverse=True)

    return array

def IntToArrOdd(num: int):
    """
        This module can convert your INT num to Array and return only ODD nums.

        examle:
            import arrmov as arr

            num = 1234554321
            print(arr.IntToArrOdd(num))


        Output:
            [1, 3, 5, 5, 3, 1]

    """

    NumError(num)

    split = [i for i in str(num)]
    array = []

    for i in split:
        for j in i.split():
            array.append(int(j))

    array.sort()

    odd = []

    for i in array:
        if i % 2 != 0:
            odd.append(i)
        else:
            pass

    return odd

def IntToArrEven(num: int):
    """
        With this module, you can convert your INT num to Array and return only EVEN nums.

        examle:
            import arrmov as arr

            num = 23456
            print(arr.IntToArr(num))


        Output:
            [2, 4, 6]

    """

    NumError(num)

    split = [i for i in str(num)]
    array = []

    for i in split:
        for j in i.split():
            array.append(int(j))

    array.sort()

    even = []

    for i in array:
        if i % 2 != 0:
            even.append(i)
        else:
            pass

    return even

def IntBiggestNum(num: int):
    """
        With this module, you return the biggest num in your int (by converting it into an array).

        examle:
            import arrmov as arr

            num = 1234567
            print(arr.IntBiggestNum(num))


        Output:
            7

    """

    NumError(num)

    split = [i for i in str(num)]
    array = []

    for i in split:
        for j in i.split():
            array.append(int(j))

    array.sort(reverse=True)

    first = array[:1]

    tmp = ''

    for i in first:
        tmp = tmp + str(i)

    biggest = int(tmp)

    return biggest

def IntSmallestNum(num: int):
    """
        With this module, you return the Smallest num in your int (by converting it into an array).

        examle:
            import arrmov as arr

            num = 012345
            print(arr.IntSmallestNum(num))


        Output:
            0

    """

    NumError(num)

    split = [i for i in str(num)]
    array = []

    for i in split:
        for j in i.split():
            array.append(int(j))

    array.sort(reverse=False)

    first = array[:1]

    tmp = ''

    for i in first:
        tmp = tmp + str(i)

    smaller = int(tmp)

    return smaller

def IntToArrRandom(fr: int, to: int):
    """
        With this module, you can generate a random Array, from (fr) to int num you want (to)

        examle:
            import arrmov as arr

            print(arr.IntToArrRandom(1, 5))


        Output:
            [4, 3, 3]

    """

    ToBigFrom(fr, to)

    num = ''

    for i in range(rd.randint(1, 10)):
        try:
            tmp = rd.randint(fr, to)
        except ValueError:
            raise ValueError("Second INT > first INT")
        else:
            pass
        num = str(tmp) + num

    split = [i for i in str(num)]
    array = []

    for i in split:
        for j in i.split():
            array.append(int(j))

    return array

def IntNumCount(num: int, fig: int):
    """
        With this module, you can return your amount of num (fig) in your int

        examle:
            import arrmov as arr

            num = 123125312
            print(arr.IntNumCount(num, 1))


        Output:
            3

    """

    NumError(num)

    split = [i for i in str(num)]
    array = []

    for i in split:
        for j in i.split():
            array.append(int(j))

    return array.count(fig)

def IntToArrFactorial(num: int):
    """
        With this module, you can convert your INT num to Array and return every single num factorial in this Array

        examle:
            import arrmov as arr

            num = 4395
            print(arr.IntToArrFactorial(num))


        Output:
            [24, 6, 362880, 120]

    """

    NumError(num)

    split = [i for i in str(num)]
    array = []

    for i in split:
        for j in i.split():
            array.append(int(j))

    for i in array:
        tmp = math.factorial(i)
        index = array.index(i)

        array[index] = tmp

    return array

def IntToArrFactorialNum(num: int, fact: int):
    """
        With this module, you can convert your INT num to Array and return the chosen num's factorial in this Array

        examle:
            import arrmov as arr

            num = 4395
            print(arr.IntToArrFactorialNum(num))


        Output:
            [24, 3, 9, 5]

    """

    NumError(num)

    split = [i for i in str(num)]
    array = []

    for i in split:
        for j in i.split():
            array.append(int(j))

    if fact not in array:
        raise NumNotInArr(fact)

    else:
        tmp = math.factorial(fact)
        index = array.index(fact)

        array[index] = tmp

    return array

def IntToArrFactorialRand(fr: int, to: int):
    """
        With this module, you can generate a random Array and return the array INT's factorial

        examle:
            import arrmov as arr

            print(arr.IntToArrFactorialRand(1, 4))


        Output:
            [24, 6, 6, 6, 24, 6, 2, 24, 6, 6]

    """

    ToBigFrom(fr, to)

    num = ''

    for i in range(rd.randint(1, 10)):
        tmp = rd.randint(fr, to)
        num = str(tmp) + num

    split = [i for i in str(num)]
    array = []

    for i in split:
        for j in i.split():
            array.append(int(j))

    for i in array:
        tmp = math.factorial(i)
        index = array.index(i)
        array[index] = tmp

    return array

def IntSum(num: int):
    """
        With this module, you can SUM your INT numbers

        examle:
            import arrmov as arr

            num = 4395
            print(arr.IntSum(num))


        Output:
            21

        4 + 3 + 9 + 5 = 21
    """

    NumError(num)

    split = [i for i in str(num)]
    array = []

    for i in split:
        for j in i.split():
            array.append(int(j))

    return sum(array)

def ArrToInt(arr: list):
    """
        With this module, you can convert your Array to INT

        examle:
            import arrmov as arr

            array = [1, 2, 3, 4, 5]
            print(arr.ArrToInt(array))


        Output:
            12345

    """

    ListErr(arr)

    tmp = ''

    for i in arr:
        tmp = tmp + str(i)

    return tmp

def ArrToIntSort(arr: list):
    """
        With this module, you can convert your Array to INT and sort it

        examle:
            import arrmov as arr

            array = [3, 2, 9, 0, 7]
            print(arr.ArrToIntSort(array))


        Output:
            02379

    """

    ListErr(arr)

    tmp = ''

    for i in arr:
        tmp = tmp + str(i)

    return tmp

def ArrBiggestNum(arr: list):
    """
        With this module, you can find the biggest num in your Array

        examle:
            import arrmov as arr

            array = [3, 2, 9, 0, 7]
            print(arr.ArrBiggestNum(array))


        Output:
            9

    """

    ListErr(arr)

    arr.sort(reverse=True)

    return arr[0]

def ArrSmallestNum(arr: list):
    """
        With this module, you can convert your Array to INT and return the most significant INT

        examle:
            import arrmov as arr

            array = [3, 2, 9, 0, 7]
            print(arr.ArrSmallestNum(array))


        Output:
            9

    """

    ListErr(arr)

    arr.sort()

    return arr[0]

def ArrNumCount(arr: list, num: int):
    """
        With this module, you can count in your Array your number

        examle:
            import arrmov as arr

            array = [3, 2, 9, 0, 7, 2, 2]
            print(arr.ArrNumCount(array, 2))


        Output:
            3

    """

    return arr.count(num)

def RandomArr(numlen: int, fr: int, to: int):
    """
        With this module, you can generate a random Array, in the len of your first written num

        examle:
            import arrmov as arr

            print(arr.RandomArr(5, 1, 10))


        Output:
            [5, 2, 6, 1, 4]

    """

    ToBigFrom(fr, to)

    arr = []

    for i in range(numlen):
        arr.append(rd.randint(fr, to))

    return arr

def StrToArr(text: list, value_enter: str):
    """
        With this module, you can read only numbers with an array from a text
        value_enter --> with this value, you can choose what kinds of type of numbers you want (int or float)

        examle:
            import arrmov as arr

            print(arr.StrToArr("This Is my 24 and 25.0 text"))

        Output:
            [24, 25]

    """

    value = 0

    if value_enter.lower() == "None":
        value = 0

    elif value_enter.lower() == "int":
        value = 0

    elif value_enter.lower() == "float":
        value = 0.0
    
    else:
        raise ValueError("Invalid value!")

    type_value = type(value)

    arr = []
    
    for i in re.findall(r'-?\d+\.?\d*', text):
        arr.append(type_value(float(i)))

    return arr

def StrToArrFromFile(filename: str, value_enter: str):
    """
        With this module, you can return only numbers with an array from a file text
        value_enter --> with this value, you can choose what kinds of type of numbers you want (int or float)

        examle:
            import arrmov as arr

            print(arr.StrToArrFromFile("myfile.txt", "int"))

        Output:
            [24, 25]

    """

    value = 0

    if value_enter.lower() == "None":
        value = 0

    elif value_enter.lower() == "int":
        value = 0

    elif value_enter.lower() == "float":
        value = 0.0
    
    else:
        raise ValueError("Invalid value!")
    
    type_value = type(value)

    try:
        with open(filename, 'r') as file:
            text = file.read()

    except FileNotFoundError:
        raise FileNotFoundError("Sorry, but file can't finded")
        
    arr = []

    for i in re.findall(r'-?\d+\.?\d*', text):
        arr.append(type_value(float(i)))

    return arr

def Converter(num):
    """
        With this module, you can convert your INT to Array, or on the contrary, it doesn't matter

        examle:
            import arrmov as arr

            array = [3, 2, 9, 0, 7]
            print(arr.Converter(array))

            number = 123456
            print(arr.Converter(number))


        Output:
            02379

    """

    if type(num) == list:
        return ArrToInt(num)

    elif type(num) == int:
        return IntToArr(num)

    else:
        raise ModuleSetError(num)

    return 0

def Biggest(num):
    """
        With this module, you can convert your INT num to Array

        examle:
            import arrmov as arr

            num = 4395
            print(arrmov.IntToArr(num)


        Output:
            [4, 3, 9, 5]

    """

    if type(num) == list:
        return ArrBiggestNum(num)

    elif type(num) == int:
        return IntBiggestNum(num)

    else:
        raise ModuleSetError(num)

    return 0

def help():
    text = "-----HELP MENU-----\n" \
            "\n" \
            "If you want to see all modules, CTRL/Command + Left Click on 'arrmovs', which is on (import arrmovs)\n"\
            "With this module, you can convert your INT to Array or on the contrary\n"\
            "For better information, visit our GITHUB repository: https://github.com/Kukushaa/arrmovs/blob/main/arrmovs/__init__.py \n"\
            "\n-----END OF HELP-----"

    return text

def __version__():
    return f'Version of arrmovs: {version}'