import json
import os
from levelCreator import level

def load_level_from_json(levelID):
    level1=level.Level()
    path1=os.getcwd()
    full_path=os.path.join(path1,"levels","mainStory.txt")
    with open(full_path, "r",encoding='utf-8') as jsonfile:
        json1 = json.load(jsonfile)
        if not str(levelID) in json1:
            print("Level with this ID doesn't exist")
        else:
            a=json1[str(levelID)]["objects"]
            for x in range(64):
                for y in range(36):
                    level1.objects[x][y]=a[x][y]
    return level1
def delete_level_from_json(levelID):
    path1=os.getcwd()
    full_path=os.path.join(path1,"levels","mainStory.txt")
    with open(full_path, "r",encoding='utf-8') as jsonfile:
        json1 = json.load(jsonfile)
        if not str(levelID) in json1:
            print("Level with this ID doesn't exist")
        else:
            del json1[str(levelID)]
            with open(full_path, "w",encoding='utf-8') as write:
                write.write(json.dumps(json1))
            print("level deleted")
        

def add_level_to_json(level1:level.Level,levelID):
    path1=os.getcwd()
    full_path=os.path.join(path1,"levels","mainStory.txt")
    with open(full_path, "r",encoding='utf-8') as jsonfile:

        json1 = json.load(jsonfile)
        if levelID in json1:
            print("Level with this ID already exists")
        else:
            level_dict = {str(levelID):level1.__dict__}
            json1.update(level_dict)
            with open(full_path, "w",encoding='utf-8') as write:
                write.write(json.dumps(json1))
def add_score_to_json(levelID:int, name:str,score:int):
    path1=os.getcwd()
    full_path=os.path.join(path1,"levels","scores.txt")
    with open(full_path, "r",encoding='utf-8') as jsonfile:
        json1 = json.load(jsonfile)
        if str(levelID) in json1 and name in json1[str(levelID)]:
            current_scores=json1[str(levelID)][name]
            if str(score) not in current_scores:
                current_scores.append(str(score))
        else:
            current_scores=list()
            current_scores.append(str(score))
        json1[str(levelID)][name]=current_scores
        with open(full_path, "w",encoding='utf-8') as write:
            write.write(json.dumps(json1))
def load_scores():
    path1=os.getcwd()
    full_path=os.path.join(path1,"levels","scores.txt")
    json1=dict()
    with open(full_path, "r",encoding='utf-8') as jsonfile:
        json1 = json.load(jsonfile)

    return json1

    
    