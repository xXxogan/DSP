from task_0 import BFC


graph: dict[str, list[str]] = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": [],
}

# Построение каркаса при обходе в ширину
bfc = BFC(graph)
bfc_res = bfc.travel("A")
bfc_carcass = bfc.carcass()

print(f"DFS обход {bfc_res}")
print(f"DFS каркас {bfc_carcass}")
