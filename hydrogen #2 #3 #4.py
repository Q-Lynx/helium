import random
#Heads or tails
def heads_or_tails():
    rzut = ["head", "tail"]
    wynik = random.choice(rzut)
    print(wynik)

#Temperature Converter
def convert_temperature():
    odpowiedz2 = input("Do you want to convert temperature? ")
    if odpowiedz2("yes"):
        zgoda = input("Celcius to Kelvin or Kelvin to Celcius? ")
        if zgoda("Celcius to Kelvin"):
            temperatura_w_celcjuszach = input("Write the value. ")
            kelvin = temperatura_w_celcjuszach + 273, 15
            print(kelvin)
        elif zgoda("Kelvin to Celcius"):
            temperatura_w_kelvinach = input("Write the value. ")
            celcjusz = temperatura_w_kelvinach - 273, 15
            print(celcjusz)
    input("Fahrenheits? Fahrenheits? Who the fck cares about Fahrenheits?")
    if odpowiedz2("no"):
        age_in_seconds()

#Age in seconds
def age_in_seconds():
    wiek = input("How old are you?")
    sekundy = wiek*365*24*60*60
    print("No, you're ", sekundy," seconds old")


print("Hello, I need to interrupt you. Sorry, I know that you might be busy but... \n I just need to do my homework.")
odpowiedz = input("Do you want to flip a coin? ")
if odpowiedz("yes"):
    heads_or_tails()
if odpowiedz("no"):
    convert_temperature()
input("Goodbye you old looser")
