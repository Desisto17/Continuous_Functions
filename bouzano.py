from gerais import calculate, relogio


def bouzano(equation: str, x: str, y: str):
  a, b = 0, 0
  temp1 = calculate(equation.replace("x", x))
  temp2 = calculate(equation.replace("x", y))

  #Se o cálculo da função temp1 for positivo, substitui o valor de a por x. Senão, substitui por b.
  if temp1 > 0:
      a = x
  else:
      b = x

  #Se o cálculo da função temp2 for positivo E o valor de a não tiver sido alterado, substitui a por y. Senão, tenta a mesma coisa com b.
  if temp2 > 0 and a == 0:
      a = y
  elif temp2 < 0 and b == 0:
      b = y

  #Se os dois valores foram alterados, era por que tinham sinais diferentes.

  #Verifica se os dois valores forem alterados, e se foram, retorna eles na ordem correta com o positivo primeiro e o negativo em segundo.
  #Senão, retorna um valor negativo duplo para informar o programa que não existe zero entre as raízes.
  if float(a) != 0 and float(b) != 0:
      return str(a), str(b)
  else:
      return "-1", "-1"

def checker(a: str, b: str):
  if a == "-1" and b == "-1":
    print("Não existe raiz entre os dois.")
    exit()
  else:
    print("Existe raiz entre os dois.")
    relogio(2)
    return