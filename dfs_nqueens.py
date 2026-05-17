import time
import tracemalloc


def check(board, col, row):
    for c in range(col):
        if board[c] == row:
            return False
        if abs(board[c] - row) == abs(c - col):
            return False
    return True


def solve(n, board, col, limit, start):
    if time.perf_counter() - start > limit:
        return False
    if col == n:
        return True
    for row in range(n):
        if check(board, col, row):
            board[col] = row
            if solve(n, board, col + 1, limit, start):
                return True
            board[col] = -1
    return False


def count_conflicts(board, n):
    total = 0
    for i in range(n):
        if board[i] < 0:
            continue
        for j in range(i + 1, n):
            if board[j] < 0:
                continue
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                total += 1
    return total


def run(n, limit=30.0):
    board = [-1] * n
    tracemalloc.start()
    t0 = time.perf_counter()
    solve(n, board, 0, limit, t0)
    elapsed = time.perf_counter() - t0
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    timeout = elapsed >= limit
    conflicts = count_conflicts(board, n)
    return {
        "n": n,
        "time_s": round(elapsed, 4),
        "memory_mb": round(peak / 1024 / 1024, 4),
        "conflicts": conflicts,
        "solved": conflicts == 0 and not timeout,
        "timeout": timeout,
    }


if __name__ == "__main__":
    sizes = [10, 30, 50, 100, 200, 500]
    print(f"{'N':>5} | {'Time (s)':>10} | {'Memory (MB)':>12} | {'Conflicts':>10} | {'Status':>10}")
    print("-" * 58)
    for n in sizes:
        r = run(n)
        status = "TIMEOUT" if r["timeout"] else ("solved" if r["solved"] else "partial")
        print(f"{r['n']:>5} | {r['time_s']:>10.4f} | {r['memory_mb']:>12.4f} | {r['conflicts']:>10} | {status:>10}")
