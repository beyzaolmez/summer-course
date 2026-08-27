# Additional Assignment: How the Degrees Search Works

## What the program solves

`degrees.py` answers a "six degrees of Kevin Bacon" style question: given two
actors, what is the *shortest* chain of movies connecting them? Each actor is a
**state**, and starring together in a movie is an **action** that moves from one
state (actor) to a neighbouring one.

## How my search works

I model the problem as a graph search and solve it with **breadth-first search
(BFS)** inside `shortest_path`:

1. Start with a `Node` for the source actor and put it in a **queue** frontier.
2. Repeatedly remove the actor at the **front** of the queue and mark them as
   explored.
3. For each co-star (neighbour) of that actor, if I haven't already explored
   them or queued them, wrap them in a `Node` that remembers its parent and the
   movie (action) used to reach them.
4. As soon as a generated neighbour **is** the target, I stop and rebuild the
   path by following `parent` pointers back to the source, then reverse it.
5. If the frontier empties without reaching the target, the actors are not
   connected, so I return `None`.

Keeping a parent reference on every node is what lets me reconstruct the full
list of `(movie_id, person_id)` steps at the end.

## Why BFS gives the *shortest* path

BFS explores the graph in "rings": first all actors 1 movie away, then all
actors 2 movies away, and so on. Because it never looks at a deeper ring before
finishing the current one, the **first** time it reaches the target it has done
so via a minimum number of steps. That is exactly what "fewest degrees of
separation" means, so BFS is the correct choice here.

## Breadth-First Search vs. Depth-First Search

Both search the same graph and use the same `Node`/frontier machinery; the
**only** difference is which node they remove next:

- **BFS** uses a **queue** (`QueueFrontier`, first-in-first-out). It removes the
  *oldest* node, so it fans out level by level.
- **DFS** uses a **stack** (`StackFrontier`, last-in-first-out). It removes the
  *newest* node, so it dives as deep as possible down one path before backing
  up.

### How they differ in practice

- **Shortest path:** BFS is *guaranteed* to find the fewest-degrees path. DFS is
  **not** — it returns the first path it stumbles onto, which can be
  needlessly long (e.g. an actor connected directly might instead be found
  through a long chain of films).
- **Memory:** DFS usually needs less memory because it only tracks the current
  branch, while BFS must hold an entire ring of nodes at once, which can be
  huge on a dataset like the "large" one.
- **Speed to *a* answer:** DFS can sometimes reach *some* answer faster if the
  target happens to be deep down the first branch it tries, but that answer may
  be wrong for this problem.

### Conclusion

For "degrees of separation" the requirement is the *shortest* chain, so **BFS is
the right algorithm**. I would only prefer DFS if I merely needed to know
whether *any* connection exists, or if memory were extremely tight and an
optimal path were not required.
