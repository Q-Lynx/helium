import random
import string
def tworz_imie():
    number = random.randint(2, 22)
    upper_alphabet = string.ascii_uppercase
    imie = [random.choice(upper_alphabet)]
    while number > 0:
        lower_alphabet = string.ascii_lowercase
        imie.extend(random.choice(lower_alphabet))
        number -=1
    else:
        print("".join(imie))
tworz_imie()
input("Python, czemu mnie nienawidzisz")

