import os

r, w = os.pipe()          # r - конец для чтения, w - конец для записи
pid = os.fork()

if pid == 0:
    # ребёнок: только пишет
    os.close(r)           # закрываем ненужный конец чтения
    os.write(w, "Привет от ребёнка!".encode())
    os.close(w)
    os._exit(0)
else:
    # родитель: только читает
    os.close(w)           # ОБЯЗАТЕЛЬНО закрыть запись, иначе не придёт EOF
    chunks = []
    while True:
        data = os.read(r, 1024)
        if not data:      # пустой результат = EOF
            break
        chunks.append(data)
    os.close(r)
    os.waitpid(pid, 0)
    print("Родитель получил:", b"".join(chunks).decode())
