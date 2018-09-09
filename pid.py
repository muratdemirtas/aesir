import os
import parameters

class pidlogger:

    curr_pid = 0;
    pidpath = parameters.INDICATOR_PID_PATH

    def __init__(self):
        curr_pid = os.getpid()

    def savepid(self):
        file = open( self.pidpath,"w")
        file.write(self.curr_pid)

    def getlastindicatorpid(self):
        if(os.path.exists(self.pidpath)):
            file = open(self.pidpath, "r")
            return file.read()
        else:
            print("dosya yok")
            return None

    def check_pid(self, pid):
         try:
            os.kill(pid, 0)
         except OSError:
            return False
         else:
            print("pid tespit edildi.")
            return True



