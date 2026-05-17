import time
import tracemalloc
import random
import math


def total_conflicts(board, n):
    total = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                total += 1
    return total


def solve(n, T=5.0, T_min=0.001, cooling=0.9995):
    if n > 200:
        T, T_min, cooling = 20.0, 0.0001, 0.9999
    elif n > 50:
        T, T_min, cooling = 10.0, 0.0001, 0.9998

    board = [random.randint(0, n - 1) for _ in range(n)]
    current = total_conflicts(board, n)
    best = board[:]
    best_score = current

    while T > T_min:
        if current == 0:
            return board

        col = random.randint(0, n - 1)
        new_row = random.randint(0, n - 1)
        old_row = board[col]
        board[col] = new_row
        new_score = total_conflicts(board, n)
        delta = new_score - current

        if delta < 0 or random.random() < math.exp(-delta / T):
            current = new_score
            if current < best_score:
                best_score = current
                best = board[:]
        else:
            board[col] = old_row

        T *= cooling

    return best


def run(n):
    tracemalloc.start()
    t0 = time.perf_counter()
    board = solve(n)
    elapsed = time.perf_counter() - t0
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    conflicts = total_conflicts(board, n)
    return {
        "n": n,
        "time_s": round(elapsed, 4),
        "memory_mb": round(peak / 1024 / 1024, 4),
        "conflicts": conflicts,
        "solved": conflicts == 0,
    }


if __name__ == "__main__":
    sizes = [10, 30, 50, 100, 200, 500]
    print(f"{'N':>5} | {'Time (s)':>10} | {'Memory (MB)':>12} | {'Conflicts':>10} | {'Status':>10}")
    print("-" * 58)
    for n in sizes:
        r = run(n)
        print(f"{r['n']:>5} | {r['time_s']:>10.4f} | {r['memory_mb']:>12.4f} | {r['conflicts']:>10} | {'solved' if r['solved'] else 'partial':>10}")
