import pulp
import networkx as nx
import matplotlib.pyplot as plt

def rysuj_graf(osiedla, sasiedzi, wybrane_osiedla, pokrycie_dict, populacja):
    # tworzenie grafu
    G = nx.Graph()
    G.add_nodes_from(osiedla)
    for i in osiedla:
        for j in sasiedzi[i]:
            G.add_edge(i, j)

    # config grafu
    pos = nx.spring_layout(G, seed=42) 
    node_sizes = [populacja[node] * 200 for node in G.nodes()]
    kolory = ['red' if node in wybrane_osiedla else 'gray' for node in G.nodes()]

    # etykiety
    etykiety = {node: f"{node}\n({pokrycie_dict[node]})" for node in G.nodes()}

    plt.figure(figsize=(12, 10))
    
    # rysuj graf
    nx.draw(G, pos, node_color=kolory, labels=etykiety, 
            node_size=node_sizes, font_weight='bold', font_color='white',
            edge_color='black', width=2)

    plt.show()



# 1. definicja danych wejściowych
populacja = {
    1: 25, 
    2: 18, 
    3: 32, 
    4: 20, 
    5: 35, 
    6: 45, 
    7: 25, 
    8: 50,
    9: 34, 
    10: 15, 
    11: 12, 
    12: 29, 
    13: 24, 
    14: 11, 
    15: 10, 
    16: 8,
    17: 9, 
    18: 12, 
    19: 19, 
    20: 7, 
    21: 10, 
    22: 5, 
    23: 8, 
    24: 7    
}

osiedla = list(populacja.keys())
liczba_patroli = 15

sasiedzi = {
    1: [2, 3, 6, 7, 9],
    2: [1, 3, 4, 5, 6, 21],
    3: [1, 2, 8, 9, 15, 21],
    4: [2, 5, 10, 12, 21, 22],
    5: [2, 4, 6, 10, 19],
    6: [1, 2, 5, 7, 13, 19, 20],
    7: [1, 6, 9, 13, 14],
    8: [3, 9, 11, 15, 16],
    9: [1, 3, 7, 11, 14],
    10: [4, 5, 12, 17, 18, 19],
    11: [8, 9, 14, 16, 24],
    12: [4, 10, 17, 22, 23],
    13: [6, 7, 14, 20],
    14: [7, 9, 11, 13, 24],
    15: [3, 8, 16, 21],
    16: [8, 11, 15],
    17: [10, 12, 18, 23],
    18: [10, 17, 19],
    19: [5, 6, 10, 18, 20],
    20: [6, 13, 19],
    21: [2, 3, 4, 15, 22],
    22: [4, 12, 21, 23],
    23: [12, 17, 22],
    24: [11, 14]
}

# 2. inicjalizacja modelu
prob = pulp.LpProblem("Rozmieszczenie_Patroli", pulp.LpMaximize)

# 3. zmienne decyzyjne
x = pulp.LpVariable.dicts("Patrol", osiedla, cat=pulp.LpBinary)

N = pulp.LpVariable("N", lowBound=0, upBound=len(osiedla), cat=pulp.LpInteger)

# 4. funkcja celu
prob += 10000 * N + pulp.lpSum([populacja[i] * x[i] for i in osiedla]), "Funkcja_Celu"

# 5. ograniczenia
prob += pulp.lpSum([x[i] for i in osiedla]) == liczba_patroli, "Liczba_Dostepnych_Patroli"

for i in osiedla:
    prob += x[i] + pulp.lpSum([x[j] for j in sasiedzi[i]]) >= N, f"Zasieg_Patroli_Osiedle_{i}"

print(prob)

# 6. rozwiązanie problemu
prob.solve(pulp.PULP_CBC_CMD(msg=True))

# 7. wyniki
print(10 * "=" + " WYNIKI " + 10 * "=")
print(f"[RESULT] Status rozwiązania: {pulp.LpStatus[prob.status]}\n")

if prob.status == pulp.LpStatusOptimal:
    print(f"[RESULT] Maksymalna minimalna liczba patroli w sąsiedztwie (N): {int(N.varValue)}")
    
    wybrane_osiedla = [i for i in osiedla if x[i].varValue == 1]
    populacja_z_patrolem = sum(populacja[i] for i in wybrane_osiedla)
    
    print(f"[RESULT] Osiedla z patrolem: {wybrane_osiedla}")
    print(f"[RESULT] Łączna populacja osiedli z patrolem: {populacja_z_patrolem} tys. mieszkańców")
    
    print(f"\n[RESULT] Szczegółowe pokrycie dla każdego osiedla (własny patrol + patrole sąsiadów):")
    for i in osiedla:
        pokrycie = int(x[i].varValue + sum(x[j].varValue for j in sasiedzi[i]))
        czy_patrol = "TAK" if x[i].varValue else "NIE"
        print(f"Osiedle {i:2d}: Patrol: {czy_patrol}, Łącznie w zasięgu: {pokrycie}")
else:
    print("Nie udało się znaleźć optymalnego rozwiązania.")
    
# if prob.status == pulp.LpStatusOptimal:
#     rysuj_mape(osiedla, sasiedzi, wybrane_osiedla)
    
# Wywołanie funkcji (upewnij się, że ten kod znajduje się wewnątrz bloku sprawdzającego status)
if prob.status == pulp.LpStatusOptimal:
    # Obliczamy pokrycie dla każdego osiedla i zapisujemy do słownika
    pokrycie_dict = {}
    for i in osiedla:
        pokrycie_dict[i] = int(x[i].varValue + sum(x[j].varValue for j in sasiedzi[i]))
        
    rysuj_graf(osiedla, sasiedzi, wybrane_osiedla, pokrycie_dict, populacja)