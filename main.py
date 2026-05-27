from data import get_problem_data
from graph_model import SettlementGraph
from optimizer import PatrolOptimizer
# from solution_verifier import verify_solution, analyze_coverage_distribution, display_detailed_solution


def main():

    print("PROBLEM OPTYMALIZACJI ROZMIESZCZENIA PATROLI POLICYJNYCH")

    # Krok 1: Wczytanie danych
    print("\n[Krok 1] Wczytanie danych")
    num_settlements, num_patrols, populations, adjacency_list = get_problem_data()
    print(f"  Wczytano {num_settlements} osiedli")
    print(f"  Dostępnych patroli: {num_patrols}")

    # Krok 2: Budowa grafu
    print("\n[Krok 2] Budowa grafu")
    graph = SettlementGraph(populations, adjacency_list)
    print(f"  Graf zbudowany: {len(graph.get_all_settlements())} węzłów, {graph.graph.number_of_edges()} krawędzi")

    # Statystyki grafu
    total_population = sum(populations.values())
    avg_degree = sum(graph.get_degree(s) for s in graph.get_all_settlements()) / num_settlements
    print(f"  Łączna populacja: {total_population} mieszkańców")
    print(f"  Średni stopień węzła: {avg_degree:.2f}")

    # Krok 3: Optymalizacja
    print("\n[Krok 3] Uruchomienie optymalizatora")
    optimizer = PatrolOptimizer(graph, num_patrols)
    solution = optimizer.optimize()

    # Krok 4: Weryfikacja
    # print("\n[Krok 4] Weryfikacja rozwiązania")
    # is_valid, messages = verify_solution(graph, solution, num_patrols)

    # if not is_valid:
    #     print("\n[BŁĄD] Rozwiązanie nie przeszło weryfikacji!")
    #     return 1

    # Krok 5: Analiza i wyświetlenie wyników
    # print("\n[Krok 5] Analiza rozwiązania...")
    # stats = analyze_coverage_distribution(graph, solution)

    # Wyświetl szczegółowe rozwiązanie
    # display_detailed_solution(graph, solution)

    print("\n" + "PODSUMOWANIE ROZWIĄZANIA")
    print(f"Minimalne pokrycie N: {solution['optimal_n']}")
    print(f"Suma populacji w osiedlach z patrolami: {solution['total_population']} / {total_population}")
    print(f"Procent populacji pokryty: {solution['total_population'] / total_population * 100:.1f}%")
    print(f"Liczba osiedli z patrolami: {len(solution['patrolled_settlements'])} / {num_settlements}")
    print(f"\nOsiedla z patrolami:")
    for settlement_id in solution['patrolled_settlements']:
        pop = graph.get_population(settlement_id)
        print(f"  Osiedle {settlement_id}: populacja={pop}")

    print("\nZapisywanie grafu")
    graph.visualize(patrol_assignment=solution['assignment'],
                       save_path='solution_visualization.png')

    print("\nZakończono pomyślnie!")
    return 0

if __name__ == '__main__':
    exit_code = main()
    exit(exit_code)
