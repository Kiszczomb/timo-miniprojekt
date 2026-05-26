"""
Model grafu osiedli używający NetworkX.
"""

import networkx as nx
import matplotlib.pyplot as plt


class SettlementGraph:
    """
    Reprezentuje graf osiedli z populacjami i sąsiedztwami.
    """

    def __init__(self, populations, adjacency_list):
        """
        Inicjalizuje graf osiedli.

        Args:
            populations: słownik {settlement_id: population}
            adjacency_list: słownik {settlement_id: [neighbor_ids]}
        """
        self.graph = nx.Graph()
        self.populations = populations

        # Dodaj węzły z atrybutem populacji
        for settlement_id, population in populations.items():
            self.graph.add_node(settlement_id, population=population)

        # Dodaj krawędzie na podstawie listy sąsiedztwa
        for settlement_id, neighbors in adjacency_list.items():
            for neighbor_id in neighbors:
                # Dodaj krawędź tylko jeśli jeszcze nie istnieje (graf nieskierowany)
                if not self.graph.has_edge(settlement_id, neighbor_id):
                    self.graph.add_edge(settlement_id, neighbor_id)

    def get_neighbors(self, settlement_id):
        """
        Zwraca listę sąsiednich osiedli.

        Args:
            settlement_id: ID osiedla

        Returns:
            list: Lista ID sąsiednich osiedli
        """
        return list(self.graph.neighbors(settlement_id))

    def get_population(self, settlement_id):
        """
        Zwraca populację osiedla.

        Args:
            settlement_id: ID osiedla

        Returns:
            int: Populacja osiedla
        """
        return self.populations.get(settlement_id, 0)

    def get_degree(self, settlement_id):
        """
        Zwraca stopień węzła (liczbę sąsiadów).

        Args:
            settlement_id: ID osiedla

        Returns:
            int: Liczba sąsiadów
        """
        return self.graph.degree(settlement_id)

    def get_all_settlements(self):
        """
        Zwraca listę wszystkich osiedli.

        Returns:
            list: Lista ID wszystkich osiedli
        """
        return list(self.graph.nodes())

    def visualize(self, patrol_assignment=None, save_path=None):
        """
        Rysuje graf z opcjonalnym zaznaczeniem patroli.

        Args:
            patrol_assignment: słownik {settlement_id: 0/1} (1 = patrol obecny)
            save_path: opcjonalna ścieżka do zapisu obrazka
        """
        plt.figure(figsize=(12, 10))

        # Użyj spring layout dla czytelnego rozmieszczenia
        pos = nx.spring_layout(self.graph, seed=42)

        # Przygotuj kolory węzłów
        if patrol_assignment:
            node_colors = ['red' if patrol_assignment.get(node, 0) == 1 else 'lightblue'
                          for node in self.graph.nodes()]
        else:
            node_colors = 'lightblue'

        # Przygotuj rozmiary węzłów proporcjonalne do populacji
        node_sizes = [self.get_population(node) * 20 for node in self.graph.nodes()]

        # Rysuj graf
        nx.draw_networkx_nodes(self.graph, pos, node_color=node_colors,
                              node_size=node_sizes, alpha=0.8)
        nx.draw_networkx_edges(self.graph, pos, alpha=0.3, width=1)
        nx.draw_networkx_labels(self.graph, pos, font_size=8, font_weight='bold')

        plt.title("Graf osiedli, patrole zaznaczone na czerwono", fontsize=14)
        plt.axis('off')
        plt.tight_layout()

        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
            print(f"Wizualizacja zapisana do: {save_path}")
        else:
            plt.show()

        plt.close()


if __name__ == '__main__':
    # Test modelu grafu
    from data_parser import parse_data_txt

    _, _, populations, adjacency_list = parse_data_txt('data.txt')

    graph = SettlementGraph(populations, adjacency_list)

    print("Test modelu grafu:")
    print(f"Liczba węzłów: {len(graph.get_all_settlements())}")
    print(f"Liczba krawędzi: {graph.graph.number_of_edges()}")
    print(f"\nOsiedle 1:")
    print(f"  Populacja: {graph.get_population(1)}")
    print(f"  Sąsiedzi: {graph.get_neighbors(1)}")
    print(f"  Stopień: {graph.get_degree(1)}")

    # Znajdź osiedle o największym stopniu
    max_degree_settlement = max(graph.get_all_settlements(),
                               key=lambda x: graph.get_degree(x))
    print(f"\nOsiedle o największym stopniu: {max_degree_settlement}")
    print(f"  Stopień: {graph.get_degree(max_degree_settlement)}")
    print(f"  Sąsiedzi: {graph.get_neighbors(max_degree_settlement)}")
