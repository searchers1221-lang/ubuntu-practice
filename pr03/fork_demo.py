import os

pid = os.fork()   # после этой строки работают ДВА процесса
if pid == 0:
    # ветка ребёнка: fork вернул 0
    print(f"Я ребёнок, PID={os.getpid()}, PPID={os.getppid()}")
    os._exit(3)   # выходим сразу, иначе ребёнок выполнит код родителя
else:
    # ветка родителя: fork вернул PID ребёнка
    child, status = os.wait()
    print(f"Родитель PID={os.getpid()}: ребёнок {child} завершился с кодом {os.WEXITSTATUS(status)}")
