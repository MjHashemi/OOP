import random
class Person:
  def __init__(self,name):
    self.name = name        

class SoccerPlayer(Person):
  def __init__(self, name, team ='Free'):
    Person.__init__(self, name)        
    self.team = team
    
  def __str__(self):
    return 'team'+ self.team.ljust(4,' ') + self.name

class SoccerTeam:
  def __init__(self, playersList, teamName):
    self.playersList = playersList
    self.teamName = teamName
    
  def showPlayersInfo(self):    
    for self.player in self.playersList:
      self.player.team = self.teamName
      print (f'{self.player}')

players=[]
 
hossein=SoccerPlayer("hossein")
players.append (hossein)
maziar=SoccerPlayer('maziar')
players.append (maziar)
akbar=SoccerPlayer('akbar')
players.append (akbar)
nima=SoccerPlayer('nima')
players.append (nima)
mehdi=SoccerPlayer('mehdi')
players.append (mehdi)
farhad=SoccerPlayer('farhad')
players.append (farhad)
mohammad=SoccerPlayer('mohammad')
players.append (mohammad)
khashayar=SoccerPlayer('khashayar')
players.append (khashayar)
milad=SoccerPlayer('milad')
players.append (milad)
mostafa=SoccerPlayer('mostafa')
players.append (mostafa)
amin=SoccerPlayer('amin')
players.append (amin)
saeed=SoccerPlayer('saeed')
players.append (saeed)
pouya=SoccerPlayer('pouya')
players.append (pouya)
pouria=SoccerPlayer('pouria')
players.append (pouria)
reza=SoccerPlayer('reza')
players.append (reza)
ali=SoccerPlayer('ali')
players.append (ali)
behzad=SoccerPlayer('behzad')
players.append (behzad)
soheil=SoccerPlayer('soheil')
players.append (soheil)
behrooz=SoccerPlayer('behrooz')
players.append (behrooz)
shahrooz=SoccerPlayer('shahrooz')
players.append (shahrooz)
saman=SoccerPlayer('saman')
players.append (saman)
mohsen=SoccerPlayer('mohsen')
players.append (mohsen)
 
Aplayers=[]
Bplayers=players
 
while len(Aplayers)*2 != 22:
  player=random.choice(Bplayers)
  Aplayers.append(player)
  Bplayers.remove (player)
 
teamA=SoccerTeam(Aplayers,'A')
teamB=SoccerTeam(Bplayers,'B')
 
teamA.showPlayersInfo()
teamB.showPlayersInfo()