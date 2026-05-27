# Notatnik

1. przygotowac równania dla obu podejść
2. graf ważony zrobić
3. Kod wyczyścić (+ parę razy przeczytać)

```
MAXIMIZE
10000*N + 25*Patrol_1 + 15*Patrol_10 + 12*Patrol_11 + 29*Patrol_12 + 24*Patrol_13 + 11*Patrol_14 + 10*Patrol_15 + 8*Patrol_16 + 9*Patrol_17 + 12*Patrol_18 + 19*Patrol_19 + 18*Patrol_2 + 7*Patrol_20 + 10*Patrol_21 + 5*Patrol_22 + 8*Patrol_23 + 7*Patrol_24 + 32*Patrol_3 + 20*Patrol_4 + 35*Patrol_5 + 45*Patrol_6 + 25*Patrol_7 + 50*Patrol_8 + 34*Patrol_9 + 0.0


SUBJECT TO
Liczba_Dostepnych_Patroli: Patrol_1 + Patrol_10 + Patrol_11 + Patrol_12
 + Patrol_13 + Patrol_14 + Patrol_15 + Patrol_16 + Patrol_17 + Patrol_18
 + Patrol_19 + Patrol_2 + Patrol_20 + Patrol_21 + Patrol_22 + Patrol_23
 + Patrol_24 + Patrol_3 + Patrol_4 + Patrol_5 + Patrol_6 + Patrol_7 + Patrol_8
 + Patrol_9 = 15

Zasieg_Patroli_Osiedle_1: - N + Patrol_1 + Patrol_2 + Patrol_3 + Patrol_6
 + Patrol_7 + Patrol_9 >= 0

Zasieg_Patroli_Osiedle_2: - N + Patrol_1 + Patrol_2 + Patrol_21 + Patrol_3
 + Patrol_4 + Patrol_5 + Patrol_6 >= 0

Zasieg_Patroli_Osiedle_3: - N + Patrol_1 + Patrol_15 + Patrol_2 + Patrol_21
 + Patrol_3 + Patrol_8 + Patrol_9 >= 0

Zasieg_Patroli_Osiedle_4: - N + Patrol_10 + Patrol_12 + Patrol_2 + Patrol_21
 + Patrol_22 + Patrol_4 + Patrol_5 >= 0

Zasieg_Patroli_Osiedle_5: - N + Patrol_10 + Patrol_19 + Patrol_2 + Patrol_4
 + Patrol_5 + Patrol_6 >= 0

Zasieg_Patroli_Osiedle_6: - N + Patrol_1 + Patrol_13 + Patrol_19 + Patrol_2
 + Patrol_20 + Patrol_5 + Patrol_6 + Patrol_7 >= 0

Zasieg_Patroli_Osiedle_7: - N + Patrol_1 + Patrol_13 + Patrol_14 + Patrol_6
 + Patrol_7 + Patrol_9 >= 0

Zasieg_Patroli_Osiedle_8: - N + Patrol_11 + Patrol_15 + Patrol_16 + Patrol_3
 + Patrol_8 + Patrol_9 >= 0

Zasieg_Patroli_Osiedle_9: - N + Patrol_1 + Patrol_11 + Patrol_14 + Patrol_3
 + Patrol_7 + Patrol_9 >= 0

Zasieg_Patroli_Osiedle_10: - N + Patrol_10 + Patrol_12 + Patrol_17 + Patrol_18
 + Patrol_19 + Patrol_4 + Patrol_5 >= 0

Zasieg_Patroli_Osiedle_11: - N + Patrol_11 + Patrol_14 + Patrol_16 + Patrol_24
 + Patrol_8 + Patrol_9 >= 0

Zasieg_Patroli_Osiedle_12: - N + Patrol_10 + Patrol_12 + Patrol_17 + Patrol_22
 + Patrol_23 + Patrol_4 >= 0

Zasieg_Patroli_Osiedle_13: - N + Patrol_13 + Patrol_14 + Patrol_20 + Patrol_6
 + Patrol_7 >= 0

Zasieg_Patroli_Osiedle_14: - N + Patrol_11 + Patrol_13 + Patrol_14 + Patrol_24
 + Patrol_7 + Patrol_9 >= 0

Zasieg_Patroli_Osiedle_15: - N + Patrol_15 + Patrol_16 + Patrol_21 + Patrol_3
 + Patrol_8 >= 0

Zasieg_Patroli_Osiedle_16: - N + Patrol_11 + Patrol_15 + Patrol_16 + Patrol_8
 >= 0

Zasieg_Patroli_Osiedle_17: - N + Patrol_10 + Patrol_12 + Patrol_17 + Patrol_18
 + Patrol_23 >= 0

Zasieg_Patroli_Osiedle_18: - N + Patrol_10 + Patrol_17 + Patrol_18 + Patrol_19
 >= 0

Zasieg_Patroli_Osiedle_19: - N + Patrol_10 + Patrol_18 + Patrol_19 + Patrol_20
 + Patrol_5 + Patrol_6 >= 0

Zasieg_Patroli_Osiedle_20: - N + Patrol_13 + Patrol_19 + Patrol_20 + Patrol_6
 >= 0

Zasieg_Patroli_Osiedle_21: - N + Patrol_15 + Patrol_2 + Patrol_21 + Patrol_22
 + Patrol_3 + Patrol_4 >= 0

Zasieg_Patroli_Osiedle_22: - N + Patrol_12 + Patrol_21 + Patrol_22 + Patrol_23
 + Patrol_4 >= 0

Zasieg_Patroli_Osiedle_23: - N + Patrol_12 + Patrol_17 + Patrol_22 + Patrol_23
 >= 0

Zasieg_Patroli_Osiedle_24: - N + Patrol_11 + Patrol_14 + Patrol_24 >= 0

VARIABLES
0 <= N Integer
0 <= Patrol_1 <= 1 Integer
0 <= Patrol_10 <= 1 Integer
0 <= Patrol_11 <= 1 Integer
0 <= Patrol_12 <= 1 Integer
0 <= Patrol_13 <= 1 Integer
0 <= Patrol_14 <= 1 Integer
0 <= Patrol_15 <= 1 Integer
0 <= Patrol_16 <= 1 Integer
0 <= Patrol_17 <= 1 Integer
0 <= Patrol_18 <= 1 Integer
0 <= Patrol_19 <= 1 Integer
0 <= Patrol_2 <= 1 Integer
0 <= Patrol_20 <= 1 Integer
0 <= Patrol_21 <= 1 Integer
0 <= Patrol_22 <= 1 Integer
0 <= Patrol_23 <= 1 Integer
0 <= Patrol_24 <= 1 Integer
0 <= Patrol_3 <= 1 Integer
0 <= Patrol_4 <= 1 Integer
0 <= Patrol_5 <= 1 Integer
0 <= Patrol_6 <= 1 Integer
0 <= Patrol_7 <= 1 Integer
0 <= Patrol_8 <= 1 Integer
0 <= Patrol_9 <= 1 Integer
```