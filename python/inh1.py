class ape:
    def __init__(m,hands,legs,ear,top):
        m.a1=hands
        m.a2=legs
        m.a3=ear
    def display(m):
        
        
class human(ape):
    def __init__(m,hands,legs,head):
        m.b1=hands
        m.b2=legs
        super.__init__(hands,legs,ear)

hum=human(2,2,"hairy",12)
