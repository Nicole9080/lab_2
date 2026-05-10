from graph_algo import *
from tree_algo import BST, heap_sort

GRAPH_VERTICES = 7
GRAPH_EDGES = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (1, 7)]
TREE_ELEMENTS = [17, 12, 25, 10, 15, 20, 30]
SEARCH_VALUE = 25
DELETE_VALUE = 12
HEAP_ARRAY = [17, 12, 25, 10, 15, 20, 30]

print("ЛАБОРАТОРНАЯ РАБОТА №2")
print("Реализация и обход графов и деревьев на Python\n")

# Часть 1: Графы
print("1. ГРАФЫ")
print("Вершины: 1-7")
print(f"Рёбра: {GRAPH_EDGES}")
adj_matrix = create_adjacency_matrix(GRAPH_EDGES, GRAPH_VERTICES)
print("\nМатрица смежности:")
for row in adj_matrix:
    print(row)
inc_matrix = create_incidence_matrix(GRAPH_EDGES, GRAPH_VERTICES)
print("\nМатрица инцидентности:")
for row in inc_matrix:
    print(row)
components = find_connected_components(GRAPH_EDGES, GRAPH_VERTICES)
print(f"\nКомпоненты связности: {components}")

# Часть 2: Деревья
print("\n2. ДЕРЕВЬЯ")
print(f"Элементы для построения BST: {TREE_ELEMENTS}")
bst = BST()
for elem in TREE_ELEMENTS:
    bst.insert(elem)
print(f"\nПоиск элемента {SEARCH_VALUE}: {'Найден' if bst.search(SEARCH_VALUE) else 'Не найден'}")
bst.delete(DELETE_VALUE)
print(f"Удаление элемента {DELETE_VALUE} выполнено")

# Часть 3: Heap Sort
print("\n3. HEAP SORT")
print(f"Исходный массив: {HEAP_ARRAY}")
sorted_array = heap_sort(HEAP_ARRAY.copy())
print(f"Отсортированный массив: {sorted_array}")
