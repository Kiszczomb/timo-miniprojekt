# Problem Optymalizacji Rozmieszczenia Patroli Policyjnych

Rozwiązanie problemu optymalizacji rozmieszczenia patroli policyjnych w grafie osiedli przy użyciu dwufazowego programowania całkowitoliczbowego (ILP).

## 📋 Opis problemu

Miasto podzielone jest na **24 osiedla** tworzące graf sąsiedztwa. Policja ma do dyspozycji **15 patroli** i musi zdecydować, w których osiedlach je rozmieścić.

### Cele optymalizacji (leksykograficzne):

1. **Cel główny**: Maksymalizować **N** - minimalną liczbę patroli pokrywających każde osiedle
   - Osiedle jest "pokryte" przez patrole znajdujące się na nim samym oraz na osiedlach bezpośrednio z nim sąsiadujących

2. **Cel drugorzędny**: Przy optymalnym N, maksymalizować sumę populacji osiedli, w których znajdują się patrole

### Ograniczenia:

- Dokładnie 15 patroli do rozmieszczenia
- Każde osiedle może mieć maksymalnie 1 patrol (zmienna binarna)
- Każde osiedle musi mieć co najmniej N patroli pokrywających je

## 🎯 Rozwiązanie

### Podejście: Dwufazowe ILP (Integer Linear Programming)

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
- **Suma populacji: 316 / 470** (67.2% całkowitej populacji miasta)
- **15 osiedli z patrolami**: 3, 4, 6, 7, 8, 10, 11, 12, 13, 14, 15, 17, 19, 23, 24

#### Rozkład pokrycia:
- 13 osiedli: pokrycie = 3 patrole (minimum)
- 7 osiedli: pokrycie = 4 patrole
- 4 osiedla: pokrycie = 5 patroli (maksimum)
- Średnie pokrycie: **3.62 patrola**

## 📁 Struktura projektu

```
opt/
├── README.md                      # Ten plik
├── main.py                        # Program główny - punkt wejścia
├── data_hardcoded.py              # Dane problemu w kodzie
├── graph_model.py                 # Model grafu (NetworkX)
├── optimizer.py                   # Optymalizator dwufazowy ILP (PuLP)
├── solution_verifier.py           # Weryfikator poprawności rozwiązania
├── data_parser.py                 # Parser pliku data.txt (opcjonalny)
├── data.txt                       # Plik z danymi (opcjonalny)
├── solution_visualization.png     # Wizualizacja grafu (generowana)
└── zad.png                        # Wizualizacja zadania
```

### Opis modułów:

#### `main.py`
Główny program łączący wszystkie komponenty:
1. Wczytanie danych (z `data_hardcoded.py`)
2. Budowa grafu osiedli
3. Optymalizacja dwufazowa
4. Weryfikacja rozwiązania
5. Wyświetlenie wyników i statystyk
6. Generowanie wizualizacji

#### `data_hardcoded.py`
Zawiera funkcję `get_problem_data()` zwracającą:
- Liczba osiedli (24)
- Liczba patroli (15)
- Słownik populacji osiedli
- Graf sąsiedztwa (adjacency list)

#### `graph_model.py`
Klasa `SettlementGraph` wykorzystująca NetworkX:
- `get_neighbors(id)` - zwraca sąsiadów osiedla
- `get_population(id)` - zwraca populację osiedla
- `get_degree(id)` - zwraca liczbę sąsiadów
- `visualize(assignment)` - generuje wizualizację grafu

#### `optimizer.py`
Klasa `PatrolOptimizer` - solver ILP wykorzystujący PuLP:
- `phase1_maximize_n()` - maksymalizuje minimalne pokrycie N
- `phase2_maximize_population(N)` - maksymalizuje populację przy ustalonym N
- `optimize()` - wykonuje pełną optymalizację dwufazową

#### `solution_verifier.py`
Funkcje weryfikacyjne:
- `verify_solution()` - sprawdza poprawność rozwiązania
- `analyze_coverage_distribution()` - analizuje rozkład pokrycia
- `display_detailed_solution()` - wyświetla szczegóły rozwiązania

#### `data_parser.py` (opcjonalny)
Parser pliku `data.txt` - używany jeśli chcesz wczytać dane z pliku tekstowego zamiast z kodu.

## 🚀 Instalacja i uruchomienie

### Wymagania:
- Python 3.8+
- Biblioteki: `pulp`, `networkx`, `matplotlib`

### Instalacja bibliotek:

```bash
pip install pulp networkx matplotlib
```

lub na Windows z Python Launcher:

```bash
py -m pip install pulp networkx matplotlib
```

### Uruchomienie:

```bash
python main.py
```

lub na Windows:

```bash
py main.py
```

### Oczekiwane wyjście:

Program wyświetli:
1. Informacje o wczytanych danych
2. Statystyki grafu
3. Przebieg optymalizacji (Faza 1 i 2)
4. Weryfikację rozwiązania
5. Szczegółowe statystyki pokrycia
6. Tabelę z rozwiązaniem
7. Podsumowanie końcowe

Dodatkowo wygeneruje plik `solution_visualization.png` z graficzną reprezentacją rozwiązania (czerwone węzły = patrole).

## 📊 Przykładowe wyjście

```
======================================================================
PROBLEM OPTYMALIZACJI ROZMIESZCZENIA PATROLI POLICYJNYCH
======================================================================

[Krok 1] Wczytanie danych problemu...
  Wczytano 24 osiedli
  Dostępnych patroli: 15

[Krok 2] Budowa modelu grafu...
  Graf zbudowany: 24 węzłów, 55 krawędzi
  Łączna populacja: 470 mieszkańców
  Średni stopień węzła: 4.58

[Krok 3] Uruchomienie optymalizatora dwufazowego...
============================================================
OPTYMALIZACJA DWUFAZOWA
============================================================
Faza 1: Maksymalizacja minimalnego pokrycia N...
  Optymalne N = 3
  Status: Optimal

Faza 2: Maksymalizacja populacji przy N = 3...
  Suma populacji: 316
  Status: Optimal

[...]

======================================================================
PODSUMOWANIE ROZWIĄZANIA
======================================================================
Minimalne pokrycie N: 3
Suma populacji w osiedlach z patrolami: 316 / 470
Procent populacji pokryty: 67.2%
Liczba osiedli z patrolami: 15 / 24

Osiedla z patrolami:
  Osiedle 3: populacja=32, stopień=6
  Osiedle 4: populacja=20, stopień=6
  Osiedle 6: populacja=45, stopień=7
  Osiedle 7: populacja=25, stopień=5
  Osiedle 8: populacja=50, stopień=5
  [...]
======================================================================

[SUKCES] Program zakończony pomyślnie!
```

## 🔍 Testowanie poszczególnych modułów

### Test danych:
```bash
py data_hardcoded.py
```

### Test modelu grafu:
```bash
py graph_model.py
```

### Test optymalizatora:
```bash
py optimizer.py
```

### Test weryfikatora:
```bash
py solution_verifier.py
```

## 🧮 Technologie użyte

- **Python 3.12** - język programowania
- **PuLP** - biblioteka do programowania liniowego (ILP/MILP)
  - Solver: CBC (Coin-or Branch and Cut)
- **NetworkX** - biblioteka do pracy z grafami
- **Matplotlib** - wizualizacja grafów
- **NumPy** - operacje numeryczne (zależność matplotlib)

## 📈 Analiza rozwiązania

### Strategia wyboru osiedli:

Program wybiera osiedla optymalizując dwa kryteria:
1. **W Fazie 1**: Osiedla o wysokim stopniu (wiele połączeń), aby maksymalizować pokrycie
2. **W Fazie 2**: Osiedla o dużej populacji, przy zachowaniu minimalnego pokrycia N=3

### Najważniejsze osiedla z patrolami:
- **Osiedle 8**: największa populacja (50)
- **Osiedle 6**: największy stopień (7 sąsiadów) + duża populacja (45)
- **Osiedla 3, 4, 10**: wysokie stopnie (6 sąsiadów)

### Interpretacja wyników:

- Każde osiedle w mieście ma **co najmniej 3 patrole** w swoim sąsiedztwie
- **67.2%** populacji miasta mieszka w osiedlach z bezpośrednią obecnością patroli
- Rozwiązanie jest **optymalne matematycznie** (potwierdzone przez solver ILP)

## 🔧 Modyfikacja danych

Jeśli chcesz rozwiązać problem dla innych danych:

### Opcja 1: Modyfikacja `data_hardcoded.py`
Edytuj słowniki `populations` i `adjacency_list` w funkcji `get_problem_data()`.

### Opcja 2: Użycie pliku tekstowego
1. Stwórz plik podobny do `data.txt`
2. W `main.py` zmień import:
   ```python
   from data_parser import parse_data_txt
   # zamiast
   from data_hardcoded import get_problem_data
   ```
3. Zmień wywołanie:
   ```python
   num_settlements, num_patrols, populations, adjacency_list = parse_data_txt('twoj_plik.txt')
   ```

## 📝 Licencja

Projekt stworzony w celach edukacyjnych i badawczych.

## 👤 Autor

Program stworzony przez Claude Code (Anthropic)
Data: 2026-05-22

---

**Uwaga**: Program wymaga zainstalowanych bibliotek PuLP, NetworkX i Matplotlib. Solver CBC jest dołączony do PuLP i nie wymaga oddzielnej instalacji.
