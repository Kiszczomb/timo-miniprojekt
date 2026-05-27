# Problem Optymalizacji Rozmieszczenia Patroli Policyjnych

Rozwiązanie problemu optymalizacji rozmieszczenia patroli policyjnych w grafie osiedli przy użyciu dwufazowego programowania całkowitoliczbowego (ILP).

## Opis problemu

Miasto podzielone jest na **24 osiedla** tworzące graf sąsiedztwa. Policja ma do dyspozycji **15 patroli** i musi zdecydować, w których osiedlach je rozmieścić.

### Cele optymalizacji (leksykograficzne):

1. **Cel główny**: Maksymalizować **N** - minimalną liczbę patroli pokrywających każde osiedle
   - Osiedle jest "pokryte" przez patrole znajdujące się na nim samym oraz na osiedlach bezpośrednio z nim sąsiadujących

2. **Cel drugorzędny**: Przy optymalnym N, maksymalizować sumę populacji osiedli, w których znajdują się patrole

### Ograniczenia:

- Dokładnie 15 patroli do rozmieszczenia
- Każde osiedle może mieć maksymalnie 1 patrol (zmienna binarna)
- Każde osiedle musi mieć co najmniej N patroli pokrywających je

## Rozwiązanie

### Podejście: Dwufazowe programowanie całkowitoliczbowe

#### Faza 1: Maksymalizacja N
```
Zmienne: x[i] ∈ {0,1} dla każdego osiedla, N ∈ ℤ₊

Maksymalizuj: N

Ograniczenia:
  ∀i: x[i] + Σ(x[j], j∈sąsiedzi[i]) ≥ N
  Σx[i] = 15
```

#### Faza 2: Maksymalizacja populacji
```
Zmienne: x[i] ∈ {0,1} dla każdego osiedla

Maksymalizuj: Σ(populacja[i] × x[i])

Ograniczenia:
  ∀i: x[i] + Σ(x[j], j∈sąsiedzi[i]) ≥ N_opt  (N_opt z Fazy 1)
  Σx[i] = 15
```

### Wyniki optymalne

- **N = 3** - każde osiedle ma co najmniej 3 patrole pokrywające je
- **Suma populacji: 325 / 470** (67.2% całkowitej populacji miasta)
- **15 osiedli z patrolami**: 3, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 17, 19, 23, 24

#### Rozkład pokrycia:
- 13 osiedli: pokrycie = 3 patrole (minimum)
- 7 osiedli: pokrycie = 4 patrole
- 4 osiedla: pokrycie = 5 patroli (maksimum)
- Średnie pokrycie: **3.62 patrola**

## Technologie użyte

- **Python 3.12** - język programowania
- **PuLP** - biblioteka do programowania liniowego (ILP/MILP)
  - Solver: CBC (Coin-or Branch and Cut)
- **NetworkX** - biblioteka do pracy z grafami
- **Matplotlib** - wizualizacja grafów
- **NumPy** - operacje numeryczne (zależność matplotlib)
