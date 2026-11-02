import subprocess

# аналог команды: ls | grep py
p1 = subprocess.Popen(["ls"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "py"], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()         # чтобы grep получил EOF, когда ls закончит
out, _ = p2.communicate()
print(out.decode())
