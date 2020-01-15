from string import ascii_lowercase as alphabet

name1 = input("Write your name. ")
name2 = input("Write name of your love ")

def calculate(name):
    result = 0
    wynik = 0
    wynik2 = 0
    for letter in name:
        number = alphabet.index(letter) + 1
        result += number
    if result >= 10:
        for element in str(result):
            element = int(element)
            wynik += element
            if wynik >= 10:
                for element2 in str(wynik):
                    element2 = int(element2)
                    wynik2 += element2
                    print(wynik2)
            if wynik < 10:
                print(wynik)

calculate(name1)

calculate(name2)
