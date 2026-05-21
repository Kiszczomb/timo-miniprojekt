import pulp

# 1. Definicja danych wejściowych
populacja = {
    1: 25, 2: 18, 3: 32, 4: 20, 5: 35, 6: 45, 7: 25, 8: 50,
    9: 34, 10: 15, 11: 12, 12: 29, 13: 24, 14: 11, 15: 10, 16: 8,
    17: 9, 18: 12, 19: 19, 20: 7, 21: 10, 22: 5, 23: 8, 24: 7
}

osiedla = list(populacja.keys())
liczba_patroli = 15

# UWAGA: Miejsce na uzupełnienie grafu sąsiedztwa!
# Należy wpisać listy sąsiadów dla każdego z 24 osiedli.
# Poniżej znajduje się pusty słownik, który służy jako przykład/szablon.
sasiedzi = {i: [] for i in osiedla} 
# Przykład wypełnienia: 
# sasiedzi[1] = [2, 3, 5] 
# sasiedzi[2] = [1, 4]
# ... itd.

# 2. Inicjalizacja modelu
prob = pulp.LpProblem("Rozmieszczenie_Patroli", pulp.LpMaximize)

# 3. Zmienne decyzyjne
# Zmienna binarna x[i]: 1, jeśli na osiedlu 'i' umieszczono patrol, 0 w przeciwnym razie
x = pulp.LpVariable.dicts("Patrol", osiedla, cat=pulp.LpBinary)

# Zmienna całkowitoliczbowa N: minimalna liczba patroli w osiedlu i u jego sąsiadów
N = pulp.LpVariable("N", lowBound=0, cat=pulp.LpInteger)

# 4. Funkcja celu (Optymalizacja leksykograficzna/wagowa)
# Waga 10 000 dla N gwarantuje, że główny cel zdominuje cel podrzędny (populację).
# Cel podrzędny: suma mieszkańców z osiedli, na których umieszczono patrol.
prob += 10000 * N + pulp.lpSum([populacja[i] * x[i] for i in osiedla]), "Funkcja_Celu"

# 5. Ograniczenia
# Ograniczenie 1: Dokładnie 15 patroli do rozdysponowania
prob += pulp.lpSum([x[i] for i in osiedla]) == liczba_patroli, "Liczba_Dostepnych_Patroli"

# Ograniczenie 2: Na każdym osiedlu i u jego sąsiadów łącznie musi być >= N patroli
for i in osiedla:
    prob += x[i] + pulp.lpSum([x[j] for j in sasiedzi[i]]) >= N, f"Zasieg_Patroli_Osiedle_{i}"

# 6. Rozwiązanie problemu
prob.solve()

# 7. Prezentacja wyników
print(f"Status rozwiązania: {pulp.LpStatus[prob.status]}\n")

if prob.status == pulp.LpStatusOptimal:
    print(f"Maksymalna minimalna liczba patroli w sąsiedztwie (N): {int(N.varValue)}")
    
    wybrane_osiedla = [i for i in osiedla if x[i].varValue == 1]
    populacja_z_patrolem = sum(populacja[i] for i in wybrane_osiedla)
    
    print(f"Patrole zostaną wysłane na osiedla: {wybrane_osiedla}")
    print(f"Łączna populacja osiedli z patrolem: {populacja_z_patrolem} tysięcy mieszkańców")
    
    print("\nSzczegółowe pokrycie dla każdego osiedla (własny patrol + patrole sąsiadów):")
    for i in osiedla:
        pokrycie = int(x[i].varValue + sum(x[j].varValue for j in sasiedzi[i]))
        czy_patrol = "TAK" if x[i].varValue == 1 else "NIE"
        print(f"Osiedle {i:2d}: Patrol na miejscu: {czy_patrol}, Łącznie w zasięgu: {pokrycie}")
else:
    print("Nie udało się znaleźć optymalnego rozwiązania.")