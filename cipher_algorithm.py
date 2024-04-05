import unicodedata
import functions_cript

actionTaken = input("Deseja criptografar(cript) ou descriptografar(decript): ")
if actionTaken == "decript":
    response = input("Possui a chave? (s ou n): ")
    if  response == "s":
        jumps = int(input("Chave(1-25): "))
    elif response == "n":
        jumps = 0
elif actionTaken == "cript":
    jumps = int(input("Chave(1-25): "))

text = ''.join(ch for ch in unicodedata.normalize('NFKD', input("Texto a ser utilizado: ")) if not unicodedata.combining(ch))
finalText = ""

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

if actionTaken == "cript":
    textArrayChar = [char for char in text]

    for textChar in textArrayChar:
        if textChar != " ":
            finalText += functions_cript.criptChar(alphabet, functions_cript.getCharIndex(textChar, alphabet), jumps) if textChar.islower() else str.upper(functions_cript.criptChar(alphabet, functions_cript.getCharIndex(textChar, alphabet), jumps))
        else:
            finalText += " "

    print("Texto criptografado: " + finalText)

elif actionTaken == "decript":
    textArrayChar = [char for char in text]
    aux = ""

    if jumps != 0:
        for textChar in textArrayChar:
            if textChar != " ":
                finalText += functions_cript.decriptChar(alphabet, functions_cript.getCharIndex(textChar, alphabet), jumps) if textChar.islower() else str.upper(functions_cript.decriptChar(alphabet, functions_cript.getCharIndex(textChar, alphabet), jumps))
            else:
                finalText += " "
    else:
        finalText = []
        for num in range(1,25):
            for textChar in textArrayChar:
                if textChar != " ":
                    aux += functions_cript.decriptChar(alphabet, functions_cript.getCharIndex(textChar, alphabet), num) if textChar.islower() else str.upper(functions_cript.decriptChar(alphabet, functions_cript.getCharIndex(textChar, alphabet), num))
                else:
                    aux += " "
            
            finalText.append(aux)
            aux = ""
    
    print("Texto descriptografado: ")
    if type(finalText) == str:
        print(finalText)
    else:
        print("\n",*finalText, sep = "\n")
    
else:
    print("Por favor, informe se deseja criptografar(cript) ou descriptografar(decript).")
