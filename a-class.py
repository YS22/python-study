class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise ValueError('input must be an integer!')
        if value<0:
            raise ValueError('input must bigger than 0!')
        self._width=value 

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        if not isinstance(value,int):
            raise ValueError('input must be an integer!')
        if value<0:
            raise ValueError('input must bigger than 0!')
        self._height=value 
    @property
    def resolution(self):
        return self._width*self._height
s=Screen()
s.width=1024
s.height=768
print(s.resolution)
   