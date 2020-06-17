from operator import itemgetter 
from endpoints import Controller


class Count(Controller):
    sum = 0
    def GET(self):
        return self.sum

class Default(Controller):
    
    def POST(self, **kwargs):
        number = int(list(kwargs.keys())[0])
        Count.sum += number


