import os

print("before fork")

pid = os.fork()

if pid == 0:
    print("child:", os.getpid())
else:
    print("parent:", os.getpid(), "child:", pid)
    os.wait()
