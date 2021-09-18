#1
def anagram_number(number):
    begin_number = number
    reversed_num = 0
    if number==0:
        return True
    else:
        while number !=0:
            digit = number % 10
            reversed_num = reversed_num * 10 + digit
            number //= 10
        if reversed_num == begin_number:
            return True
        else:
            return False
#2
def roman_to_int(s):
    translations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = 0
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    for char in s:
        number += translations[char]
    return number