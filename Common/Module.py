import os

class Module(object):
    def __init__(self,name):
        self.name = name
    
    def begin(self,collector):
        pass

    def end(self,collector):
        pass

    def analyze(self,data,collector):
        pass
