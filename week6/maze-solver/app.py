from flask import Flask, render_template, request

from maze import Maze

app = Flask(__name__)

# A default maze shown when the page first loads
DEFAULT_MAZE = (
    "A## #B\n"
    "      \n"
    "## ## \n"
    "      \n"
    "######"
)


@app.route("/")
def index():
    # Show the input form pre-filled with an example maze
    return render_template("index.html", maze_text=DEFAULT_MAZE)


@app.route("/solve", methods=["POST"])
def solve():
    maze_text = request.form.get("maze", "")

    # Parsing can fail if the maze is missing an A or B
    try:
        maze = Maze(maze_text)
    except ValueError as error:
        return render_template("index.html", maze_text=maze_text, error=str(error))

    solved = maze.solve()

    return render_template(
        "result.html",
        grid=maze.grid(),
        solved=solved,
        steps=len(maze.solution[1]) if solved else 0,
        explored=maze.num_explored,
        maze_text=maze_text,
    )


if __name__ == "__main__":
    app.run(debug=True)
