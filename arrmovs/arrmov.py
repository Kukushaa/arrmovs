"""
This is module, that can help you convert your INT num into Array (and on the contrary)

There is 18 modules (main)

Enjoy

----------------------------------------------------------------------------------------------
Facebook: https://www.facebook.com/nika.beridze15
Instagram: https://www.instagram.com/nikaa_beroo
GitHub: https://github.com/Kukushaa
StackOverFlow: https://stackoverflow.com/users/19145314/kukushaa

Telegarm: @raigetsu
----------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------
NIKA BERIDZE 2022®
KUKUSHAA®
----------------------------------------------------------------------------------------------
"""

#Importing some modules
import random as rd
import math

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

def ListErr(value):
    if type(value) != list:
        raise NumNotInt("Enter only List")

    else:
        pass

def NumError(value):
    if type(value) != int:
        raise NumNotInt("Enter only INT num")

    else:
        pass

def ModuleSetError(value):
    raise ModuleSetError("Only list or INT")

#----------------------------------------------------------------------------------------------

#Main modules

def IntToArr(num: int):
    """
    With this module, you can conver your INT num to Array

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
    With this module, you can conver your INT num to Array and Sort it.

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
    With this module, you can conver your INT num to Array and Sort it Reversed.

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
    With this module, you can conver your INT num to Array and return only ODD nums.

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
        With this module, you can conver your INT num to Array and return only EVEN nums.

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

def IntToArrBiggest(num: int):
    """
        With this module, you return biggest num in your int (by converting into array).

        examle:
            import arrmov as arr

            num = 1234567
            print(arr.IntToArrBiggest(num))


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

def IntToArrSmaller(num: int):
    """
        With this module, you return Smallest num in your int (by converting into array).

        examle:
            import arrmov as arr

            num = 012345
            print(arr.IntToArr(num))


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
        With this module, you can generate random Array, from (fr) to int num you want (to)

        examle:
            import arrmov as arr

            print(arr.IntToArrRandom(1, 5))


        Output:
            [4, 3, 3]

        """
    if fr == 0:
        raise NoZeroEntry("Invaid Entry: {g}".format(g = fr))
    else:
        pass

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

def IntToArrYourNum(num: int, fig: int):
    """
        With this module, you can return your amount of num (fig) in your int

        examle:
            import arrmov as arr

            num = 123125312
            print(arr.IntToArrYourNum(num, 1))


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
        With this module, you can conver your INT num to Array and return every single nums factorial in this Array

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
        With this module, you can conver your INT num to Array and return choosen num's factorial in this Array

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
        With this module, you can generate random Array and return array INT's factorial

        examle:
            import arrmov as arr

            print(arr.IntToArrFactorialRand(1, 4))


        Output:
            [24, 6, 6, 6, 24, 6, 2, 24, 6, 6]

        """
    if fr == 0:
        raise NoZeroEntry("Invaid Entry: 0")
    else:
        pass

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
        With this module, you can conver your Array to INT

        examle:
            import arrmov as arr

            array = [1, 2, 3, 4, 5]
            print(arr.ArrToInt(array))


        Output:
            12345

        """
    ListErr(arr)

    if arr[0] == 0:
        del arr[0]

    else:
        pass

    tmp = ''

    for i in arr:
        tmp = tmp + str(i)

    return tmp

def ArrToIntSort(arr: list):
    """
        With this module, you can conver your Array to INT and sort it

        examle:
            import arrmov as arr

            array = [3, 2, 9, 0, 7]
            print(arr.ArrToIntSort(array))


        Output:
            02379

        """
    ListErr(arr)

    tmp = ''

    arr.sort()

    if arr[0] == 0:
        del arr[0]

    else:
        pass

    for i in arr:
        tmp = tmp + str(i)

    return tmp

def ArrToIntBiggest(arr: list):
    """
        With this module, you can conver your Array to INT and return biggest INT

        examle:
            import arrmov as arr

            array = [3, 2, 9, 0, 7]
            print(arr.ArrToIntBiggest(array))


        Output:
            9

        """
    ListErr(arr)

    arr.sort(reverse=True)

    return arr[0]

def Converter(num):
    """
        With this module, you can convert your INT to Array or on the contrary, it doesn't matter

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

def Biggest(num):
    """
        With this module, you can conver your INT num to Array

        examle:
            import arrmov as arr

            num = 4395
            print(arrmov.IntToArr(num)


        Output:
            [4, 3, 9, 5]

        """
    if type(num) == list:
        return ArrToIntBiggest(num)

    elif type(num) == int:
        return IntToArrBiggest(num)

    else:
        raise ModuleSetError(num)