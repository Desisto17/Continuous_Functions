from sympy import lambdify, diff, sin, cos, tan, log, pi, E, sqrt
from sympy.abc import x

def newton_raphson(funcao: str, x1: float, aprox: int, k: int, qnt: int):
  f = lambdify(x, funcao)
  df = lambdify(x, diff(funcao, x))

  f_xi = f(x1)
  df_xi = df(x1)

  x2 = x1 - (f_xi / df_xi)
  f_x2 = f(x2)

  print(f"{k}", end=" |")
  print(f" {round(x1,aprox):^{aprox+3}}", end=" |")
  print(f" {round(f_xi,aprox):^{aprox+3}}", end=" |")
  print(f" {round(df_xi,aprox):^{aprox+3}}", end=" |")
  print(f" {round(x2,aprox):^{aprox+3}}", end=" |")
  print(f" {round(f_x2,aprox):^{aprox+3}} |")

  k += 1

  if round(f_x2,aprox) == 0:
    trava = input()
    return
  elif k == qnt:
    trava = input()
    return
  else:
    newton_raphson(funcao, x2, aprox, k, qnt)