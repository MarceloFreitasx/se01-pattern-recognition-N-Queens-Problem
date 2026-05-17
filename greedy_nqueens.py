import time
import tracemalloc
import random


def conflicts_at(board, col, row, n):
    total = 0
    for c in range(n):
        if c == col:
            continue
        if board[c] == row:
            total += 1
        if abs(board[c] - row) == abs(c - col):
            total += 1
    return total


def total_conflicts(board, n):
    total = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                total += 1
    return total


def solve(n, restarts=200, max_steps=None):
    if max_steps is None:
        max_steps = n * n

    best = None
    best_score = float("inf")

    for _ in range(restarts):
        board = [random.randint(0, n - 1) for _ in range(n)]

        for _ in range(max_steps):
            scores = [conflicts_at(board, c, board[c], n) for c in range(n)]
            total = sum(scores)

            if total == 0:
                return board

            if total < best_score:
                best_score = total
                best = board[:]

            worst = max(scores)
            candidates = [c for c, v in enumerate(scores) if v == worst]
            col = random.choice(candidates)

            best_row = board[col]
            best_val = scores[col]
            for row in range(n):
                if row == board[col]:
                    continue
                v = conflicts_at(board, col, row, n)
                if v < best_val:
                    best_val = v
                    best_row = row

            if best_row == board[col]:
                break

            board[col] = best_row

    return best if best is not None else board


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
