"""
Dwufazowy optymalizator ILP dla problemu rozmieszczenia patroli.
"""

import pulp


class PatrolOptimizer:
    """
    Optymalizator dwufazowy dla rozmieszczenia patroli.

    Faza 1: Maksymalizacja minimalnego pokrycia N
    Faza 2: Maksymalizacja populacji przy ustalonym N
    """

    def __init__(self, graph_model, num_patrols):
        """
        Inicjalizuje optymalizator.

        Args:
            graph_model: Obiekt SettlementGraph
            num_patrols: Liczba dostępnych patroli
        """
        self.graph = graph_model
        self.num_patrols = num_patrols
        self.optimal_n = None
        self.optimal_assignment = None
        self.settlements = self.graph.get_all_settlements()

    def phase1_maximize_n(self):

        print("Faza 1: Maksymalizacja minimalnego pokrycia N...")

        # Stwórz problem optymalizacyjny
        prob = pulp.LpProblem("MaximizeMinCoverage", pulp.LpMaximize)

        # Zmienne decyzyjne: x[i] = 1 jeśli patrol w osiedlu i, 0 inaczej
        x = pulp.LpVariable.dicts("patrol",
                                  self.settlements,
                                  cat='Binary')

        # Zmienna pomocnicza: N = minimalne pokrycie
        N = pulp.LpVariable("min_coverage", lowBound=0, upBound=self.num_patrols, cat='Integer')

        # Funkcja celu: maksymalizuj N
        prob += N, "Maximize_N"

        # Ograniczenie 1: Każde osiedle ma co najmniej N pokrycia
        for settlement_id in self.settlements:
            neighbors = self.graph.get_neighbors(settlement_id)
            # Pokrycie = patrol w osiedlu + patrole u sąsiadów
            coverage = x[settlement_id] + pulp.lpSum([x[neighbor] for neighbor in neighbors])
            prob += coverage >= N, f"MinCoverage_{settlement_id}"

        # Ograniczenie 2: Dokładnie num_patrols patroli
        prob += pulp.lpSum([x[i] for i in self.settlements]) == self.num_patrols, "TotalPatrols"

        # Rozwiąż problem
        print(prob)
        prob.solve(pulp.PULP_CBC_CMD(msg=0))

        # Sprawdź status
        if prob.status != pulp.LpStatusOptimal:
            raise ValueError(f"Problem nieoptymalny! Status: {pulp.LpStatus[prob.status]}")

        # Ekstraktuj wyniki
        optimal_n = int(N.varValue)
        assignment = {i: int(x[i].varValue) for i in self.settlements}

        print(f"  Optymalne N = {optimal_n}")
        print(f"  Status: {pulp.LpStatus[prob.status]}")

        return optimal_n, assignment

    def phase2_maximize_population(self, fixed_n):

        print(f"\nFaza 2: Maksymalizacja populacji przy N = {fixed_n}...")

        # Stwórz problem optymalizacyjny
        prob = pulp.LpProblem("MaximizePopulation", pulp.LpMaximize)

        # Zmienne decyzyjne: x[i] = 1 jeśli patrol w osiedlu i, 0 inaczej
        x = pulp.LpVariable.dicts("patrol",
                                  self.settlements,
                                  cat='Binary')

        # Funkcja celu: maksymalizuj sumę populacji osiedli z patrolami
        objective = pulp.lpSum([
            self.graph.get_population(i) * x[i]
            for i in self.settlements
        ])
        prob += objective, "Maximize_Population"

        # Ograniczenie 1: Każde osiedle ma co najmniej fixed_n pokrycia
        for settlement_id in self.settlements:
            neighbors = self.graph.get_neighbors(settlement_id)
            coverage = x[settlement_id] + pulp.lpSum([x[neighbor] for neighbor in neighbors])
            prob += coverage >= fixed_n, f"MinCoverage_{settlement_id}"

        # Ograniczenie 2: Dokładnie num_patrols patroli
        prob += pulp.lpSum([x[i] for i in self.settlements]) == self.num_patrols, "TotalPatrols"

        # Rozwiąż problem
        print(prob)
        prob.solve(pulp.PULP_CBC_CMD(msg=0))

        # Sprawdź status
        if prob.status != pulp.LpStatusOptimal:
            raise ValueError(f"Problem nieoptymalny! Status: {pulp.LpStatus[prob.status]}")

        # Ekstraktuj wyniki
        total_pop = sum(
            self.graph.get_population(i) * int(x[i].varValue)
            for i in self.settlements
        )
        assignment = {i: int(x[i].varValue) for i in self.settlements}

        print(f"  Suma populacji: {total_pop}")
        print(f"  Status: {pulp.LpStatus[prob.status]}")

        return total_pop, assignment

    def optimize(self):

        print("OPTYMALIZACJA DWUFAZOWA")

        # Faza 1: Maksymalizacja N
        optimal_n, assignment1 = self.phase1_maximize_n()

        # Faza 2: Maksymalizacja populacji przy ustalonym N
        total_pop, assignment2 = self.phase2_maximize_population(optimal_n)

        # Zapisz wyniki
        self.optimal_n = optimal_n
        self.optimal_assignment = assignment2

        # Lista osiedli z patrolami
        patrolled_settlements = sorted([i for i in assignment2 if assignment2[i] == 1])

        print("\n" + "ROZWIĄZANIE OPTYMALNE")

        return {
            'optimal_n': optimal_n,
            'assignment': assignment2,
            'total_population': total_pop,
            'patrolled_settlements': patrolled_settlements
        }