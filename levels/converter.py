"""a"""
import json
import os
from levelCreator import level

def load_level_from_json(level_id):
    """a"""
    level1=level.Level()
    path1=os.getcwd()
    full_path=os.path.join(path1,"levels","mainStory.txt")
    with open(full_path, "r",encoding='utf-8') as jsonfile:
        json1 = json.load(jsonfile)
        if not str(level_id) in json1:
            print("Level with this ID doesn't exist")
        else:
            a=json1[str(level_id)]["objects"]
            for x in range(64):
                for y in range(36):
                    level1.objects[x][y]=a[x][y]
    return level1
def delete_level_from_json(level_id):
    """a"""
    path1=os.getcwd()
    full_path=os.path.join(path1,"levels","mainStory.txt")
    with open(full_path, "r",encoding='utf-8') as jsonfile:
        json1 = json.load(jsonfile)
        if not str(level_id) in json1:
            print("Level with this ID doesn't exist")
        else:
            del json1[str(level_id)]
            with open(full_path, "w",encoding='utf-8') as write:
                write.write(json.dumps(json1))
            print("level deleted")


def add_level_to_json(level1:level.Level,level_id):
    """a"""
    path1=os.getcwd()
    full_path=os.path.join(path1,"levels","mainStory.txt")
    with open(full_path, "r",encoding='utf-8') as jsonfile:

        json1 = json.load(jsonfile)
        if level_id in json1:
            print("Level with this ID already exists")
        else:
            level_dict = {str(level_id):level1.__dict__}
            json1.update(level_dict)
            with open(full_path, "w",encoding='utf-8') as write:
                write.write(json.dumps(json1))
def add_score_to_json(level_id:int, name:str,score:int):
    """a"""
    path1=os.getcwd()
    full_path=os.path.join(path1,"levels","scores.txt")
    with open(full_path, "r",encoding='utf-8') as jsonfile:
        json1 = json.load(jsonfile)
        if str(level_id) in json1 and name in json1[str(level_id)]:
            current_scores=json1[str(level_id)][name]
            if str(score) not in current_scores:
                current_scores.append(str(score))
        else:
            current_scores=list()
            current_scores.append(str(score))
        json1[str(level_id)][name]=current_scores
        with open(full_path, "w",encoding='utf-8') as write:
            write.write(json.dumps(json1))
def load_scores():
    """a"""
    path1=os.getcwd()
    full_path=os.path.join(path1,"levels","scores.txt")
    json1=dict()
    with open(full_path, "r",encoding='utf-8') as jsonfile:
        json1 = json.load(jsonfile)

    return json1
