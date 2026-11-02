import sys

def load(path):
    available, alloc, mx = None, [], []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if parts[0] == "Available":
                available = [int(x) for x in parts[1:]]
            else:
                nums = [int(x) for x in parts[1:]]
                m = len(nums) // 2
                alloc.append(nums[:m])
                mx.append(nums[m:])
    return available, alloc, mx

def need_matrix(alloc, mx):
    # Need = Max - Allocation
    return [[mx[i][j] - alloc[i][j] for j in range(len(mx[i]))]
            for i in range(len(mx))]

def is_safe(available, alloc, mx):
    need = need_matrix(alloc, mx)
    n, m = len(alloc), len(available)
    work = available[:]
    finish = [False] * n
    seq = []
    progress = True
    while progress:
        progress = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                for j in range(m):
                    work[j] += alloc[i][j]     # процесс завершился - вернул ресурсы
                finish[i] = True
                seq.append(i)
                progress = True
    return all(finish), seq

def request(pid, req, available, alloc, mx):
    need = need_matrix(alloc, mx)
    m = len(available)
    if any(req[j] > need[pid][j] for j in range(m)):
        return False, "запрос превышает заявленный максимум"
    if any(req[j] > available[j] for j in range(m)):
        return False, "ресурсов нет, процесс должен ждать"
    # пробуем выдать
    for j in range(m):
        available[j] -= req[j]
        alloc[pid][j] += req[j]
    safe, seq = is_safe(available, alloc, mx)
    if not safe:
        for j in range(m):                      # откат
            available[j] += req[j]
            alloc[pid][j] -= req[j]
        return False, "состояние стало бы небезопасным, откат"
    return True, "выдать можно, безопасная последовательность: " + ", ".join(f"P{i}" for i in seq)

if __name__ == "__main__":
    path = sys.argv[1]
    available, alloc, mx = load(path)
    print("Need:")
    for i, row in enumerate(need_matrix(alloc, mx)):
        print(f"  P{i}: {row}")
    safe, seq = is_safe(available, alloc, mx)
    if safe:
        print("SAFE, последовательность:", ", ".join(f"P{i}" for i in seq))
    else:
        print("UNSAFE")
    if len(sys.argv) > 3:                       # python3 banker.py bank1.txt 1 1 0 2
        pid = int(sys.argv[2])
        req = [int(x) for x in sys.argv[3:]]
        ok, msg = request(pid, req, available, alloc, mx)
        print(f"Запрос P{pid} {tuple(req)}: {'ДА' if ok else 'НЕТ'} - {msg}")
