import timeit

def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return 0
    bad_char = {pattern[i]: i for i in range(m)}
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))
    return -1


def knuth_morris_pratt(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    m = len(pattern)
    n = len(text)
    lps = compute_lps(pattern)
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def rabin_karp(text, pattern, q=101):
    d = 256
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    for i in range(m - 1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            if text[i : i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
    return -1


def measure_time(func, text, pattern):
    return timeit.timeit(lambda: func(text, pattern), number=10)


def main():
    pattern_existing = "відомі алгоритми пошуку"
    pattern_non_existing = "випадковий підрядок"

    text_1 = open("article_1.txt", "r", encoding="utf-8", errors="ignore").read()
    text_2 = open("article_2.txt", "r", encoding="utf-8", errors="ignore").read()

    algorithms = [boyer_moore, knuth_morris_pratt, rabin_karp]
    texts = [(text_1, "Article 1"), (text_2, "Article 2")]
    patterns = [(pattern_existing, "Existing"), (pattern_non_existing, "Non-Existing")]

    results = {}
    for text, article in texts:
        results[article] = {}
        for pattern, result_type in patterns:
            results[article][result_type] = {}
            for algo in algorithms:
                algo_name = algo.__name__.replace("_", "-").title()
                results[article][result_type][algo_name] = measure_time(algo, text, pattern)

    def print_results(results):
        for article, types in results.items():
            print(f"{article}:")
            for result_type, algorithms in types.items():
                print(f"  {result_type}:")
                for algo, time in algorithms.items():
                    print(f"    {algo}: {time:.6f} seconds")
            print()

    print_results(results)


if __name__ == "__main__":
    main()