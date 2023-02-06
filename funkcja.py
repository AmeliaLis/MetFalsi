"""
Klasa przechowująca funkcje:
a) f(x) = lnx + 2cosx
przedział x [1,3]

b) przykład z zajęć
"""

import math
from sympy import *



def pochodna(funkcja):
    return diff((funkcja),x)

def wartosc(funkcja,xi):
    expr = funkcja.subs(x,xi)
    return expr


class MetodaFalsi:
    def __init__(self, funkcja, lewy_kraniec, prawy_kraniec):
        """Konstruktor okreslajacy problem"""
        self.funkcja = funkcja
        self.a = lewy_kraniec
        self.b = prawy_kraniec
        self.pochodna1 = pochodna(self.funkcja)
        self.pochodna2 = pochodna(self.pochodna1)
        self.kmax = 10000   
    
    def wartosc(funkcja,xi):
        wartosc = funkcja.subs(x,xi)
        return wartosc

    def interuj_roznica(self, eps, wyswietlaj = 1):
        self.eps = eps

        self.x = []
        # ustalam punkt nieruchomy - obliczam wartosci 2. pochodnej
        wart_poch2_a = MetodaFalsi.wartosc(self.pochodna2,self.a)
        wart_poch2_b = MetodaFalsi.wartosc(self.pochodna2,self.b)
        # obliczam wartosci na krancach aktualnego przedzialu
        wart_a = MetodaFalsi.wartosc(self.funkcja,self.a)
        wart_b = MetodaFalsi.wartosc(self.funkcja,self.b)
        # sprawdzam, ktory z punktow powinien byc nieruchomy (nazywam go const)
        # punkt startowy - oznaczam x_akt
        if wart_a * wart_poch2_a > 0:
            const = self.a
            wart_const = wart_a
            x_akt = self.b
        elif wart_b * wart_poch2_b > 0:
            const = self.b
            wart_const = wart_b
            x_akt = self.a
        else:
            print("Nie mozna zastosowac metody.")
            return 0
        # dodaje przyblizenie startowe do listy
        self.x.append(x_akt)
        k = 0
        # wyswietlam przyblizenie startowe
        if wyswietlaj == 1:
            print(f"{k}. \t {x_akt}")
        roznica = 100.0
        while roznica > eps:
            k += 1
            # obliczam wartosc w punkcie x_akt
            wart_x = MetodaFalsi.wartosc(self.funkcja,x_akt)
            x_akt -= wart_x * (x_akt-const) / (wart_x-wart_const) 
            self.x.append(x_akt)
            if wyswietlaj == 1:
                print(f"{k}. \t {x_akt}")
            roznica = abs(self.x[-1] - self.x[-2])
            # jezeli przkroczono maksymalna liczbe rozwiazan - przerywam
            if k == self.kmax:
                print("Przekroczono maksymalna liczbe iteraji.")
                break
        return k


#fx=Funkcja()
#print(fx.f(1.9))
x = symbols('x')

#print(fx.f(5))
#print(pochodna((ln(x) + 2*cos(x))))
#print(pochodna(x**2))

met_falsi = MetodaFalsi((ln(x) + 2*cos(x)),1.0,3.0)
#print(met_falsi.funkcja)
#print(met_falsi.a)
#print(met_falsi.b)
#print(met_falsi.pochodna1)
#print(met_falsi.pochodna2)
funkcja=(ln(x) + 2*cos(x))

pochodna1 = pochodna(funkcja)
print(pochodna1)
print(wartosc(pochodna1,xi=1.8965))
