'''
Created on 2010-11-15

@author: Adrian
'''
from hamilton.DataSource import DataSource
from string import split

class FileDataSource(DataSource):
    
    _file = None
    
    def __init__(self, file):
        self._file = file
    
    def getData( self ):
        data = []
        
        for line in self._file:
            data.append([int(chunk) for chunk in split(line)])
             
        vertices = len(data)
        
        for row in data:
            if len(row) != vertices:
                raise RuntimeError("File contains jagged array - square required")
                
        if(vertices < 4):
            raise RuntimeError("File contains fewer than 4 vertices")
        
        return data;
        
    