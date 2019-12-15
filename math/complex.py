class cm:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def __mul__(self, other):
        return cm((self.real*other.real)-(self.img*other.img),(self.real*other.img)+(self.img*other.real))
    def __rmul__(self, other):
        return cm((self.real*other.real)-(self.img*other.img),(self.real*other.img)+(self.img*other.real))
    def __imul__(self, other):
        return cm((self.real*other.real)-(self.img*other.img),(self.real*other.img)+(self.img*other.real))
    def __add__(self,other):
        return cm(self.real+other.real,self.img+other.img)
    def __radd__(self,other):
        return cm(self.real+other.real,self.img+other.img)
    def __iadd__(self,other):
        return cm(self.real+other.real,self.img+other.img)
    def __sub__(self,other):
        return cm(self.real+other.real,self.img+other.img)
    def __rsub__(self,other):
        return cm(self.real+other.real,self.img+other.img)
    def __isub__(self,other):
        return cm(self.real+other.real,self.img+other.img)
    def __truediv__(self,other):
        return cm((self.real*other.real+self.img*other.img)/(other.real^2+other.img^2),(self.img*other.real-self.real*other.img)/(other.real^2+other.img^2))
    def __rtruediv__(self,other):
        return cm((other.real*self.real+other.img*self.img)/(self.real^2+self.img^2),(other.img*self.real-other.real*self.img)/(self.real^2+self.img^2))
    def __itruediv__(self,other):
        return cm((self.real*other.real+self.img*other.img)/(other.real^2+other.img^2),(self.img*other.real-self.real*other.img)/(other.real^2+other.img^2))
    def __str__(self):
        return "{}+{}i".format(self.real,self.img)
    def __int__(self):
        return cm(int(self.real),int(self.img))
    def __float__(self):
        return cm(float(self.real),float(self.img))
    def __bool__(self):
        return (self.real!=0) or (self.img!=0)
