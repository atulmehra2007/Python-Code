import threading
class messenger(threading.Thread):
    def run(self):
        for _ in range(20): # _ can used in place of variable name if you dont want to use any variable name
            print(threading.currentThread().getName())
x=messenger(name='send out messages ') # name is property of thread and we can give name to a thread
y=messenger(name='\n recieve messages')
x.start()
y.start()
