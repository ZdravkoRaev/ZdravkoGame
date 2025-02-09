"""a"""
class Level:
    """a"""
    def __init__(self):
        """a"""
        self.objects =list()
        for x in range(64):
            q=list()
            for y in range(36):
                if x==0 or x==1 or x==63 or x==62 or y==0 or y==35 or y==1 or y==34:
                    q.append(1)
                else:
                    q.append(0)
            self.objects.append(q)
