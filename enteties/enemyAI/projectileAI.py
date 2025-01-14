from enteties.enemies.projectile import Projectile
def AI(projectile : Projectile):
    if projectile.base.wallBelow or projectile.base.wallAbove or projectile.base.wallLeft or projectile.base.wallRight:
        projectile.hp=-1
    return projectile