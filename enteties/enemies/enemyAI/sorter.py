def sortAI(player,enemy):
    newEnemy=None
    if enemy.id==1:
        enemy=enemy.ai(player)
    if enemy.id==2:
        both=enemy.ai(player)
        enemy=both[0]
        newEnemy=both[1]
    if enemy.id==3:
        pass
    if enemy.id==4:
        pass
    if enemy.id==100:
        enemy=enemy.ai()
    return list((enemy, newEnemy))