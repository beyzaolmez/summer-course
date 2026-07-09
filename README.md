# Summer Preparation Programme — Computer Science

A 6-week self-study programme built from CS50x, CS50 Python, and CS50 AI.
Each week lives on its own branch, with assignments and a written reflection.

## Progress

| Week | Topic | Status |
| ---- | ----- | ------ |
| 1 | Deep Dive into C | In progress |
| 2 | Python Essentials | Not started |
| 3 | OOP & Flask | Not started |
| 4 | AI: Search | Not started |
| 5 | AI: Knowledge | Not started |
| 6 | Final Project | Not started |

## Week 1 — Deep Dive into C

CS50x lectures completed: Week 0 (Scratch), Week 1 (C), Week 2 (Arrays).

### Assignments

| Assignment | File |
| ---------- | ---- |
| Scratch Project | [`week1/scratch/README.md`](week1/scratch/README.md) |
| Hello | [`week1/hello/hello.c`](week1/hello/hello.c) |
| Mario | [`week1/mario/mario.c`](week1/mario/mario.c) |
| Cash | [`week1/cash/cash.c`](week1/cash/cash.c) |
| Credit | [`week1/credit/credit.c`](week1/credit/credit.c) |
| Readability | [`week1/readability/readability.c`](week1/readability/readability.c) |
| Additional (algorithm write-up) | [`week1/explanation.md`](week1/explanation.md) |

### Building and running

The programs use the CS50 library (`cs50.h`) and are meant to be compiled in
the CS50 environment (e.g. cs50.dev / Codespaces):

```bash
cd week1/mario
make mario
./mario
```

### Week 1 Reflection

This week was my first real experience with C. Scratch made programming easy to understand because I could drag and drop blocks and instantly see what happened. With C, I had to pay much more attention to the details. Even a missing semicolon or brace could stop the whole program from compiling, which I find very annoying. :) 

The first assignments, `hello` and `mario`, helped me get used to using `printf`, `get_string`, `get_int`, and writing loops. The `mario` problem especially helped me understand how nested loops work. At first it was confusing, but once I figured out how the rows and columns related to each other, it started to make sense. `cash` introduced me to the greedy algorithm, and I learned why it's better to convert dollars into cents using `round()` instead of working with floating-point numbers, which can cause unexpected errors.

The most challenging assignment was `credit`. Implementing Luhn's algorithm took some time because I had to work with each digit individually, double every second digit, and handle numbers larger than 9 correctly. My first solution became more complicated than it needed to be, so I started over and split the problem into smaller parts. First, I checked whether the card number was valid, and then I determined the card issuer. That approach made the code much easier to understand, and I also explained my solution in `explanation.md`. The `readability` assignment was interesting because it showed how counting letters, words, and sentences can be used to calculate a reading grade level.

The biggest thing I learned this week was the importance of debugging step by step. Instead of trying to fix everything at once, I compiled my code often, tested different inputs, and used small `printf` statements to check whether my variables contained the values I expected. I also realized that reading the assignment instructions carefully saves a lot of time because many of my mistakes came from missing small details.

