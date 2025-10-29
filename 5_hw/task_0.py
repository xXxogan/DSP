import abc
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation


class GraphTravel(abc.ABC):
    def __init__(self, graph: dict[str, list[str]]):
        super().__init__()
        all_nodes = set(graph.keys())
        for neighbors in graph.values():
            all_nodes.update(neighbors)

        self.graph = {node: graph.get(node, []) for node in all_nodes}
        self.parent: dict[str, str | None] = {}
        self.steps: list[dict] = []

    @abc.abstractmethod
    def travel(self, start_vertex: str) -> list[str]:
        pass

    def carcass(self):
        return self.parent

    def _save_step(self, current, visited, queue_or_stack):
        self.steps.append(
            {
                "current": current,
                "visited": visited.copy(),
                "queue": queue_or_stack.copy(),
                "parent": self.parent.copy(),
            }
        )

    def visualize(self, start_vertex: str, delay: float = 1.0):
        self.steps = []
        self.parent = {}

        result = self.travel(start_vertex)

        G = nx.DiGraph(self.graph)

        if not G.nodes():
            print("Граф пуст.")
            return result

        pos = nx.spring_layout(G, seed=42)
        fig, ax = plt.subplots(figsize=(10, 7))

        def draw(frame):
            ax.clear()

            if frame >= len(self.steps):
                return []

            step = self.steps[frame]

            colors = []
            for n in G.nodes():
                if n == step["current"]:
                    colors.append("red")
                elif n in step["visited"]:
                    colors.append("green")
                elif n in step["queue"]:
                    colors.append("orange")
                else:
                    colors.append("#cccccc")

            nx.draw(
                G,
                pos,
                node_color=colors,
                with_labels=True,
                node_size=800,
                font_weight="bold",
                ax=ax,
                arrows=True,
                arrowstyle="->",
                arrowsize=20,
            )

            tree_edges = []
            for child, parent in step["parent"].items():
                if parent is not None:
                    if G.has_edge(parent, child):
                        tree_edges.append((parent, child))

            nx.draw_networkx_edges(
                G, pos, edgelist=tree_edges, edge_color="blue", width=2.5, ax=ax
            )

            title_prefix = "Очередь" if isinstance(self, BFC) else "Стек"
            ax.set_title(f"Шаг {frame + 1}: {title_prefix}: {step['queue']}")
            return []

        anim = FuncAnimation(
            fig, draw, frames=len(self.steps), interval=delay * 1000, repeat=False
        )

        plt.show()
        return result


class BFC(GraphTravel):
    def travel(self, start_vertex: str) -> list[str]:
        if start_vertex not in self.graph:
            raise ValueError(f"Start vertex {start_vertex} not in graph")

        visited: set[str] = set()
        queue: list[str] = [start_vertex]
        result: list[str] = []
        self.parent = {start_vertex: None}

        while queue:
            self._save_step(None, visited, queue)
            vertex = queue.pop(0)

            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                self._save_step(vertex, visited, queue)

                for neighbor in self.graph.get(vertex, []):
                    if neighbor not in visited and neighbor not in queue:
                        queue.append(neighbor)
                        self.parent[neighbor] = vertex

                print(f"Очередь после обхода {vertex}: {queue}")

        self._save_step(None, visited, queue)
        return result


class DFC(GraphTravel):
    def travel(self, start_vertex: str) -> list[str]:
        if start_vertex not in self.graph:
            raise ValueError(f"Start vertex {start_vertex} not in graph")

        visited: set[str] = set()
        stack: list[str] = [start_vertex]
        result: list[str] = []
        self.parent = {start_vertex: None}

        while stack:
            self._save_step(None, visited, stack)
            vertex = stack.pop()

            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                self._save_step(vertex, visited, stack)

                for neighbor in reversed(self.graph.get(vertex, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
                        self.parent[neighbor] = vertex

                print(f"Стек после обхода {vertex}: {stack}")

        self._save_step(None, visited, stack)
        return result
