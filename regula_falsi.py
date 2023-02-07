import math
MAX_ITERACJA=100
# Miejsce na wpisanie ciała funkcji
# a) f(x) = lnx + 2cosx, czyli math.log(x,math.e) + 2*math.cos(x), która w przedziale [1,3] nie jest wypukła
# b) g(x) = 0.25x^3 - 3x^2 + 6x + 2, czyli 0.25*x**3 - 3*(x**2) + 6*x +2, która w przedziale [2,3] jest wypukła
# c) h(x) = cos((3x)/7), czyli math.cos((3*x)/7)
def f(x):
    return math.log(x,math.e) + 2*math.cos(x)

# Procedura obliczająca miejsca zerowe za pomocą reguły falsi
def regulaFalsi(a,b,eps):
    # a - lewy kraniec przedziału
    # b - prawy kraniec przedziału
    # eps - epsilon


    tablica_x = []  # tablica, w której będę umieszczać przybliżenia miejsc zerowych
    tablica_x.append(a) # na początku wstawiam do tablicy lewy kraniec przedziału, jako pierwsze przybliżenie
    iteracja = 1
    print('\n*** Reguła Falsi ***')
    print('------'*20)
    roznica = True
    

    while roznica and iteracja!=MAX_ITERACJA:
        x0 = (a * f(b) - b * f(a)) / (f(b) - f(a))
        print('Iteracja-%d, przybliżone x0 = %0.40f; f(x0) = %0.40f' % (iteracja, x0, f(x0)))


        if f(x0) == 0:
            print("Przybliżenie jest bliskie lub równe 0.")
            break

        # sprawdzam, czy wartosc funkcji w nowym miejscu zerwoym funkcji liniowej (stycznej) jest przeciwnego znaku jak wartość wczesniej ustalonego krancu
        if f(a) * f(x0) < 0:
            b = x0
        else:
            a = x0
        
        tablica_x.append(x0)
        iteracja = iteracja + 1
        roznica = abs(f(tablica_x[-1])-f(tablica_x[-2])) > eps 
        # procedura będzie wykonywać się do momentu, aż róznica dwóch kolejnych przbylizen x0 będie mniejsza od eps

    print('\nOstateczne przybliżenie x0 - %0.40f, iteracje - %d' % (x0,iteracja-1))

    return [iteracja-1,x0]


# Podanie lewego i prawego końca przedziału
a = float(input('Lewy kraniec przedziału: '))
b = float(input('Prawy kraniec przedziału: '))


# Sprawdzenie założenia, czy wartości na prawym i lewym przedziale są przeciwnych znaków
if f(a) * f(b) > 0.0:
    print('Wartości krańców tego przedziału nie są przeciwnych znaków.')
    print('Wpisz ponownie poprawny przedział.')
else:
    regulaFalsi(a,b,0.0000000001) # wywołanie procedury reguły falsi