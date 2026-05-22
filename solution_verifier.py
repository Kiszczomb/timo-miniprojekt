"""
Weryfikator poprawności rozwiązania problemu rozmieszczenia patroli.
"""


def verify_solution(graph, solution, num_patrols):
    """
    Kompleksowa weryfikacja rozwiązania.

    Sprawdza:
    1. Dokładnie num_patrols patroli przydzielonych
    2. Każde osiedle ma co najmniej N pokrycia
    3. N jest rzeczywiście minimalnym pokryciem
    4. Poprawność obliczenia sumy populacji

    Args:
        graph: Obiekt SettlementGraph
        solution: Słownik z rozwiązaniem (z klucze: optimal_n, assignment, total_population)
        num_patrols: Oczekiwana liczba patroli

    Returns:
        tuple: (is_valid, list_of_messages)
    """
    messages = []
    assignment = solution['assignment']
    optimal_n = solution['optimal_n']

    print("\n" + "=" * 60)
    print("WERYFIKACJA ROZWIĄZANIA")
    print("=" * 60)

    # Sprawdzenie 1: Łączna liczba patroli
    total_assigned = sum(assignment.values())
    print(f"\n1. Liczba patroli: {total_assigned} (oczekiwano {num_patrols})")
    if total_assigned != num_patrols:
        messages.append(f"BŁĄD: Oczekiwano {num_patrols} patroli, przydzielono {total_assigned}")
    else:
        print("   [OK] Poprawna liczba patroli")

    # Sprawdzenie 2: Pokrycie dla każdego osiedla
    print(f"\n2. Weryfikacja minimalnego pokrycia N = {optimal_n}:")
    min_coverage_found = float('inf')
    settlements_below_n = []

    for settlement_id in graph.get_all_settlements():
        neighbors = graph.get_neighbors(settlement_id)
        coverage = assignment[settlement_id] + sum(
            assignment[neighbor] for neighbor in neighbors
        )
        min_coverage_found = min(min_coverage_found, coverage)

        if coverage < optimal_n:
            settlements_below_n.append(settlement_id)
            messages.append(
                f"BŁĄD: Osiedle {settlement_id} ma pokrycie {coverage} < N={optimal_n}"
            )

    if settlements_below_n:
        print(f"   [BLAD] {len(settlements_below_n)} osiedli ma pokrycie poniżej N")
    else:
        print("   [OK] Wszystkie osiedla mają pokrycie >= N")

    # Sprawdzenie 3: N jest rzeczywiście minimum
    print(f"\n3. Weryfikacja czy N jest minimum:")
    print(f"   Minimalne znalezione pokrycie: {min_coverage_found}")
    print(f"   Zadeklarowane N: {optimal_n}")
    if min_coverage_found != optimal_n:
        messages.append(
            f"BŁĄD: Zadeklarowano N={optimal_n}, ale rzeczywiste minimum to {min_coverage_found}"
        )
        print(f"   [BLAD] Niezgodność!")
    else:
        print("   [OK] N jest poprawnie zidentyfikowane jako minimum")

    # Sprawdzenie 4: Suma populacji
    print(f"\n4. Weryfikacja sumy populacji:")
    expected_pop = sum(
        graph.get_population(i) * assignment[i]
        for i in graph.get_all_settlements()
    )
    print(f"   Obliczona suma populacji: {expected_pop}")
    print(f"   Zadeklarowana suma populacji: {solution['total_population']}")
    if expected_pop != solution['total_population']:
        messages.append(
            f"BŁĄD: Niezgodność populacji - oczekiwano {expected_pop}, otrzymano {solution['total_population']}"
        )
        print(f"   [BLAD] Niezgodność!")
    else:
        print("   [OK] Suma populacji poprawna")

    # Podsumowanie
    is_valid = len(messages) == 0
    print("\n" + "=" * 60)
    if is_valid:
        print("WYNIK WERYFIKACJI: [OK] ROZWIAZANIE POPRAWNE")
    else:
        print("WYNIK WERYFIKACJI: [BLAD] ZNALEZIONO BLEDY")
        for msg in messages:
            print(f"  - {msg}")
    print("=" * 60)

    return is_valid, messages


def analyze_coverage_distribution(graph, solution):
    """
    Analizuje rozkład pokrycia w osiedlach.

    Args:
        graph: Obiekt SettlementGraph
        solution: Słownik z rozwiązaniem

    Returns:
        dict: Statystyki pokrycia
    """
    assignment = solution['assignment']
    coverage_counts = {}

    for settlement_id in graph.get_all_settlements():
        neighbors = graph.get_neighbors(settlement_id)
        coverage = assignment[settlement_id] + sum(
            assignment[neighbor] for neighbor in neighbors
        )
        coverage_counts[settlement_id] = coverage

    stats = {
        'min_coverage': min(coverage_counts.values()),
        'max_coverage': max(coverage_counts.values()),
        'avg_coverage': sum(coverage_counts.values()) / len(coverage_counts),
        'coverage_by_settlement': coverage_counts
    }

    print("\n" + "=" * 60)
    print("STATYSTYKI POKRYCIA")
    print("=" * 60)
    print(f"Minimalne pokrycie: {stats['min_coverage']}")
    print(f"Maksymalne pokrycie: {stats['max_coverage']}")
    print(f"Średnie pokrycie: {stats['avg_coverage']:.2f}")

    # Rozkład pokrycia
    coverage_distribution = {}
    for coverage in coverage_counts.values():
        coverage_distribution[coverage] = coverage_distribution.get(coverage, 0) + 1

    print("\nRozkład pokrycia:")
    for coverage_level in sorted(coverage_distribution.keys()):
        count = coverage_distribution[coverage_level]
        print(f"  {coverage_level} patroli: {count} osiedli")

    return stats


def display_detailed_solution(graph, solution):
    """
    Wyświetla szczegółowe informacje o rozwiązaniu.

    Args:
        graph: Obiekt SettlementGraph
        solution: Słownik z rozwiązaniem
    """
    assignment = solution['assignment']
    patrolled = solution['patrolled_settlements']

    print("\n" + "=" * 60)
    print("SZCZEGÓŁOWE ROZWIĄZANIE")
    print("=" * 60)

    print("\nOsiedla z patrolami:")
    print("-" * 60)
    print(f"{'ID':<5} {'Populacja':<12} {'Sąsiedzi':<30}")
    print("-" * 60)

    total_pop = 0
    for settlement_id in patrolled:
        pop = graph.get_population(settlement_id)
        neighbors = graph.get_neighbors(settlement_id)
        total_pop += pop
        print(f"{settlement_id:<5} {pop:<12} {str(neighbors):<30}")

    print("-" * 60)
    print(f"Łączna populacja: {total_pop}")

    print("\nPokrycie dla każdego osiedla:")
    print("-" * 60)
    print(f"{'ID':<5} {'Ma patrol?':<12} {'Pokrycie':<10} {'Sąsiedzi z patrolami':<30}")
    print("-" * 60)

    for settlement_id in sorted(graph.get_all_settlements()):
        has_patrol = "TAK" if assignment[settlement_id] == 1 else "NIE"
        neighbors = graph.get_neighbors(settlement_id)
        coverage = assignment[settlement_id] + sum(
            assignment[neighbor] for neighbor in neighbors
        )
        patrolled_neighbors = [n for n in neighbors if assignment[n] == 1]

        print(f"{settlement_id:<5} {has_patrol:<12} {coverage:<10} {str(patrolled_neighbors):<30}")

    print("-" * 60)


if __name__ == '__main__':
    # Test weryfikatora
    from data_parser import parse_data_txt
    from graph_model import SettlementGraph
    from optimizer import PatrolOptimizer

    print("Test weryfikatora...\n")

    # Wczytaj dane
    num_settlements, num_patrols, populations, adjacency_list = parse_data_txt('data.txt')

    # Stwórz graf
    graph = SettlementGraph(populations, adjacency_list)

    # Uruchom optymalizator
    optimizer = PatrolOptimizer(graph, num_patrols)
    solution = optimizer.optimize()

    # Zweryfikuj rozwiązanie
    is_valid, messages = verify_solution(graph, solution, num_patrols)

    # Analizuj rozkład pokrycia
    stats = analyze_coverage_distribution(graph, solution)

    # Wyświetl szczegóły
    display_detailed_solution(graph, solution)
