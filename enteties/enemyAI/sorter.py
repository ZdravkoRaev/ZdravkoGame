from enteties.enemyAI import basicFlierAI
from enteties.enemyAI import shootyFlierAI
from enteties.enemyAI import projectileAI
def sortAI(player,enemy):
    newEnemy=None
    if enemy.ID==1:
        enemy=basicFlierAI.AI(player,enemy)
    if enemy.ID==2:
        both=shootyFlierAI.AI(player,enemy)
        enemy=both[0]
        newEnemy=both[1]
    if enemy.ID==3:
        pass
    if enemy.ID==4:
        pass
    if enemy.ID==100:
        enemy=projectileAI.AI(enemy)
    return list((enemy, newEnemy))