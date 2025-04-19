class myHash:
    def __init__(self,b):
        self.bucket=b
        self.table=[[] for x in range(b)]
    
    def insert(self,x):
        i=x%self.bucket
        self.table[i].append(x)N