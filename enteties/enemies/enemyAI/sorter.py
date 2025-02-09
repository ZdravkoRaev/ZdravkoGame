"""a"""
def sort_ai(player,enemy):
    """a"""
    new_enemy=None
    if enemy.id==1:
        enemy=enemy.ai(player)
    if enemy.id==2:
        both=enemy.ai(player)
        enemy=both[0]
        new_enemy=both[1]
    if enemy.id==3:
        pass
    if enemy.id==4:
        pass
    if enemy.id==100:
        enemy=enemy.ai()
    return list((enemy, new_enemy))
