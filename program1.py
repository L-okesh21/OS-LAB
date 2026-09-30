import os 

print("before Fork")
print("Current PID: ",
    os.getpid())

pid = os.fork()

if pid ==0:
    print("\nChild process")
    print("Child PID: ", os.getpid())
    
else:
    os.wait()
    print("\nParent process")
    print("Parent PID: ", os.getpid())
    print("Child PID: ", pid)
    
