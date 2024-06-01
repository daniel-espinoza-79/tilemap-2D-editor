class Element:
    def __init__(self, pos:list[int],type:str, subtype:str, img_pos=0):
        self.pos:list[int] = pos
        self.type:str = type
        self.subtype:str = subtype
