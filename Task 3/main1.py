# import networkx as nx
# import matplotlib.pyplot as plt
# import random
#
# # Створення графа
# G = nx.Graph()
#
# # Додавання вершин
# G.add_nodes_from([1, 2, 3, 4, 5, 6])
# # G.add_nodes_from([1, 2, 3, 4, 5])
#
# # Додавання ребер
# # G.add_edges_from([(7, 2), (1, 7), (1, 2), (1, 3), (1, 4), (2, 3), (2, 5), (3, 4), (3, 5), (4, 5), (1, 5), (7, 6), (4, 6)])
# G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3), (3, 5), (5, 2), (2, 4), (4, 1), (2, 6), (3, 6)])
#
# # Функція для генерування ваги ребра від 1 до 10
# def generate_weight():
#     return random.randint(1, 10)
#
# # Ініціалізація ваги ребер
# for u, v in G.edges():
#     G[u][v]['weight'] = generate_weight()
#
# # Відзначення ваги ребер
# edge_labels = {(u, v): f"{G[u][v]['weight']}" for u, v in G.edges()}
#
# # Шлях з вершини 5 до 6
# shortest_path = nx.shortest_path(G, source=5, target=6, weight='weight')
#
# # Виведення найкоротшого шляху та його довжини
# print("Мінімальний шлях від вершини 5 до вершини 6:", shortest_path)
# path_length = sum(G[shortest_path[i]][shortest_path[i+1]]['weight'] for i in range(len(shortest_path)-1))
# print("Довжина мінімального шляху:", path_length)
#
# # Візуалізація графа з відзначеним найкоротшим шляхом
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='lightblue', node_size=800)
# nx.draw_networkx_nodes(G, pos, nodelist=[5], node_color='red', node_size=800)
# nx.draw_networkx_nodes(G, pos, nodelist=[6], node_color='green', node_size=800)
# nx.draw_networkx_edges(G, pos, edgelist=[(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)], edge_color='red', width=2)
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
# plt.show()
import networkx as nx
import matplotlib.pyplot as plt

# Введення даних
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (1, 3), (3, 5), (5, 2), (2, 4), (4, 1), (2, 6), (3, 6)]
weights = [6, 2, 5, 6, 2, 3, 10, 4, 10, 2, 6, 7]

# Створення графа
G = nx.Graph()

# Додавання ребер та їх ваг
for edge, weight in zip(edges, weights):
    G.add_edge(edge[0], edge[1], weight=weight)

# Пошук найкоротшого шляху
shortest_path = nx.shortest_path(G, source=5, target=6)
print("Найкоротший шлях:", shortest_path)

# Візуалізація графа
pos = nx.spring_layout(G)  # Позиціонування вершин
nx.draw(G, pos, with_labels=True, font_weight='bold')  # Намалювати граф
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)  # Додати підписи ребер

# Виділення найкоротшого шляху зеленим кольором
path_edges = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='g', width=2)

plt.show()
