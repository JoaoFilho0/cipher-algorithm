# TUTORIAL

## Requisitos para execução
* Python 3.x instalado - link: https://www.python.org/downloads/.

## Executar o código via terminal
1. Acesse a página do projeto pelo terminal;
2. Já na pasta, digite o seguinte comando:
```
python .\cipher_algorithm.py
``` 

## Preenchendo dados necessários
1. Ao executar o código irá aparecer o texto abaixo, as únicas opções válidas são cript para criptografar o texto e decript para descriptografar o texto.
```
Deseja criptografar(cript) ou descriptografar(decript):
``` 
2. Esse passo irá depender de sua escolha anterior:
* Caso digite cript, será pedido a chave de criptografia que será de 1 à 25:
```
Chave(1-25):
``` 
* Caso digite decript, será perguntado se tem a chave para a descriptografia ou não, as respostas são s para sim e n não:
  - Caso digite sim, será perguntado qual a chave e assim como a criptografia a chave é de 1 à 25.
  - Caso digite não o sistema vai tentar todas as possibilidades possíveis.
```
Possui a chave? (s ou n): 
``` 

3. O último dado pedido é o texto que deseja criptografar ou descriptografar.
```
Texto a ser utilizado:
``` 

## Retorno dos códigos
* Caso selecione cript, a saida será o texto criptografado seguindo a chave informada.
```
Texto a ser utilizado: meu
Texto criptografado: phx
``` 
* Caso selecione decript e informe a chave, o código irá retornar o texto descriptografado seguindo a chave informada.
```
Texto a ser utilizado: phx
Texto descriptografado: meu
``` 

* Caso selecione decript e não informe a chave, o código irá retornar todas as opções possíveis.
```
Texto a ser utilizado: phx
Texto descriptografado:
ogw
nfv
meu
ldt
kcs
jbr
iaq
hzp
gyo
fxn
ewm
dvl
cuk
btj
asi
zrh
yqg
xpf
woe
vnd
umc
tlb
ska
rjz
``` 
