import time

def brute_force(text: str, pattern: str) -> int:
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            return i
    return -1

def kmp_match(text: str, pattern: str, border_function: list[int]) -> int:
    n = len(text)
    m = len(pattern)
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            if j == m - 1:
                return i - m + 1
            i += 1
            j += 1
        elif j > 0:
            j = border_function[j - 1]
        else:
            i += 1
    return -1

def compute_border_function(pattern: str) -> list[int]:
    border_function = [-1] * len(pattern)
    border_function[0] = 0
    m = len(pattern)
    j = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[j]:
            border_function[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            j = border_function[j - 1]
        else:
            border_function[i] = 0
            i += 1
    return border_function

def bm_match(text: str, pattern: str, lo_function) -> int:
    n = len(text)
    m = len(pattern)
    i = m - 1
    j = m - 1
    while i < n:
        if pattern[j] == text[i]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        else:
            lo = lo_function[ord(text[i])]
            i += m - min(j, 1 + lo)
            j = m - 1
    return -1

def compute_last_occurence_function(pattern: str) -> list[int]:
    lo_function = [-1] * 128
    for i in range(len(pattern)):
        lo_function[ord(pattern[i])] = i
    return lo_function

if __name__ == "__main__":
    # Baca file parts_list.txt
    PARTS_FILE_NAME = "parts_list.txt"
    parts = []
    with open("test/" + PARTS_FILE_NAME) as file:
        for line in file:
            parts.append(line.strip().lower())
    
    # Input pattern dan algoritma
    pattern = input("Pattern: ").lower()
    algorithm_input = input("Algoritma (BF/KMP/BM): ").lower()

    # Pencarian dilakukan
    start = time.time()
    count = 0
    result = []
    if algorithm_input == "bf":
        for part in parts:
            if brute_force(part, pattern) != -1:
                count += 1
                result.append(part)
    elif algorithm_input == "kmp":
        border_function = compute_border_function(pattern)
        for part in parts:
            if kmp_match(part, pattern, border_function) != -1:
                count += 1
                result.append(part)
    elif algorithm_input == "bm":
        lo_function = compute_last_occurence_function(pattern)
        for part in parts:
            if bm_match(part, pattern, lo_function) != -1:
                count += 1
                result.append(part)
    else:
        print("Algoritma tidak dikenal")
        exit(1)
    end = time.time()
    
    # Hasil pencarian
    print("===== HASIL PENCARIAN =====")
    print(f"Waktu eksekusi: {((end - start) * 1000):.5f} ms")
    print(f"Banyak komponen yang ditemukan: {count}")
    print("Komponen yang ditemukan:")
    for part in result:
        print(part)
