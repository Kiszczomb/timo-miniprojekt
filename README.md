# timo-miniprojekt
Miniprojekt na zajęcia z Teorii i Metod Optymalizacji na kierunku AIR II

## Treść zadania

LP1. Średniej wielkości miasto w zachodniej Indonezji podzielone jest na 24 osiedla: Policja ma do dyspozycji tylko 15 patroli i musi zdecydować, na które osiedla patrole powinny być wysłane. Aby to zrobić, patrole mają być rozmieszczone w taki sposób, że dla każdego osiedla na tym osiedlu oraz na osiedlach bezpośrednio z nim graniczących ma znaleźć się co najmniej N patroli, przy czym N ma być największe możliwe. Dodatkowo, aby lepiej pokryć najbardziej zaludnione części miasta, suma liczby mieszkańców osiedli, w których pojawią się patrole, ma być największa możliwa przy uwzględnieniu maksymalizacji głównej funkcji celu, czyli liczby N. Populacja (w tysiącach) poszczególnych osiedli zadana jest w tabeli: 

| Osiedle | Populacja | Osiedle | Populacja | Osiedle | Populacja |
|---|---|---|---|---|---|
1 | 25 |9 |34 |17 |9
2 | 18 |10 |15 |18 |12
3 |32 |11 |12 |19 |19
4 |20 |12 |29 |20 |7
5 |35 |13 |24 |21 |10
6 |45 |14 |11 |22 |5
7 |25 |15 |10 |23 |8
8 |50 |16 |8 |24 |7

Rozwiąż zadanie programowania całkowitoliczbowego, umożliwiające przypisanie patroli do osiedli.

## Metoda 1 - wagowa


Zmaksymalizować: `10000 * N + suma(populacja_i * x_i for i in osiedla)`

Przy ograniczeniach:
```
Liczba_Dostepnych_Patroli: Patrol_1 + Patrol_10 + Patrol_11 + Patrol_12
 + Patrol_13 + Patrol_14 + Patrol_15 + Patrol_16 + Patrol_17 + Patrol_18
 + Patrol_19 + Patrol_2 + Patrol_20 + Patrol_21 + Patrol_22 + Patrol_23
 + Patrol_24 + Patrol_3 + Patrol_4 + Patrol_5 + Patrol_6 + Patrol_7 + Patrol_8
 + Patrol_9 = 15

Zasieg_Patroli_Osiedle_1: - N + Patrol_1 + Patrol_2 + Patrol_3 + Patrol_6
 + Patrol_7 + Patrol_9 >= 0

...

Zasieg_Patroli_Osiedle_24: - N + Patrol_11 + Patrol_14 + Patrol_24 >= 0

VARIABLES
0 <= N <= 24 Integer
0 <= Patrol_1 <= 1 Integer
...
0 <= Patrol_24 <= 1 Integer
```


