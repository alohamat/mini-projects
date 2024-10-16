#   Random password generator in Python
import random as rd
import string as s

def generatePassword(level):
    senha = []
    
    #   Essa é a senha de nível 1:
    
    if level == 1:
        for _ in range(8):
            senha.append(rd.choice(s.ascii_letters + s.digits))
            
    #   Essa é a senha de nível 2:
    
    elif level == 2:
        for _ in range(rd.randint(8, 12)):
            senha.append(rd.choice(s.ascii_letters + s.digits))

    #   Essa é a senha de nível 3:
    
    else:
        for _ in range(16):
            allowedSymbols = ".!_@#"
            senha.append(rd.choice(s.ascii_letters + s.digits + allowedSymbols))
    
    return ''.join(senha)

def main():
    print("Welcome to password generator")
    while True:
        try:
            r = int(input("Specify password level (1 to 3): "))
            if not r in [1,2,3]:
                raise ValueError
            else:
                print(generatePassword(r), "\n")
        except ValueError:
            print("Specify a valid digit! (1 to 3)\n")

main()