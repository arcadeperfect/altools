searchPath = '/net/homes/aharding/test'


name = 'butt'
ext = 'exr'

fileTypes = ['exr','jpg','dpx','mov', 'tif']

def isNumber(string):
    try:
        int(string)
        return True
    except:
        return False
isNumber(None)

class sequence:
    def __init__ (self, name, type, first, last, location):
        self.name = name
        self.type = type
        self.first = first
        self.last = last
        self.location = location
        if isNumber(last):
            self.padding = '%%0%sd' %len(str(int(last)))
        else:
            self.padding = None

    def nukeString(self):
        if isNumber(self.first) & isNumber(self.last):
            return "%s.%s.%s %s-%s" %(self.name,self.padding,self.type,self.first,self.last)
        else:
            return "%s.%s" %(self.name, self.type)

    def fullPath(self):
        if isNumber(self.first) & isNumber(self.last):
            return "%s.%s.%s" %(os.path.join(location,name),self.padding,ext)
        else:
            return "%s.%s" %(os.path.join(location,name),ext)

    def fullNukeString(self):
        if isNumber(self.first) & isNumber(self.last):
            return "%s.%s.%s %s-%s" %(os.path.join(location,name),self.padding,ext, self.first, self.last)
        else:
            return "%s.%s" %(os.path.join(searchPath,name),ext)

    def duration(self):
        if isNumber(self.first) & isNumber(self.last):
            return int(self.last)-int(self.first)
        else:
            return 'could not find duration'

butt =sequence('butt','exr',None,None,'/net/homes/aharding/test')


for i in os.listdir(searchPath):
    ext = os.path.splitext(i)[-1].replace('.', '')
    if ext in fileTypes:
        found = []
        frame = None
        splitted = i.split('.')
        clipName = splitted[0]
        
        try:
            frame = int(splitted[-2])
         
        except:
            print i, ': failed to find frame numbers'
            frame = None

        if len(found) == 0:
            found = [name,ext,frame,frame,searchPath]
        elif frame < found[2]:
            found[2] = frame
        elif frame > found[3]:
            found[3] = frame
    seq = sequence(found[0],found[1],found[2],found[3],found[4])

