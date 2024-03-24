from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

def synthesize_graph(edges, weights, path, const):
    mirror_edges = [(edge[1], edge[0]) for edge in edges]
    mirror_graph = defaultdict(list)
    for edge, weight in zip(mirror_edges, weights):
        mirror_graph[edge[0]].append((edge[1], weight))
        mirror_graph[edge[1]].append((edge[0], weight))

    path_length = sum(weight for edge, weight in zip(edges, weights) if edge in zip(path[:-1], path[1:]))
    path_weights = [path_length / len(path)] * len(path)
    path_weights[0] += const
    path_weights[-1] -= const

    lambdas = {path[-1]: 0}
    for i in range(len(path) - 2, -1, -1):
        lambdas[path[i]] = lambdas[path[i + 1]] + path_weights[i]

    edge_weights = defaultdict(lambda: None)
    for edge in mirror_edges:
        if edge[0] in lambdas and edge[1] in lambdas:
            if lambdas[edge[0]] > lambdas[edge[1]] and edge[0] in path:
                edge_weights[edge] = lambdas[edge[0]] - lambdas[edge[1]] + 1
            else:
                edge_weights[edge] = max(lambdas[edge[0]] - lambdas[edge[1]], 1)
        else:
            if edge[0] in lambdas:
                min_neighbor = min(
                    edge[1] for edge in mirror_edges if edge[0] == edge[1] and lambdas[edge[1]] is not None)
                lambdas[edge[0]] += 1
            else:
                min_neighbor = min(
                    edge[0] for edge in mirror_edges if edge[1] == edge[0] and lambdas[edge[0]] is not None)
                lambdas[edge[1]] = lambdas[min_neighbor] + 1

    return edge_weights


def main():
    edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3), (3, 5), (5, 2), (2, 4), (4, 1), (2, 6), (3, 6)]
    weights = [6, 2, 5, 6, 2, 3, 10, 4, 10, 2, 6, 7]
    path = [1, 2, 3, 4, 5, 6]
    const = 5

    edge_weights = synthesize_graph(edges, weights, path, const)
    print(edge_weights)

    G = nx.Graph()
    G.add_nodes_from(range(1, 7))
    for edge, weight in zip(edges, weights):
        G.add_edge(*edge, weight=weight)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='black', linewidths=1,
            font_size=15)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Додавання ваг на ребра
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()

if __name__ == "__main__":
    main()
