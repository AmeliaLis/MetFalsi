import math
from sympy import *


def procedura(funkcja, lewy_kraniec, prawy_kraniec, eps):
    pochodna_funkcji = diff(sympify(str(funkcja)),'x')
    print(pochodna_funkcji)
    druga_pochodna_funkcji = diff(sympify(str(pochodna_funkcji),'x'))
    print(druga_pochodna_funkcji)



    return ("k","x0")
x=symbols('x')
procedura((ln(x) + 2*cos(x)),1,3,0.01)