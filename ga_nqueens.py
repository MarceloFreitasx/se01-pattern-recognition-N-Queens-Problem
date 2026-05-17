import time
import tracemalloc
import random


def fitness(board, n):
    max_pairs = n * (n - 1) // 2
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return max_pairs - conflicts


def select(pop, scores):
    a, b = random.sample(range(len(pop)), 2)
    return pop[a] if scores[a] >= scores[b] else pop[b]


def crossover(p1, p2, n):
    cut = random.randint(1, n - 1)
    return p1[:cut] + p2[cut:]


def mutate(board, n, rate):
    board = board[:]
    if random.random() < rate:
        board[random.randint(0, n - 1)] = random.randint(0, n - 1)
    return board


def solve(n):
    if n <= 50:
        pop_size, max_gen, rate = 50, 500, 0.05
    elif n <= 200:
        pop_size, max_gen, rate = 100, 1000, 0.05
    else:
        pop_size, max_gen, rate = 200, 2000, 0.10

    perfect = n * (n - 1) // 2
    pop = [[random.randint(0, n - 1) for _ in range(n)] for _ in range(pop_size)]
    best = None
    best_fit = -1

    for _ in range(max_gen):
        scores = [fitness(ind, n) for ind in pop]
        idx = scores.index(max(scores))

        if scores[idx] > best_fit:
            best_fit = scores[idx]
            best = pop[idx][:]

        if best_fit == perfect:
            return best

        new_pop = [best[:]]
        while len(new_pop) < pop_size:
            p1 = select(pop, scores)
            p2 = select(pop, scores)
            child = crossover(p1, p2, n)
            child = mutate(child, n, rate)
            new_pop.append(child)
        pop = new_pop

    return best


def total_conflicts(board, n):
    return n * (n - 1) // 2 - fitness(board, n)


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
