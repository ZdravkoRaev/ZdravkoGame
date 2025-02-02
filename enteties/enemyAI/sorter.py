def sortAI(player,enemy):
    newEnemy=None
    if enemy.ID==1:
        enemy=enemy.AI(player)
    if enemy.ID==2:
        both=enemy.AI(player)
        enemy=both[0]
        newEnemy=both[1]
    if enemy.ID==3:
        pass
    if enemy.ID==4:
        pass
    if enemy.ID==100:
        enemy=enemy.AI()
    return list((enemy, newEnemy))