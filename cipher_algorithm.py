import functions_cript

actionTaken = input("Deseja criptografar(cript) ou descriptografar(decript)?: ")
jumps = int(input("Chave(1-25): "))
text = input("Texto a ser utilizado: ")
finalText = ""

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

if actionTaken == "cript":
    textArrayChar = [char for char in text]

    for textChar in textArrayChar:
        finalText += functions_cript.criptChar(alphabet, functions_cript.getCharIndex(textChar, alphabet), jumps)
    
    print(finalText)

elif actionTaken == "cript":
    textArrayChar = [char for char in text]

    # TODO
else:
    print("Por favor, informe se deseja criptografar(cript) ou descriptografar(decript).")
