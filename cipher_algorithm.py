import unicodedata
import functions_cript

actionTaken = input("Deseja criptografar(cript) ou descriptografar(decript)?: ")
jumps = int(input("Chave(1-25): "))
text = ''.join(ch for ch in unicodedata.normalize('NFKD', input("Texto a ser utilizado: ")) if not unicodedata.combining(ch))
print(text)
finalText = ""

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

if actionTaken == "cript":
    textArrayChar = [char for char in text]

    for textChar in textArrayChar:
        if textChar != " ":
            finalText += functions_cript.criptChar(alphabet, functions_cript.getCharIndex(textChar, alphabet), jumps)
        else:
            finalText += " "

    print(finalText)

elif actionTaken == "cript":
    textArrayChar = [char for char in text]

    # TODO
else:
    print("Por favor, informe se deseja criptografar(cript) ou descriptografar(decript).")
