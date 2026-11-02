import os
import signal
import time

count = 0

def handler(signum, frame):
    global count
    count += 1
    msg = f"получен сигнал {signum} ({signal.Signals(signum).name}), №{count} из 3"
    print(msg, flush=True)
    with open("signal_log.txt", "a") as f:
        f.write(msg + "\n")

signal.signal(signal.SIGINT, handler)
print(f"PID = {os.getpid()}. Отправьте SIGINT 3 раза (kill -INT или Ctrl+C)", flush=True)
while count < 3:
    time.sleep(0.2)
print("Три сигнала получено, выход.")
