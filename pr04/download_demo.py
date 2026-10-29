import time, threading, urllib.request, http.server, socketserver

# Локальный сервер с задержкой 0.3 с на каждый запрос, имитирует медленную сеть
class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        time.sleep(0.3)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"x" * 1000)
    def log_message(self, *a):
        pass

class Server(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True

srv = Server(("127.0.0.1", 8765), Handler)
threading.Thread(target=srv.serve_forever, daemon=True).start()

urls = ["http://127.0.0.1:8765/file%d" % i for i in range(20)]

def fetch(u):
    urllib.request.urlopen(u).read()

t0 = time.time()
for u in urls:
    fetch(u)
print(f"Последовательно: {time.time() - t0:.2f} с")

t0 = time.time()
ts = [threading.Thread(target=fetch, args=(u,)) for u in urls]
# запускаем по 4 потока одновременно
for k in range(0, 20, 4):
    batch = ts[k:k+4]
    for t in batch: t.start()
    for t in batch: t.join()
print(f"В 4 потока: {time.time() - t0:.2f} с")
srv.shutdown()
