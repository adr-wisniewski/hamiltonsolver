'''
Created on 2010-11-15

@author: Adrian
'''
class DataSource(object):
    def getData( self ):
        raise NotImplementedError()
    
    @staticmethod
    def fromOption( option ):
        raise NotImplementedError()
