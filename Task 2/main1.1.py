import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Створення графа
G = nx.Graph()

# Додавання вершин та ребер
G.add_nodes_from(range(1, 5))
edges = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)]

G.add_edges_from(edges)

# Виведення матриці суміжності
adjacency_matrix = nx.adjacency_matrix(G).todense()
print("Матриця суміжності:")
print(adjacency_matrix)

# Виведення матриці інцидентності
incidence_matrix = nx.incidence_matrix(G, oriented=True).todense()
print("\nМатриця інцидентності:")
print(incidence_matrix)

# Виведення графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='lightblue', font_size=8, font_color='black', font_family='arial')
plt.title("Граф")
plt.show()
