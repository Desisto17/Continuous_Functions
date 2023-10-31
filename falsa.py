from gerais import calculate

def falsa_posicao(equation: str, x1: str, x2: str, k: int, aprox: int, qnt: int):
  # Recebendo as variáveis em variáveis temporárias
  a = float(x1)
  b = float(x2)
  f_a = float(calculate(equation.replace("x",str(a))))
  f_b = float(calculate(equation.replace("x",str(b))))
  #Arredondando as variáveis de C para que não fique um número gigante.
  c = ((a*f_b)-(b*f_a)) / (f_b-f_a)
  f_c = calculate(equation.replace("x", str(c)))

  print(f"{k}", end=" |")
  print(f" {round(a,aprox):^{aprox+3}}", end=" |")
  print(f" {round(b,aprox):^{aprox+3}}", end=" |")
  print(f" {round(f_a,aprox):^{aprox+3}}", end=" |")
  print(f" {round(f_b,aprox):^{aprox+3}}", end=" |")
  print(f" {round(c,aprox):^{aprox+3}}", end= " |")
  print(f" {round(f_c,aprox):^{aprox+3}} |")

  #Verificando se a função de C é positivo e se é menor(mais próximo de zero) que a função de a. O valor de C vira o valor de A para a próxima iteração, senão vira de B.
  if f_c > 0 and f_c < f_b:
      b = c
  else:
      a = c

  k += 1

  #Verificando se pode acabar com a função recursiva. Senão, chama ela denovo com o contador aumentado e um dos dois valores alterados.
  if round(f_c,aprox) == 0:
    trava = input()
    return
  elif k == qnt:
    trava = input()
    return
  else:
    falsa_posicao(equation, str(a), str(b), k, aprox, qnt)