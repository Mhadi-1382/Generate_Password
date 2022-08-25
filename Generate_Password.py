
# Generate Password
# Built by Mahdi Rabiee
# Created: Sunday, August 7, 2022


from colorama import Fore
import random
import os


# Clear Screen
os.system("cls")


# Splash Screen
SplashScreen = """
    ::::
    :::   G E N E R A T E   P A S S W O R D
    ::
"""
print(Fore.BLUE + SplashScreen)
print("S. Show all saved passwords")
print("C. Clear all saved passwords")
print("D. Clear password file")
print("E. Exit the app \n" + Fore.WHITE)


# Characters
CharacterLower = "abcdefghijklmnoqrstuvwxyz"
CharacterUpper = "ABCDEFGHIJKLMNOQRSTUVWXYZ"
CharacterNumber = "0123456789"
CharacterSymbol = "[]{}()*;/\,_-#@$!%&=+"

Set = CharacterLower + CharacterUpper + CharacterNumber + CharacterSymbol

while True:
    Length = input(Fore.BLUE + "Specify the password length (Allowed to 81 characters): " + Fore.WHITE)

    if 's' == Length.lower():
        try:
            file = open("listpasswords.txt", "r")
            print(Fore.YELLOW + file.read() + Fore.WHITE)
        except:
            print(Fore.RED + "The 'listpasswords.txt' file is not found. \n" + Fore.WHITE)
        continue

    elif 'c' == Length.lower():
        file = open("listpasswords.txt", "w")
        file.write("")
        print(Fore.GREEN + "Cleanup was successfully completed. \n" + Fore.WHITE)
        continue

    elif 'd' == Length.lower():
        try:
            file = "listpasswords.txt"
            os.remove(file)
            print(Fore.GREEN + "The 'listpasswords.txt' file has been successfully deleted. \n" + Fore.WHITE)
        except:
            print(Fore.RED + "The 'listpasswords.txt' file is not found. \n" + Fore.WHITE)
        continue

    elif 'e' == Length.lower():
        exit()

    GeneratePass = "".join(random.sample(Set,int(Length)))
    print(GeneratePass , "\n")

    with open("listpasswords.txt", "a") as file:
        file.write(GeneratePass + "\n\n")
        file.close()