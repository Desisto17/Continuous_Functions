from gerais import calculate

def bissecao(equation: str, x1: str, x2: str, k: int, aprox: int, qnt: int):
  # Recebendo as variáveis em variáveis temporárias
  a = x1
  b = x2
  c = str((float(a)+float(b))/2)
  f_a = calculate(equation.replace("x",a))
  f_b = calculate(equation.replace("x",b))
  #Arredondando só a função C por que ela é a única que pode acabar toda quebrada.
  f_c = calculate(equation.replace("x",c))

  print(f"{k}", end=" |")
  print(f" {a:^{aprox+3}}", end=" |")
  print(f" {b:^{aprox+3}}", end=" |")
  print(f" {round(f_a,aprox):^{aprox+3}}", end=" |")
  print(f" {round(f_b,aprox):^{aprox+3}}", end=" |")
  print(f" {c:^{aprox+3}}", end= " |")
  print(f" {round(f_c,aprox):^{aprox+3}} |")
  

  #Verificando se a função de C é positivo e se é menor(mais próximo de zero) que a função de a. O valor de C vira o valor de A para a próxima iteração, senão vira de B.
  if f_c > 0 and f_c < f_a:
      a = c
  else:
      b = c

  k += 1

  #Verificando se pode acabar com a função recursiva. Senão, chama ela denovo com o contador aumentado e um dos dois valores alterados.
  if round(f_c,aprox) == 0:
    trava = input()
    return
  elif k == qnt:
    trava = input()
    return
  else:
    bissecao(equation, a, b, k, aprox, qnt)