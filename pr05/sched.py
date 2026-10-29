#!/usr/bin/env python3
"""Симулятор планирования CPU: FCFS, SJF (невытесняющий), RR."""
import argparse
from collections import deque


class Process:
    def __init__(self, pid, arrival, burst, priority):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.priority = priority
        self.remaining = burst


def read_file(path):
    procs = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            pid, a, b, p = line.split()
            procs.append(Process(pid, int(a), int(b), int(p)))
    return procs


def pid_num(p):
    return int(p.pid[1:])


def fcfs(procs):
    t, intervals = 0, []
    for p in sorted(procs, key=lambda x: (x.arrival, pid_num(x))):
        t = max(t, p.arrival)
        intervals.append((p.pid, t, t + p.burst))
        t += p.burst
    return intervals


def sjf(procs):
    left = sorted(procs, key=lambda x: (x.arrival, pid_num(x)))
    t, intervals = 0, []
    while left:
        ready = [p for p in left if p.arrival <= t]
        if not ready:
            t = min(p.arrival for p in left)
            continue
        p = min(ready, key=lambda x: (x.burst, x.arrival, pid_num(x)))
        intervals.append((p.pid, t, t + p.burst))
        t += p.burst
        left.remove(p)
    return intervals


def rr(procs, quantum):
    pending = sorted(procs, key=lambda x: (x.arrival, pid_num(x)))
    queue, t, intervals, i = deque(), 0, [], 0
    for p in procs:
        p.remaining = p.burst

    def admit(upto):
        nonlocal i
        while i < len(pending) and pending[i].arrival <= upto:
            queue.append(pending[i])
            i += 1

    admit(0)
    while queue or i < len(pending):
        if not queue:
            t = pending[i].arrival
            admit(t)
        p = queue.popleft()
        run = min(quantum, p.remaining)
        intervals.append((p.pid, t, t + run))
        t += run
        p.remaining -= run
        admit(t)
        if p.remaining > 0:
            queue.append(p)
    return intervals


def metrics(procs, intervals):
    finish = {}
    for pid, s, e in intervals:
        finish[pid] = e
    n = len(procs)
    turn = {p.pid: finish[p.pid] - p.arrival for p in procs}
    wait = {p.pid: turn[p.pid] - p.burst for p in procs}
    return sum(wait.values()) / n, sum(turn.values()) / n


def gantt(intervals):
    merged = []
    for pid, s, e in intervals:
        if merged and merged[-1][0] == pid and merged[-1][2] == s:
            merged[-1] = (pid, merged[-1][1], e)
        else:
            merged.append((pid, s, e))
    return " ".join(f"|{pid} {s}-{e}" for pid, s, e in merged) + "|"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--algo", choices=["fcfs", "sjf", "rr"], required=True)
    ap.add_argument("--quantum", type=int, default=3)
    ap.add_argument("file")
    a = ap.parse_args()

    procs = read_file(a.file)
    if a.algo == "fcfs":
        iv = fcfs(procs)
    elif a.algo == "sjf":
        iv = sjf(procs)
    else:
        iv = rr(procs, a.quantum)

    w, t = metrics(procs, iv)
    print(f"Алгоритм: {a.algo}" + (f" (q={a.quantum})" if a.algo == "rr" else ""))
    print("Гант:", gantt(iv))
    print(f"Среднее ожидание: {w:.2f}")
    print(f"Средний оборот:   {t:.2f}")


if __name__ == "__main__":
    main()
