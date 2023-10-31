from bisseccao import bissecao
from falsa import falsa_posicao
from bouzano import bouzano, checker
from gerais import relogio, header
from newton import newton_raphson

def menu():
  relogio(0)
  calculadora = "- \033[34mCALCULADORA\033[0m -"
  print(f"{calculadora:^50}")
  resposta = input("\n1 - \033[31mBissecção\033[0m\n2 - \033[34mFalsa Posição\033[0m \n3 - \033[35mNewton-Raphson\033[0m\n\nQual metódo você gostaria de usar? -> ").strip()
  relogio(1)
  if resposta == "1":
    func = input("Insira a função a ser utilizada -> ").strip()
    a = input("Insira o primeiro valor de chute inicial -> ").strip()
    b = input("Insira o segundo valor de chute inicial -> ").strip()
    lim = int(input("Insira a aproximação desejada -> "))
    qnt = int(input("Quantia de iterações -> "))
    a, b = bouzano(func, a, b)
    checker(a, b)
    header(1,lim)
    bissecao(func, a, b, 0, lim, qnt)
    
  elif resposta == "2":
    func = input("Insira a função a ser utilizada -> ").strip()
    a = input("Insira o primeiro valor de chute inicial -> ").strip()
    b = input("Insira o segundo valor de chute inicial -> ").strip()
    lim = int(input("Insira a aproximação desejada -> "))
    qnt = int(input("Quantia de iterações -> "))
    b, a = bouzano(func, a, b)
    checker(a, b)
    header(2,lim)
    falsa_posicao(func, a, b, 0, lim, qnt)
    
  elif resposta == "3":
    func = input("Insira a função a ser utilizada -> ").strip()
    a = float(input("Insira o chute inicial -> "))
    lim = int(input("Insira a aproximação desejada -> "))
    qnt = int(input("Quantia de iterações -> "))
    header(3, lim)
    newton_raphson(func, a, lim, 0, qnt)
  else:
    print("Essa não é uma resposta válida !")
    relogio(2)
    
      
    