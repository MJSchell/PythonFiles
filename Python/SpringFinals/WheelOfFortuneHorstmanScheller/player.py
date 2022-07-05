
class Player:
    playernames=[]
    Player1score=0
    Player2score=0
    Player3score=0
    playerlist=[Player1score,Player2score,Player3score]
    
    def __init__(self,name,score):
        self.name=name
        self.score=score
    
    def __str__(self):
        return f"{self.name} has a balance of {self.score}"
    
#players=[]
#for i in range(3):
#    players.append(Player(input(),0))
#players[1].score+=100
#
#print(players[1])