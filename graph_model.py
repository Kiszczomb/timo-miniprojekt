import networkx as nx
import matplotlib.pyplot as plt


class SettlementGraph:

    def __init__(self, populations, adjacency_list):

        self.graph = nx.Graph()
        self.populations = populations

        # węzły z atrybutem populacji
        for settlement_id, population in populations.items():
            self.graph.add_node(settlement_id, population=population)

        # krawędzie na podstawie listy sąsiedztwa
        for settlement_id, neighbors in adjacency_list.items():
            for neighbor_id in neighbors:
                # Dodaj krawędź tylko jeśli jeszcze nie istnieje (graf nieskierowany)
                if not self.graph.has_edge(settlement_id, neighbor_id):
                    self.graph.add_edge(settlement_id, neighbor_id)

    def get_neighbors(self, settlement_id):

        return list(self.graph.neighbors(settlement_id))

    def get_population(self, settlement_id):

        return self.populations.get(settlement_id, 0)

    def get_degree(self, settlement_id):

        return self.graph.degree(settlement_id)

    def get_all_settlements(self):

        return list(self.graph.nodes())

    def visualize(self, patrol_assignment=None, save_path=None):

        plt.figure(figsize=(12, 10))

        pos = nx.spring_layout(self.graph, seed=42)

        # kolory węzłów
        if patrol_assignment:
            node_colors = ['red' if patrol_assignment.get(node, 0) == 1 else 'lightblue'
                          for node in self.graph.nodes()]
        else:
            node_colors = 'lightblue'

        # rozmiary węzłów proporcjonalne do populacji
        node_sizes = [self.get_population(node) * 20 for node in self.graph.nodes()]

        # Rysowanie
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