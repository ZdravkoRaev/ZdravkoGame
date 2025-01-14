import json
import os
from levelCreator import level

def loadLevelFromJson(levelID):
    level1=level.Level()
    path1=os.getcwd()
    fullPath=os.path.join(path1,"homework7","levels","mainStory.txt")
    with open(fullPath, "r") as jsonfile:
        json1 = json.load(jsonfile)
        if not str(levelID) in json1:
            print("Level with this ID doesn't exist")
        else:
            a=json1[str(levelID)]["objects"]
            for x in range(64):
                for y in range(36):
                    level1.objects[x][y]=a[x][y]




    return level1
def deleteLevelFromJson(levelID):
    path1=os.getcwd()
    fullPath=os.path.join(path1,"homework7","levels","mainStory.txt")
    with open(fullPath, "r") as jsonfile:
        json1 = json.load(jsonfile)
        if not str(levelID) in json1:
            print("Level with this ID doesn't exist")
        else:
            del json1[str(levelID)]
            with open(fullPath, "w") as write:
                write.write(json.dumps(json1))
            print("level deleted")
        

def addLevelToJson(level1:level.Level,levelID):
    path1=os.getcwd()
    fullPath=os.path.join(path1,"homework7","levels","mainStory.txt")
    with open(fullPath, "r") as jsonfile:

        json1 = json.load(jsonfile)
        if levelID in json1:
            print("Level with this ID already exists")
        else: 
            levelDict = {str(levelID):level1.__dict__}
            json1.update(levelDict)
            with open(fullPath, "w") as write:
                write.write(json.dumps(json1))
def addScoreToJson(levelID:int, name:str,score:int):
    path1=os.getcwd()
    fullPath=os.path.join(path1,"homework7","levels","scores.txt")
    with open(fullPath, "r") as jsonfile:
        json1 = json.load(jsonfile)
        if str(levelID) in json1 and name in json1[str(levelID)]:
            currentScores=json1[str(levelID)][name]
            if str(score) not in currentScores:
                currentScores.append(str(score))
        else:
            currentScores=list()
            currentScores.append(str(score))
        json1[str(levelID)][name]=currentScores
        with open(fullPath, "w") as write:
            write.write(json.dumps(json1))
def loadScores():
    path1=os.getcwd()
    fullPath=os.path.join(path1,"homework7","levels","scores.txt")
    json1=dict()
    with open(fullPath, "r") as jsonfile:
        json1 = json.load(jsonfile)

    return json1

    
    