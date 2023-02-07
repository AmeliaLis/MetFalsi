"""
Klasa przechowująca funkcje:
a) f(x) = lnx + 2cosx
przedział x [1,3]

b) g(x) = 0.25*x**3 - 3*(x**2) + 6*x + 2
"""

import math
from sympy import *

# funkcje pomocnicze
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

    def iteruj_roznica(self, eps, wyswietlaj = 1):
        # epsilon
        self.eps = eps

        # tablica z przyblizonymi x0
        self.x = []

        print("\n*** Implementacja metody siecznych ***\n")
        
        print(f"Funkcja: ", self.funkcja)
        print(f"Pierwsza pochodna funkcji: ", self.pochodna1)
        print(f"Druga pochodna funkcji: ", self.pochodna2)

        print("-----"*10)

        # obliczam wartosci na krancach aktualnego przedzialu
        wart_a = MetodaFalsi.wartosc(self.funkcja,self.a)
        print(f"Wartość w punkcie a = {self.a}: ", wart_a)
        wart_b = MetodaFalsi.wartosc(self.funkcja,self.b)
        print(f"Wartość w punkcie b = {self.b}: ",wart_b)

        print("-----"*10)

        # ustalam punkt nieruchomy - obliczam wartosci 2. pochodnej
        wart_poch2_a = MetodaFalsi.wartosc(self.pochodna2,self.a)
        print(f"Wartość drugiej pochodnej w punkcie a = {self.a}: ",wart_poch2_a)
        wart_poch2_b = MetodaFalsi.wartosc(self.pochodna2,self.b)
        print(f"Wartość drugiej pochodnej w punkcie b = {self.b}: ",wart_poch2_b)
        print()

        # sprawdzam, ktory z punktow powinien byc nieruchomy (nazywam go const), czyli sprawdzenie czy funkcja jest stale wypukła
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
            # ponieważ funkcja lnx+2cos, nie jest funkcją wypukłą na podanym przedziale, nieruchomy koniec nie może zostać ustalony
            return [0,0]

        # dodaje przyblizenie startowe do listy
        self.x.append(x_akt)

        # początkowa iteracja
        k = 0

        # wyswietlam przyblizenie startowe
        print("Iteracje i ich przybliżenia: ")
        if wyswietlaj == 1:
            print(f"Iteracja-{k}, przyblizone x0 = {x_akt}, f(x0) = {wartosc(self.funkcja, x_akt)}")
        roznica = 100.0
        while roznica > eps:
            k += 1
            # obliczam wartosc w punkcie x_akt
            wart_x = MetodaFalsi.wartosc(self.funkcja,x_akt)
            x_akt -= wart_x * (x_akt-const) / (wart_x-wart_const) 
            self.x.append(x_akt)
            if wyswietlaj == 1:
                print(f"Iteracja-{k}, przyblizone x0 = {x_akt}, f(x0) = {wartosc(self.funkcja, x_akt)}")
            roznica = abs(self.x[-1] - self.x[-2])
            # jezeli przkroczono maksymalna liczbe rozwiazan - przerywam
            if k == self.kmax:
                print("Przekroczono maksymalna liczbe iteraji.")
                break
        print(f"\nOstateczne przybliżenie x0 - {x_akt}, iteracje - {k}")
        return [k, x_akt]


x = symbols('x')


#testy funkcjonalnsoci definicji utworzonych
#funkcja=(ln(x) + 2*cos(x))
# pochodna1 = pochodna(funkcja)
# print(wartosc(pochodna1,1.0))
# print(wartosc(pochodna1,3.0))
# print(wartosc(funkcja,1.0))
# print(wartosc(funkcja,3.0))
# print(pochodna1)
# print(wartosc(funkcja,xi=1.8965))

met_falsi_a = MetodaFalsi((ln(x) + 2*cos(x)),1.0,3.0)
met_falsi_b = MetodaFalsi((0.25*x**3 - 3*(x**2) + 6*x +2),2.0,3.0)
#met_falsi_c = MetodaFalsi((cos((3*x)/7)), 3.2, 3.7)

met_falsi_a.iteruj_roznica(0.0001)
print("\n")
met_falsi_b.iteruj_roznica(0.0001)
print("\n")
#met_falsi_c.iteruj_roznica(0.0001)
