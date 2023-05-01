class G_string():
    def __init__(self, ins="") -> None:
        self.instr = ins
        #pass
    
    def getString(self):
        self.instr = input('Please type anything: ')
        
    def printString(self):
        print(self.instr)
        
x = G_string()
x.getString()    
x.printString()    