import time, os, math
from math import log as ln
from math import sqrt, e, pi, sin, cos, tan


def relogio(tempo: int):
  time.sleep(tempo)
  os.system("clear")

def calculate(equation: str):
  return eval(equation)

def header(which: int, size: int):
  if which == 1:
    h_1, h_2, h_3, h_4, h_5, h_6, h_7 = "K", "A", "B", "F(a)", "F(b)", "C", "F(c)"
    print(f"{h_1} | {h_2:^{size+3}} | {h_3:^{size+3}} | {h_4:^{size+3}} | {h_5:^{size+3}} | {h_6:^{size+3}} | {h_7:^{size+3}} |")
  elif which == 2:
    h_1, h_2, h_3, h_4, h_5, h_6, h_7 = "K", "A", "B", "F(a)", "F(b)", "C", "F(c)"
    print(f"{h_1} | {h_2:^{size+3}} | {h_3:^{size+3}} | {h_4:^{size+3}} | {h_5:^{size+3}} | {h_6:^{size+3}} | {h_7:^{size+3}} |")
  elif which == 3:
    h_1, h_2, h_3, h_4, h_5, h_6 = "K", "X", "F(x)", "F'(x)", "X+1", "F(xk+1)"
    print(f"{h_1} | {h_2:^{size+3}} | {h_3:^{size+3}} | {h_4:^{size+3}} | {h_5:^{size+3}} | {h_6:^{size+3}} |")