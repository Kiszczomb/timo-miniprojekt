# PROBLEM OPTYMALIZACJI ROZMIESZCZENIA PATROLI POLICYJNYCH

## Oznaczenia

| Symbol | Znaczenie | Dziedzina |
|--------|-----------|-----------|
| $V = \{1, 2, \dots, 24\}$ | zbiór osiedli | — |
| $x_i$ | $x_i = 1$ jeśli patrol stoi w osiedlu $i$, inaczej $0$ | $\{0, 1\}$ (binarna) |
| $N$ | minimalne pokrycie (zmienna pomocnicza, tylko Faza 1) | $\{0, 1, \dots, 15\}$ (całkowita) |
| $p_i$ | populacja osiedla $i$ | dane wejściowe |
| $\mathcal{N}[i]$ | sąsiedztwo osiedla $i$ | — |
| $P = 15$ | liczba dostępnych patroli | stała |

**Pokrycie osiedla** $i$ to liczba patroli w nim samym oraz u jego sąsiadów:

$$\mathrm{cov}(i) = x_i + \sum_{j \in \text{sąsiedzi}(i)} x_j = \sum_{j \in \mathcal{N}[i]} x_j$$

<!-- ### Dane: populacja osiedli

| $i$ | $p_i$ | $i$ | $p_i$ | $i$ | $p_i$ | $i$ | $p_i$ |
|----:|------:|----:|------:|----:|------:|----:|------:|
| 1 | 25 | 7 | 25 | 13 | 24 | 19 | 19 |
| 2 | 18 | 8 | 50 | 14 | 11 | 20 | 7 |
| 3 | 32 | 9 | 34 | 15 | 10 | 21 | 10 |
| 4 | 20 | 10 | 15 | 16 | 8 | 22 | 5 |
| 5 | 35 | 11 | 12 | 17 | 9 | 23 | 8 |
| 6 | 45 | 12 | 29 | 18 | 12 | 24 | 7 |

### Sąsiedztwa $\mathcal{N}[i]$

Te zbiory definiują lewe strony wszystkich ograniczeń pokrycia:

| $i$ | $\mathcal{N}[i]$ | $i$ | $\mathcal{N}[i]$ |
|----:|------------------|----:|------------------|
| 1 | {1, 2, 3, 6, 7, 9} | 13 | {6, 7, 13, 14, 20} |
| 2 | {1, 2, 3, 4, 5, 6, 21} | 14 | {7, 9, 11, 13, 14, 24} |
| 3 | {1, 2, 3, 8, 9, 15, 21} | 15 | {3, 8, 15, 16, 21} |
| 4 | {2, 4, 5, 10, 12, 21, 22} | 16 | {8, 11, 15, 16} |
| 5 | {2, 4, 5, 6, 10, 19} | 17 | {10, 12, 17, 18, 23} |
| 6 | {1, 2, 5, 6, 7, 13, 19, 20} | 18 | {10, 17, 18, 19} |
| 7 | {1, 6, 7, 9, 13, 14} | 19 | {5, 6, 10, 18, 19, 20} |
| 8 | {3, 8, 9, 11, 15, 16} | 20 | {6, 13, 19, 20} |
| 9 | {1, 3, 7, 8, 9, 11, 14} | 21 | {2, 3, 4, 15, 21, 22} |
| 10 | {4, 5, 10, 12, 17, 18, 19} | 22 | {4, 12, 21, 22, 23} |
| 11 | {8, 9, 11, 14, 16, 24} | 23 | {12, 17, 22, 23} |
| 12 | {4, 10, 12, 17, 22, 23} | 24 | {11, 14, 24} |

--- -->

## Faza 1 — Maksymalizacja minimalnego pokrycia ($N$)

Cel: rozmieścić patrole tak, aby **najsłabiej chronione** osiedle było chronione
jak najlepiej (sprawiedliwość typu *max–min*).

**Funkcja celu**

$$\max \; N$$

**Ograniczenia**

$$\sum_{j \in \mathcal{N}[i]} x_j \;\ge\; N \qquad \forall\, i \in V \quad (\text{24 ograniczenia pokrycia})$$

$$\sum_{i \in V} x_i = 15 \qquad (\text{dokładnie 15 patroli})$$

$$x_i \in \{0, 1\}, \quad N \in \{0, 1, \dots, 15\}$$

**Wynik tej fazy:** $N^{*} = 3$ (przenoszone do Fazy 2 jako stała).

---

## Faza 2 — Maksymalizacja populacji przy ustalonym $N^{*}$

Cel: spośród rozmieszczeń gwarantujących minimalne pokrycie $N^{*} = 3$ wybrać to,
które chroni **największą łączną populację**.

**Funkcja celu**

$$\max \; \sum_{i \in V} p_i \, x_i$$

co po podstawieniu populacji daje:

$$\max \; \big(25x_1 + 18x_2 + 32x_3 + 20x_4 + 35x_5 + 45x_6 + 25x_7 + 50x_8 + 34x_9$$
$$+\, 15x_{10} + 12x_{11} + 29x_{12} + 24x_{13} + 11x_{14} + 10x_{15} + 8x_{16} + 9x_{17}$$
$$+\, 12x_{18} + 19x_{19} + 7x_{20} + 10x_{21} + 5x_{22} + 8x_{23} + 7x_{24}\big)$$

**Ograniczenia**

$$\sum_{j \in \mathcal{N}[i]} x_j \;\ge\; 3 \qquad \forall\, i \in V \quad (N^{*} \text{ wstawione na stałe})$$

$$\sum_{i \in V} x_i = 15$$

$$x_i \in \{0, 1\}$$

---

## Ograniczenia pokrycia — postać rozwinięta

Dla kompletności, każde z 24 ograniczeń pokrycia zapisane jawnie
(w Fazie 1 prawa strona to $N$, w Fazie 2 to $3$):

| # | Ograniczenie |
|---|--------------|
| 1  | $x_1 + x_2 + x_3 + x_6 + x_7 + x_9 \ge N$ |
| 2  | $x_1 + x_2 + x_3 + x_4 + x_5 + x_6 + x_{21} \ge N$ |
| 3  | $x_1 + x_2 + x_3 + x_8 + x_9 + x_{15} + x_{21} \ge N$ |
| 4  | $x_2 + x_4 + x_5 + x_{10} + x_{12} + x_{21} + x_{22} \ge N$ |
| 5  | $x_2 + x_4 + x_5 + x_6 + x_{10} + x_{19} \ge N$ |
| 6  | $x_1 + x_2 + x_5 + x_6 + x_7 + x_{13} + x_{19} + x_{20} \ge N$ |
| 7  | $x_1 + x_6 + x_7 + x_9 + x_{13} + x_{14} \ge N$ |
| 8  | $x_3 + x_8 + x_9 + x_{11} + x_{15} + x_{16} \ge N$ |
| 9  | $x_1 + x_3 + x_7 + x_8 + x_9 + x_{11} + x_{14} \ge N$ |
| 10 | $x_4 + x_5 + x_{10} + x_{12} + x_{17} + x_{18} + x_{19} \ge N$ |
| 11 | $x_8 + x_9 + x_{11} + x_{14} + x_{16} + x_{24} \ge N$ |
| 12 | $x_4 + x_{10} + x_{12} + x_{17} + x_{22} + x_{23} \ge N$ |
| 13 | $x_6 + x_7 + x_{13} + x_{14} + x_{20} \ge N$ |
| 14 | $x_7 + x_9 + x_{11} + x_{13} + x_{14} + x_{24} \ge N$ |
| 15 | $x_3 + x_8 + x_{15} + x_{16} + x_{21} \ge N$ |
| 16 | $x_8 + x_{11} + x_{15} + x_{16} \ge N$ |
| 17 | $x_{10} + x_{12} + x_{17} + x_{18} + x_{23} \ge N$ |
| 18 | $x_{10} + x_{17} + x_{18} + x_{19} \ge N$ |
| 19 | $x_5 + x_6 + x_{10} + x_{18} + x_{19} + x_{20} \ge N$ |
| 20 | $x_6 + x_{13} + x_{19} + x_{20} \ge N$ |
| 21 | $x_2 + x_3 + x_4 + x_{15} + x_{21} + x_{22} \ge N$ |
| 22 | $x_4 + x_{12} + x_{21} + x_{22} + x_{23} \ge N$ |
| 23 | $x_{12} + x_{17} + x_{22} + x_{23} \ge N$ |
| 24 | $x_{11} + x_{14} + x_{24} \ge N$ |
