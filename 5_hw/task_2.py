from task_0 import DFC


graph: dict[str, list[str]] = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": [],
}

# Обход в глубину
dfc = DFC(graph)
dfc_res = dfc.travel("A")

print(f"DFS обход {dfc_res}")
