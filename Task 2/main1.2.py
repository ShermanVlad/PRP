import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    # Ініціалізація відстаней та відстаней до кожної вершини
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Створення пріоритетної черги для вершин та їх відстаней
    priority_queue = [(0, start)]

    while priority_queue:
        # Вибір вершини з найменшою відстанню
        current_distance, current_vertex = priority_queue.pop(0)

        # Оновлення відстаней до сусідів поточної вершини
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']  # Отримання ваги ребра
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                priority_queue.append((distance, neighbor))
                priority_queue.sort()

    return distances

# Створення графа
G = nx.Graph()

# Додавання вершин та ребер
G.add_nodes_from(range(1, 21))
edges = [(1, 2, {'weight': 3}), (1, 3, {'weight': 2}), (2, 4, {'weight': 5}),
         (3, 5, {'weight': 1}), (4, 6, {'weight': 7}), (5, 7, {'weight': 4}),
         (6, 8, {'weight': 3}), (7, 9, {'weight': 6}), (8, 10, {'weight': 8}),
         (9, 11, {'weight': 2}), (10, 12, {'weight': 5}), (11, 13, {'weight': 4}),
         (12, 14, {'weight': 1}), (13, 15, {'weight': 7}), (14, 16, {'weight': 9}),
         (15, 17, {'weight': 3}), (16, 18, {'weight': 6}), (17, 19, {'weight': 4}),
         (18, 20, {'weight': 2}), (19, 20, {'weight': 5}), (1, 10, {'weight': 4}),
         (5, 15, {'weight': 8}), (11, 20, {'weight': 3})]

G.add_edges_from(edges)

# Задання початкової вершини для алгоритму Дейкстри
start_node = 1

# Виклик алгоритму Дейкстри
shortest_paths = dijkstra(G, start_node)

# Виведення результатів
print("Найкоротші шляхи від вершини {}:".format(start_node))
for vertex, distance in shortest_paths.items():
    print("Вершина {}: Відстань - {}".format(vertex, distance))

# Виведення графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='lightblue', font_size=8, font_color='black', font_family='arial')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
