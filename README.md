# N-Queens Problem — Comparing Optimization Algorithms

## Student Information

| Field | Details |
|---|---|
| **Name** | Marcelo Augusto de Azevedo Freitas Filho |
| **Student ID** | 72007730 |
| **Course** | MSc Software Engineering |
| **Subject** | Pattern Recognition |
| **University** | University of Europe for Applied Sciences |
| **Professor** | Raja Hashim Ali |
| **Deadline** | May 17, 2026 |

---

## Project Description

This project implements and compares four algorithms for solving the N-Queens problem:

1. **Depth-First Search (DFS)** — exhaustive backtracking search
2. **Hill Climbing** — greedy local search with random restarts
3. **Simulated Annealing (SA)** — local search with probabilistic acceptance
4. **Genetic Algorithm (GA)** — evolutionary optimization

All algorithms were tested for board sizes N = 10, 30, 50, 100, 200, and 500, measuring execution time, memory consumption, and solution quality.

---

## Files

| File | Description |
|---|---|
| `dfs_nqueens.py` | Depth-First Search implementation |
| `greedy_nqueens.py` | Hill Climbing implementation |
| `sa_nqueens.py` | Simulated Annealing implementation |
| `ga_nqueens.py` | Genetic Algorithm implementation |

---

## How to Run

```bash
python dfs_nqueens.py
python greedy_nqueens.py
python sa_nqueens.py
python ga_nqueens.py
```

No external libraries required — uses only Python standard library (`time`, `tracemalloc`, `random`, `math`).

---

## Results Summary

| N | DFS | Hill Climbing | Simulated Annealing | Genetic Algorithm |
|---|---|---|---|---|
| 10 | 0.002s ✓ | 0.003s ✓ | 0.20s ✓ | 0.65s (1 conflict) |
| 30 | 20.0s ✓ | 0.15s ✓ | 4.27s (1 conflict) | 4.12s (4 conflicts) |
| 50 | TIMEOUT | 7.04s (3 conflicts) | 8.70s ✓ | 11.74s (10 conflicts) |
| 100 | TIMEOUT | 58.22s (5 conflicts) | 22.1s (1 conflict) | 48.43s (27 conflicts) |
| 200 | TIMEOUT | TIMEOUT | 10.6s (25 conflicts) | 2.90s (140 conflicts) |
| 500 | TIMEOUT | TIMEOUT | TIMEOUT | 23.33s (444 conflicts) |

✓ = exact solution found (0 conflicts)
