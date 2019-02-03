#wprowadzenie tabeli
a1 = [5.1, 4.9, 4.6, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9, 6.9, 6.4, 6.9, 5.5, 6.5, 5.7, 6.3, 4.9, 6.6, 5.2, 6.3, 5.8, 7.1, 6.3, 6.5, 7.6, 4.9, 7.3, 6.7, 7.2]
a2 = [3.5, 3.0, 3.1, 3.1, 3.6, 3.9, 3.4, 3.4, 2.9, 3.1, 3.2, 3.2, 3.1, 2.3, 2.8, 2.8, 3.3, 2.4, 2.9, 2.7, 3.3, 2.7, 3.0, 2.9, 3.0, 3.0, 2.5, 2.9, 2.5, 3.6]
a3 = [1.4, 1.4, 1.3, 1.3, 1.4, 1.7, 1.4, 1.5, 1.4, 1.5, 4.7, 4.5, 4.9, 4.0, 4.6, 4.5, 4.7, 3.3, 4.6, 3.9, 6.0, 5.1, 5.9, 5.6, 5.8, 6.6, 4.5, 6.3, 5.8, 6.1]
a4 = [0.2, 0.2, 0.2, 0.2, 0.2, 0.4, 0.3, 0.2, 0.2, 0.1, 1.4, 1.5, 1.5, 1.3, 1.5, 1.3, 1.6, 1.0, 1.3, 1.4, 2.5, 1.9, 2.1, 1.8, 2.2, 2.1, 1.7, 1.8, 1.8, 2.5]

Klasa = ["SETOSA", "SETOSA", "SETOSA", "SETOSA", "SETOSA", "SETOSA", "SETOSA", "SETOSA", "SETOSA", "SETOSA",
         "VERSICOLOR", "VERSICOLOR", "VERSICOLOR", "VERSICOLOR", "VERSICOLOR", "VERSICOLOR", "VERSICOLOR", "VERSICOLOR", "VERSICOLOR", "VERSICOLOR",
         "VIRGINICA", "VIRGINICA", "VIRGINICA", "VIRGINICA", "VIRGINICA", "VIRGINICA", "VIRGINICA", "VIRGINICA", "VIRGINICA","VIRGINICA" ]

#pobudzenia dla pól
x_a1 = {}
x_a2 = {}
x_a3 = {}
x_a4 = {}
tab_x_a = [x_a1, x_a2, x_a3, x_a4]

pobudzenia_a1 = {}
pobudzenia_a2 = {}
pobudzenia_a3 = {}
pobudzenia_a4 = {}
tab_pob=[pobudzenia_a1, pobudzenia_a2, pobudzenia_a3, pobudzenia_a4]

#czasy aktywacji
czas_a1 = {}
czas_a2 = {}
czas_a3 = {}
czas_a4 = {}
tab_czas=[czas_a1, czas_a2, czas_a3, czas_a4]

neurony = {}
pob_jedynki = {} #jedynki z pobudzeń
lokal_min = {} #minima z pól sensorycznych
lista_neuronow = [] #lista podobnych neuronów

#obliczanie zakresów
r1 = max(a1) - min(a1)
r2 = max(a2) - min(a2)
r3 = max(a3) - min(a3)
r4 = max(a4) - min(a4)
r = [r1, r2, r3, r4]

#sortowanie
posortowane_a1 = sorted(set(a1))
posortowane_a2 = sorted(set(a2))
posortowane_a3 = sorted(set(a3))
posortowane_a4 = sorted(set(a4))
posortowane_a=[posortowane_a1, posortowane_a2, posortowane_a3, posortowane_a4]

#tworzenie grafu (listy i słowniki)
neuron_number = 1
for item1, item2, item3, item4, item5 in zip(a1, a2, a3, a4, Klasa):
    repeated_value = True
    for key in neurony:
        if neurony[key] == [item1, item2, item3, item4, item5]:
            repeated_value = False
            break
    if repeated_value == True:
        neurony[neuron_number] = [item1, item2, item3, item4, item5]
        neuron_number += 1

#menu
while True:

    print("Co chcesz zrobić?")
    print("[1] Pokaż tabelę")
    print("[2] Pokaż pola sensoryczne")
    print("[3] Pokaż neurony")
    print("[4] Pokaż wartości najmniejsze i największe")
    print("[5] Wprowadź pobudzenie dla neuronu zewnętrznego")
    print("[6] Wprowadź pobudzenie dla pola sensorycznego")
    print("[7] Koniec")
    numer = int(input())

#wyświetlanie tabeli
    if numer == 1:
        print("\n")
        print( "   " + " sepal length " + " sepal width " + " petal length " + " petal width " + " class ")
        i = 1
        for item1, item2, item3, item4, item5 in zip(a1, a2, a3, a4, Klasa):
            print(" R" + str(i) + "    ", item1, "        ", item2, "        ", item3, "         ", item4, "     ", item5)
            i = i+1
        print("\n")

#wyświetlanie pól sensorycznych
    elif numer == 2:
        print("\n")
        print("A1 :", posortowane_a1)
        print("A2 :", posortowane_a2)
        print("A3 :", posortowane_a3)
        print("A4 :", posortowane_a4)
        print("\n")

#wyświetlanie neuronów
    elif numer == 3:
        print("\n")
        for key in neurony:
            print(key, ": ", neurony[key])
        print("\n")

# wartości min max
    elif numer == 4:
        print("\n")
        print("SEPAL LENGTH: najmniejsza: ",min(posortowane_a1),", największa:",max(posortowane_a1))
        print("SEPAL WIDTH: najmniejsza: ", min(posortowane_a2), ", największa:", max(posortowane_a2))
        print("PETAL LENGTH: najmniejsza: ", min(posortowane_a3), ", największa:", max(posortowane_a3))
        print("PETAL WIDTH: najmniejsza: ", min(posortowane_a4), ", największa:", max(posortowane_a4))
        print("\n")

#pobudzanie neuronu
    elif numer == 5:
        print("\n")
        print("Który neuron chcesz pobudzić (1-" + str(len(neurony)) + ")?")
        neuron = int(input())
        for pobudzenie_x1 in posortowane_a1:
            pobudzenia_a1[pobudzenie_x1] = []
            if posortowane_a1[0] == pobudzenie_x1:
                for v in posortowane_a1:
                    if r1 > 0:
                        pobudzenia_a1[pobudzenie_x1].append((max(a1) - v) / r1)
                    else:
                        pobudzenia_a1[pobudzenie_x1].append(0)
            elif posortowane_a1[-1] == pobudzenie_x1:
                for v in posortowane_a1:
                    if r1 > 0:
                        pobudzenia_a1[pobudzenie_x1].append((v - min(a1)) / r1)
                    else:
                        pobudzenia_a1[pobudzenie_x1].append(0)
            else:
                for v in posortowane_a1:
                    if r1 > 0:
                        pobudzenia_a1[pobudzenie_x1].append(1 - (abs(pobudzenie_x1 - v)) / r1)
                    else:
                        pobudzenia_a1[pobudzenie_x1].append(0)

        for pobudzenie_x2 in posortowane_a2:
            pobudzenia_a2[pobudzenie_x2] = []
            if posortowane_a2[0] == pobudzenie_x2:
                for v in posortowane_a2:
                    if r2 > 0:
                        pobudzenia_a2[pobudzenie_x2].append((max(a2) - v) / r2)
                    else:
                        pobudzenia_a2[pobudzenie_x2].append(0)
            elif posortowane_a2[-1] == pobudzenie_x2:
                for v in posortowane_a2:
                    if r2 > 0:
                        pobudzenia_a2[pobudzenie_x2].append((v - min(a2)) / r2)
                    else:
                        pobudzenia_a2[pobudzenie_x2].append(0)
            else:
                for v in posortowane_a2:
                    if r2 > 0:
                        pobudzenia_a2[pobudzenie_x2].append(1 - (abs(pobudzenie_x2 - v)) / r2)
                    else:
                        pobudzenia_a2[pobudzenie_x2].append(0)

        for pobudzenie_x3 in posortowane_a3:
            pobudzenia_a3[pobudzenie_x3] = []
            if posortowane_a3[0] == pobudzenie_x3:
                for v in posortowane_a3:
                    if r3 > 0:
                        pobudzenia_a3[pobudzenie_x3].append((max(a3) - v) / r3)
                    else:
                        pobudzenia_a3[pobudzenie_x3].append(0)
            elif posortowane_a3[-1] == pobudzenie_x3:
                for v in posortowane_a3:
                    if r2 > 0:
                        pobudzenia_a3[pobudzenie_x3].append((v - min(a3)) / r3)
                    else:
                        pobudzenia_a3[pobudzenie_x3].append(0)
            else:
                for v in posortowane_a3:
                    if r2 > 0:
                        pobudzenia_a3[pobudzenie_x3].append(1 - (abs(pobudzenie_x3 - v)) / r3)
                    else:
                        pobudzenia_a3[pobudzenie_x3].append(0)

        for pobudzenie_x4 in posortowane_a4:
            pobudzenia_a4[pobudzenie_x4] = []
            if posortowane_a4[0] == pobudzenie_x4:
                for v in posortowane_a4:
                    if r4 > 0:
                        pobudzenia_a4[pobudzenie_x4].append((max(a4) - v) / r4)
                    else:
                        pobudzenia_a4[pobudzenie_x4].append(0)
            elif posortowane_a4[-1] == pobudzenie_x4:
                for v in posortowane_a4:
                    if r4 > 0:
                        pobudzenia_a4[pobudzenie_x4].append((v - min(a4)) / r4)
                    else:
                        pobudzenia_a4[pobudzenie_x4].append(0)
            else:
                for v in posortowane_a4:
                    if r2 > 0:
                        pobudzenia_a4[pobudzenie_x4].append(1 - (abs(pobudzenie_x4 - v)) / r4)
                    else:
                        pobudzenia_a4[pobudzenie_x4].append(0)

        x1 = neurony[neuron][0]
        x2 = neurony[neuron][1]
        x3 = neurony[neuron][2]
        x4 = neurony[neuron][3]

        if x1 == min(posortowane_a1):
            for sensor in posortowane_a1:
                x_a1[sensor] = (max(posortowane_a1) - sensor) / r1
        elif x1 == max(posortowane_a1):
            for sensor in posortowane_a1:
                x_a1[sensor] = (sensor - min(posortowane_a1)) / r1
        else:
            for sensor in posortowane_a1:
                x_a1[sensor] = (1 - (abs(x1 - sensor)) / r1)

        for key in x_a1:
            if x_a1[key] == 0:
                x_a1[key] = 0.1

        if x1 == min(posortowane_a2):
            for sensor in posortowane_a2:
                x_a2[sensor] = (max(posortowane_a2) - sensor) / r2
        elif x2 == max(posortowane_a2):
            for sensor in posortowane_a2:
                x_a2[sensor] = (sensor - min(posortowane_a2)) / r2
        else:
            for sensor in posortowane_a2:
                x_a2[sensor] = (1 - (abs(x2 - sensor)) / r2)

        for key in x_a2:
            if x_a2[key] == 0:
                x_a2[key] = 0.1

        if x3 == min(posortowane_a3):
            for sensor in posortowane_a3:
                x_a3[sensor] = (max(posortowane_a3) - sensor) / r3
        elif x3 == max(posortowane_a3):
            for sensor in posortowane_a3:
                x_a3[sensor] = (sensor - min(posortowane_a3)) / r3
        else:
            for sensor in posortowane_a3:
                x_a3[sensor] = (1 - (abs(x3 - sensor)) / r3)

        for key in x_a3:
            if x_a3[key] == 0:
                x_a3[key] = 0.1

        if x4 == min(posortowane_a4):
            for sensor in posortowane_a4:
                x_a4[sensor] = (max(posortowane_a4) - sensor) / r4
        elif x4 == max(posortowane_a4):
            for sensor in posortowane_a4:
                x_a4[sensor] = (sensor - min(posortowane_a4)) / r4
        else:
            for sensor in posortowane_a4:
                x_a4[sensor] = (1 - (abs(x4 - sensor)) / r4)

        for key in x_a4:
            if x_a4[key] == 0:
                x_a4[key] = 0.1

        for value in x_a1:
            czas_a1[value] = (1 / x_a1[value])

        for value in x_a2:
            czas_a2[value] = (1 / x_a2[value])

        for value in x_a3:
            czas_a3[value] = (1 / x_a3[value])

        for value in x_a4:
            czas_a4[value] = (1 / x_a4[value])

        for key in neurony:
            pob_jedynki[key] = 0

        while len(czas_a1) > 0 or len(czas_a2) > 0 or len(czas_a3) > 0 or len(czas_a4) > 0:
            try:
                lokal_min[min(czas_a1, key=czas_a1.get)] = czas_a1[min(czas_a1, key=czas_a1.get)]
            except:
                lokal_min[2147483647] = 2147483647
            try:
                lokal_min[min(czas_a2, key=czas_a2.get)] = czas_a2[min(czas_a2, key=czas_a2.get)]
            except:
                lokal_min[2147483646] = 2147483646
            try:
                lokal_min[min(czas_a3, key=czas_a3.get)] = czas_a3[min(czas_a3, key=czas_a3.get)]
            except:
                lokal_min[2147483645] = 2147483645
            try:
                lokal_min[min(czas_a4, key=czas_a4.get)] = czas_a4[min(czas_a4, key=czas_a4.get)]
            except:
                lokal_min[2147483644] = 2147483644
            min_rec = min(lokal_min, key=lokal_min.get)

            for key in neurony:
                if neurony[key][0] == min_rec:
                    pob_jedynki[key] = pob_jedynki[key] + 1
                    try:
                        czas_a1.pop(min_rec)
                    except:
                        continue
                    continue
                elif neurony[key][1] == min_rec:
                    pob_jedynki[key] = pob_jedynki[key] + 1
                    try:
                        czas_a2.pop(min_rec)
                    except:
                        continue
                    continue
                elif neurony[key][2] == min_rec:
                    pob_jedynki[key] = pob_jedynki[key] + 1
                    try:
                        czas_a3.pop(min_rec)
                    except:
                        continue
                    continue
                elif neurony[key][3] == min_rec:
                    pob_jedynki[key] = pob_jedynki[key] + 1
                    try:
                        czas_a4.pop(min_rec)
                    except:
                        continue
                    continue
                else:
                    continue

            for key in pob_jedynki:
                if pob_jedynki[key] == 4 and key not in lista_neuronow:
                    lista_neuronow.append(key)
            lokal_min = {}

        print('\n')

        print("Podobieństwo neuronów (od najbardziej do najmniej podobnego):")
        for key in lista_neuronow:
            print("N" + str(key) + " : " + str(neurony[key]))

        lista_neuronow = []
        print('\n')

#pobudzanie pola sensorycznego
    elif numer == 6:
        print("\n")
        ilosc = float(input("Ile pól sensorycznych chcesz pobudzić (1, 2, 3 lub 4)? "))

        if ilosc ==1:
            print("\n")
            ktore = int(input("Które pole sensoryczne chcesz pobudzić? "))
            print("\n")

            x1 = float(input("Wartość pobudzenia: "))
            print("\n")
            if x1 == min(posortowane_a[ktore-1]):
                for sensor in posortowane_a[ktore-1]:
                    tab_x_a[ktore-1][sensor] = (max(posortowane_a[ktore-1]) - sensor) / r[ktore-1]
            elif x1 == max(posortowane_a[ktore-1]):
                for sensor in posortowane_a[ktore-1]:
                    tab_x_a[ktore-1][sensor] = (sensor - min(posortowane_a[ktore-1])) / r[ktore-1]
            else:
                for sensor in posortowane_a[ktore-1]:
                    tab_x_a[ktore-1][sensor] = (1 - (abs(x1 - sensor)) / r[ktore-1])

            for key in tab_x_a[ktore-1]:
                if tab_x_a[ktore-1][key] == 0:
                    tab_x_a[ktore-1][key] = 0.1

            for value in tab_x_a[ktore-1]:
                tab_czas[ktore-1][value] = (1 / tab_x_a[ktore-1][value])

            for key in neurony:
                pob_jedynki[key] = 0

            while len(tab_czas[ktore-1]) > 0:
                try:
                    lokal_min[min(tab_czas[ktore-1], key=tab_czas[ktore-1].get)] = tab_czas[ktore-1][min(tab_czas[ktore-1], key=tab_czas[ktore-1].get)]
                except:
                    lokal_min[2147483647] = 2147483647

                min_rec = min(lokal_min, key=lokal_min.get)

                for key in neurony:
                    if neurony[key][ktore-1] == min_rec:
                        pob_jedynki[key] = pob_jedynki[key] + 1
                        try:
                            tab_czas[ktore-1].pop(min_rec)
                        except:
                            continue
                        continue

                    else:
                        continue

                for key in pob_jedynki:
                    if pob_jedynki[key] == 1 and key not in lista_neuronow:
                        lista_neuronow.append(key)
                lokal_min = {}

            print('\n')

            print("Klasyfikacja obiektu do klasy: " + str(neurony[lista_neuronow[0]][4]))
            print("Podobieństwo neuronów (od najbardziej do najmniej podobnego):")
            for key in lista_neuronow:
                print(neurony[key])

            lista_neuronow = []
            print('\n')

        elif ilosc == 2:
            print("\n")
            ktore1 = int(input("Które pole sensoryczne chcesz pobudzić jako pierwsze (1-4)? "))
            ktore2 = int(input("Które pole sensoryczne chcesz pobudzić jako drugie (1-4)? "))
            print("\n")

            if ktore1 == ktore2:
                print("Numery pobudzanych pól muszą być różne!")
                break

            x1 = float(input("Wartość pierwszego pobudzenia: "))
            x2 = float(input("Wartość drugiego pobudzenia: "))
            print("\n")

            if x1 == min(posortowane_a[ktore1-1]):
                for sensor in posortowane_a[ktore1-1]:
                    tab_x_a[ktore1-1][sensor] = (max(posortowane_a[ktore1-1]) - sensor) / r[ktore1-1]
            elif x1 == max(posortowane_a[ktore1-1]):
                for sensor in posortowane_a[ktore1-1]:
                    tab_x_a[ktore1-1][sensor] = (sensor - min(posortowane_a[ktore1-1])) / r[ktore1-1]
            else:
                for sensor in posortowane_a[ktore1-1]:
                    tab_x_a[ktore1-1][sensor] = (1 - (abs(x1 - sensor)) / r[ktore1-1])

            for key in tab_x_a[ktore1-1]:
                if tab_x_a[ktore1-1][key] == 0:
                    tab_x_a[ktore1-1][key] = 0.1

            if x2 == min(posortowane_a[ktore2-1]):
                for sensor in posortowane_a[ktore2-1]:
                    tab_x_a[ktore2-1][sensor] = (max(posortowane_a[ktore2-1]) - sensor) / r[ktore2-1]
            elif x2 == max(posortowane_a[ktore2-1]):
                for sensor in posortowane_a[ktore2-1]:
                    tab_x_a[ktore2-1][sensor] = (sensor - min(posortowane_a[ktore2-1])) / r[ktore2-1]
            else:
                for sensor in posortowane_a[ktore2-1]:
                    tab_x_a[ktore2-1][sensor] = (1 - (abs(x2 - sensor)) / r[ktore2-1])

            for key in tab_x_a[ktore2-1]:
                if tab_x_a[ktore2-1][key] == 0:
                    tab_x_a[ktore2-1][key] = 0.1

            for value in tab_x_a[ktore1-1]:
                tab_czas[ktore1-1][value] = (1 / tab_x_a[ktore1-1][value])

            for value in tab_x_a[ktore2-1]:
                tab_czas[ktore2-1][value] = (1 / tab_x_a[ktore2-1][value])

            for key in neurony:
                pob_jedynki[key] = 0

            while len(tab_czas[ktore1-1]) > 0 or len(tab_czas[ktore2-1]) > 0:
                try:
                    lokal_min[min(tab_czas[ktore1-1], key=tab_czas[ktore1-1].get)] = tab_czas[ktore1-1][min(tab_czas[ktore1-1], key=tab_czas[ktore1-1].get)]
                except:
                    lokal_min[2147483647] = 2147483647
                try:
                    lokal_min[min(tab_czas[ktore2-1], key=tab_czas[ktore2-1].get)] = tab_czas[ktore2-1][min(tab_czas[ktore2-1], key=tab_czas[ktore2-1].get)]
                except:
                    lokal_min[2147483646] = 2147483646
                min_rec = min(lokal_min, key=lokal_min.get)

                for key in neurony:
                    if neurony[key][ktore1-1] == min_rec:
                        pob_jedynki[key] = pob_jedynki[key] + 1
                        try:
                            tab_czas[ktore1-1].pop(min_rec)
                        except:
                            continue
                        continue
                    elif neurony[key][ktore2-1] == min_rec:
                        pob_jedynki[key] = pob_jedynki[key] + 1
                        try:
                            tab_czas[ktore2-1].pop(min_rec)
                        except:
                            continue
                        continue

                for key in pob_jedynki:
                    if pob_jedynki[key] == 2 and key not in lista_neuronow:
                        lista_neuronow.append(key)
                lokal_min = {}

            print('\n')

            print("Klasyfikacja obiektu do klasy: " + str(neurony[lista_neuronow[0]][4]))
            print("Podobieństwo neuronów (od najbardziej do najmniej podobnego):")
            for key in lista_neuronow:
                print(neurony[key])

            lista_neuronow = []
            print('\n')

        elif ilosc == 3:
            print("\n")
            ktore1 = int(input("Które pole sensoryczne chcesz pobudzić jako pierwsze (1-4)? "))
            ktore2 = int(input("Które pole sensoryczne chcesz pobudzić jako drugie (1-4)? "))
            ktore3 = int(input("Które pole sensoryczne chcesz pobudzić jako trzecie (1-4)? "))
            print("\n")

            if ktore1 == ktore2 or ktore1==ktore3 or ktore2==ktore3:
                print("Numery pobudzanych pól muszą być różne!")
                break

            x1 = float(input("Wartość pierwszego pobudzenia: "))
            x2 = float(input("Wartość drugiego pobudzenia: "))
            x3 = float(input("Wartość trzeciego pobudzenia: "))
            print("\n")

            if x1 == min(posortowane_a[ktore1 - 1]):
                for sensor in posortowane_a[ktore1 - 1]:
                    tab_x_a[ktore1 - 1][sensor] = (max(posortowane_a[ktore1 - 1]) - sensor) / r[ktore1 - 1]
            elif x1 == max(posortowane_a[ktore1 - 1]):
                for sensor in posortowane_a[ktore1 - 1]:
                    tab_x_a[ktore1 - 1][sensor] = (sensor - min(posortowane_a[ktore1 - 1])) / r[ktore1 - 1]
            else:
                for sensor in posortowane_a[ktore1 - 1]:
                    tab_x_a[ktore1 - 1][sensor] = (1 - (abs(x1 - sensor)) / r[ktore1 - 1])

            for key in tab_x_a[ktore1 - 1]:
                if tab_x_a[ktore1 - 1][key] == 0:
                    tab_x_a[ktore1 - 1][key] = 0.1

            if x2 == min(posortowane_a[ktore2 - 1]):
                for sensor in posortowane_a[ktore2 - 1]:
                    tab_x_a[ktore2 - 1][sensor] = (max(posortowane_a[ktore2 - 1]) - sensor) / r[ktore2 - 1]
            elif x2 == max(posortowane_a[ktore2 - 1]):
                for sensor in posortowane_a[ktore2 - 1]:
                    tab_x_a[ktore2 - 1][sensor] = (sensor - min(posortowane_a[ktore2 - 1])) / r[ktore2 - 1]
            else:
                for sensor in posortowane_a[ktore2 - 1]:
                    tab_x_a[ktore2 - 1][sensor] = (1 - (abs(x2 - sensor)) / r[ktore2 - 1])

            for key in tab_x_a[ktore2 - 1]:
                if tab_x_a[ktore2 - 1][key] == 0:
                    tab_x_a[ktore2 - 1][key] = 0.1

            if x3 == min(posortowane_a[ktore3 - 1]):
                for sensor in posortowane_a[ktore3 - 1]:
                    tab_x_a[ktore3 - 1][sensor] = (max(posortowane_a[ktore3 - 1]) - sensor) / r[ktore3 - 1]
            elif x3 == max(posortowane_a[ktore3 - 1]):
                for sensor in posortowane_a[ktore3 - 1]:
                    tab_x_a[ktore3 - 1][sensor] = (sensor - min(posortowane_a[ktore3 - 1])) / r[ktore3 - 1]
            else:
                for sensor in posortowane_a[ktore3 - 1]:
                    tab_x_a[ktore3 - 1][sensor] = (1 - (abs(x3 - sensor)) / r[ktore3 - 1])

            for key in tab_x_a[ktore3 - 1]:
                if tab_x_a[ktore3 - 1][key] == 0:
                    tab_x_a[ktore3 - 1][key] = 0.1

            for value in tab_x_a[ktore1 - 1]:
                tab_czas[ktore1 - 1][value] = (1 / tab_x_a[ktore1 - 1][value])

            for value in tab_x_a[ktore2 - 1]:
                tab_czas[ktore2 - 1][value] = (1 / tab_x_a[ktore2 - 1][value])

            for value in tab_x_a[ktore3 - 1]:
                tab_czas[ktore3 - 1][value] = (1 / tab_x_a[ktore3 - 1][value])

            for key in neurony:
                pob_jedynki[key] = 0

            while len(tab_czas[ktore1 - 1]) > 0 or len(tab_czas[ktore2 - 1]) > 0 or len(tab_czas[ktore3 - 1]) > 0:
                try:
                    lokal_min[min(tab_czas[ktore1 - 1], key=tab_czas[ktore1 - 1].get)] = tab_czas[ktore1 - 1][
                        min(tab_czas[ktore1 - 1], key=tab_czas[ktore1 - 1].get)]
                except:
                    lokal_min[2147483647] = 2147483647
                try:
                    lokal_min[min(tab_czas[ktore2 - 1], key=tab_czas[ktore2 - 1].get)] = tab_czas[ktore2 - 1][
                        min(tab_czas[ktore2 - 1], key=tab_czas[ktore2 - 1].get)]
                except:
                    lokal_min[2147483646] = 2147483646
                try:
                    lokal_min[min(tab_czas[ktore3 - 1], key=tab_czas[ktore3 - 1].get)] = tab_czas[ktore3 - 1][
                        min(tab_czas[ktore3 - 1], key=tab_czas[ktore3 - 1].get)]
                except:
                    lokal_min[2147483646] = 2147483646
                min_rec = min(lokal_min, key=lokal_min.get)

                for key in neurony:
                    if neurony[key][ktore1 - 1] == min_rec:
                        pob_jedynki[key] = pob_jedynki[key] + 1
                        try:
                            tab_czas[ktore1 - 1].pop(min_rec)
                        except:
                            continue
                        continue
                    elif neurony[key][ktore2 - 1] == min_rec:
                        pob_jedynki[key] = pob_jedynki[key] + 1
                        try:
                            tab_czas[ktore2 - 1].pop(min_rec)
                        except:
                            continue
                        continue
                    elif neurony[key][ktore3 - 1] == min_rec:
                        pob_jedynki[key] = pob_jedynki[key] + 1
                        try:
                            tab_czas[ktore3 - 1].pop(min_rec)
                        except:
                            continue
                        continue

                for key in pob_jedynki:
                    if pob_jedynki[key] == 3 and key not in lista_neuronow:
                        lista_neuronow.append(key)
                lokal_min = {}

            print('\n')

            print("Klasyfikacja obiektu do klasy: " + str(neurony[lista_neuronow[0]][4]))
            print("Podobieństwo neuronów (od najbardziej do najmniej podobnego):")
            for key in lista_neuronow:
                print(neurony[key])

            lista_neuronow = []
            print('\n')

        elif ilosc ==4:
            print("\n")
            x1 = float(input("Wartość pobudzenia pierwszego pola sensorycznego: "))
            x2 = float(input("Wartość pobudzenia drugiego pola sensorycznego: "))
            x3 = float(input("Wartość pobudzenia trzeciego pola sensorycznego: "))
            x4 = float(input("Wartość pobudzenia czwartego pola sensorycznego: "))
            print("\n")

            if x1 == min(posortowane_a1):
                for sensor in posortowane_a1:
                    x_a1[sensor] = (max(posortowane_a1)- sensor) / r1
            elif x1 == max(posortowane_a1):
                for sensor in posortowane_a1:
                    x_a1[sensor] = (sensor - min(posortowane_a1)) / r1
            else:
                for sensor in posortowane_a1:
                    x_a1[sensor] = (1 - (abs(x1 - sensor)) / r1)

            for key in x_a1:
                if x_a1[key] == 0:
                    x_a1[key] = 0.1

            if x2 == min(posortowane_a2):
                for sensor in posortowane_a2:
                    x_a2[sensor] = (max(posortowane_a2) - sensor) / r2
            elif x2 == max(posortowane_a2):
                for sensor in posortowane_a2:
                    x_a2[sensor] = (sensor - min(posortowane_a2)) / r2
            else:
                for sensor in posortowane_a2:
                    x_a2[sensor] = (1 - (abs(x2 - sensor)) / r2)

            for key in x_a2:
                if x_a2[key] == 0:
                    x_a2[key] = 0.1

            if x3 == min(posortowane_a3):
                for sensor in posortowane_a3:
                    x_a3[sensor] = (max(posortowane_a3) - sensor) / r3
            elif x3 == max(posortowane_a3):
                for sensor in posortowane_a3:
                    x_a3[sensor] = (sensor - min(posortowane_a3)) / r3
            else:
                for sensor in posortowane_a3:
                    x_a3[sensor] = (1 - (abs(x3 - sensor)) / r3)

            for key in x_a3:
                if x_a3[key] == 0:
                    x_a3[key] = 0.1

            if x4 == min(posortowane_a4):
                for sensor in posortowane_a4:
                    x_a4[sensor] = (max(posortowane_a4) - sensor) / r4
            elif x4 == max(posortowane_a4):
                for sensor in posortowane_a4:
                    x_a4[sensor] = (sensor - min(posortowane_a4)) / r4
            else:
                for sensor in posortowane_a4:
                    x_a4[sensor] = (1 - (abs(x4 - sensor)) / r4)

            for key in x_a4:
                if x_a4[key] == 0:
                    x_a4[key] = 0.1

            for value in x_a1:
                czas_a1[value] = (1/x_a1[value])

            for value in x_a2:
                czas_a2[value] = (1/x_a2[value])

            for value in x_a3:
                czas_a3[value] = (1/x_a3[value])

            for value in x_a4:
                czas_a4[value] = (1/x_a4[value])

            for key in neurony:
                pob_jedynki[key] = 0

            while len(czas_a1) > 0 or len(czas_a2) > 0 or len(czas_a3) > 0 or len(czas_a4) > 0:
                try:
                    lokal_min[min(czas_a1, key=czas_a1.get)] = czas_a1[min(czas_a1, key=czas_a1.get)]
                except:
                    lokal_min[2147483647] = 2147483647
                try:
                    lokal_min[min(czas_a2, key=czas_a2.get)] = czas_a2[min(czas_a2, key=czas_a2.get)]
                except:
                    lokal_min[2147483646] = 2147483646
                try:
                    lokal_min[min(czas_a3, key=czas_a3.get)] = czas_a3[min(czas_a3, key=czas_a3.get)]
                except:
                    lokal_min[2147483645] = 2147483645
                try:
                    lokal_min[min(czas_a4, key=czas_a4.get)] = czas_a4[min(czas_a4, key=czas_a4.get)]
                except:
                    lokal_min[2147483644] = 2147483644
                min_rec = min(lokal_min, key=lokal_min.get)

                for key in neurony:
                    if neurony[key][0] == min_rec:
                        pob_jedynki[key] = pob_jedynki[key] + 1
                        try:
                            czas_a1.pop(min_rec)
                        except:
                            continue
                        continue
                    elif neurony[key][1] == min_rec:
                        pob_jedynki[key] = pob_jedynki[key] + 1
                        try:
                            czas_a2.pop(min_rec)
                        except:
                            continue
                        continue
                    elif neurony[key][2] == min_rec:
                        pob_jedynki[key] = pob_jedynki[key] + 1
                        try:
                            czas_a3.pop(min_rec)
                        except:
                            continue
                        continue
                    elif neurony[key][3] == min_rec:
                        pob_jedynki[key] = pob_jedynki[key] + 1
                        try:
                            czas_a4.pop(min_rec)
                        except:
                            continue
                        continue
                    else:
                        continue

                for key in pob_jedynki:
                    if pob_jedynki[key] == 4 and key not in lista_neuronow:
                        lista_neuronow.append(key)
                lokal_min = {}

            print('\n')

            print("Klasyfikacja obiektu do klasy: " + str(neurony[lista_neuronow[0]][4]))
            print("Podobieństwo neuronów (od najbardziej do najmniej podobnego):")
            for key in lista_neuronow:
                print(neurony[key])

            lista_neuronow = []
            print('\n')

#wyjście
    elif numer == 7:
        break

