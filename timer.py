from time import sleep
import _thread

def incTime(timer, extra):
    while True:
        if timer.started:
            sleep(0.0000001)
            timer.time += 0.0000001

class Timer:
    def __init__(self):
        
        self.time = 0.0
        self.started = False
    
    def start(self):
        self.started = True



    def stop(self):
        self.started = False
        return self.time

    def reset(self):
        self.started = False
        self.time = 0.0
        
        
        
        
timer = Timer()

_thread.start_new_thread(incTime, (timer, 0))

timer.start()

# Do Stuff

print(timer.stop())
