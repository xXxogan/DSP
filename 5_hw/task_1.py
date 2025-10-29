from task_0 import BFC

graph: dict[str, list[str]] = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": [],
}

# Обход в ширину
bfc = BFC(graph)
bfc_res = bfc.travel("A")

print(f"DFS обход {bfc_res}")
