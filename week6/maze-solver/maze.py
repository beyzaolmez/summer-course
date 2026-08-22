"""
Maze solver core logic.

A maze is given as text using these characters:
    A  = start
    B  = goal
    #  = wall
    (space) = open path

The Maze class parses that text and solves it with breadth-first search (BFS),
which guarantees the shortest path. The search machinery (Node + frontiers) is
the same idea used in the Week 4 "Degrees" project.
"""


class Node:
    def __init__(self, state, parent, action):
        self.state = state      # (row, col) position in the maze
        self.parent = parent    # the node we came from
        self.action = action    # the move used to get here


class StackFrontier:
    """Last-in-first-out frontier -> depth-first search."""

    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        node = self.frontier[-1]
        self.frontier = self.frontier[:-1]
        return node


class QueueFrontier(StackFrontier):
    """First-in-first-out frontier -> breadth-first search (shortest path)."""

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        node = self.frontier[0]
        self.frontier = self.frontier[1:]
        return node


class Maze:
    def __init__(self, text):
        # Split into lines; drop a single trailing blank line if present
        lines = text.splitlines()
        if lines and lines[-1] == "":
            lines = lines[:-1]

        if not lines:
            raise ValueError("Maze is empty.")

        # Validate that exactly one start (A) and one goal (B) exist
        if text.count("A") != 1:
            raise ValueError("Maze must have exactly one start point 'A'.")
        if text.count("B") != 1:
            raise ValueError("Maze must have exactly one goal point 'B'.")

        # Determine dimensions
        self.height = len(lines)
        self.width = max(len(line) for line in lines)

        # Build the wall grid and record start/goal positions
        self.walls = []
        for i, line in enumerate(lines):
            row = []
            for j in range(self.width):
                char = line[j] if j < len(line) else " "
                if char == "A":
                    self.start = (i, j)
                    row.append(False)
                elif char == "B":
                    self.goal = (i, j)
                    row.append(False)
                elif char == "#":
                    row.append(True)
                else:
                    row.append(False)
            self.walls.append(row)

        self.solution = None
        self.num_explored = 0

    def neighbors(self, state):
        # The four orthogonal moves from a cell
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1)),
        ]

        # Keep only moves that stay in bounds and don't hit a wall
        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result

    def solve(self):
        """Find the shortest path with BFS. Returns True if solved."""
        self.num_explored = 0

        start = Node(state=self.start, parent=None, action=None)
        frontier = QueueFrontier()
        frontier.add(start)

        explored = set()

        while True:
            # No path exists if the frontier empties
            if frontier.empty():
                self.solution = None
                return False

            node = frontier.remove()
            self.num_explored += 1

            # Goal reached: rebuild the path via parent links
            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return True

            explored.add(node.state)

            for action, state in self.neighbors(node.state):
                if state not in explored and not frontier.contains_state(state):
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)

    def grid(self):
        """Return a 2D list labelling each cell for display."""
        path = set(self.solution[1]) if self.solution else set()
        result = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                state = (i, j)
                if self.walls[i][j]:
                    row.append("wall")
                elif state == self.start:
                    row.append("start")
                elif state == self.goal:
                    row.append("goal")
                elif state in path:
                    row.append("path")
                else:
                    row.append("empty")
            result.append(row)
        return result

    def to_ascii(self):
        """Simple text rendering, using '*' for the solution path."""
        cell_char = {
            "wall": "#",
            "start": "A",
            "goal": "B",
            "path": "*",
            "empty": " ",
        }
        return "\n".join(
            "".join(cell_char[cell] for cell in row) for row in self.grid()
        )


def main():
    example = (
        "A## #B\n"
        "      \n"
        "## ## \n"
        "      \n"
        "######"
    )
    maze = Maze(example)
    solved = maze.solve()
    print("Solvable:", solved)
    if solved:
        print("Steps:", len(maze.solution[1]))
        print("Cells explored:", maze.num_explored)
    print(maze.to_ascii())


if __name__ == "__main__":
    main()
