import os, time

pid = os.fork()
if pid == 0:
    print("Ребёнок завершается сразу")
    os._exit(0)
else:
    print(f"Родитель PID={os.getpid()} спит 30 секунд и не вызывает wait(), ребёнок {pid} станет зомби")
    time.sleep(30)
