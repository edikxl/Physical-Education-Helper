from typing import Optional

import os

class File:
  
  def __init__( self, path: str, defaultContent: Optional[str] = None ) -> None:
    self._path = path

    if not self.doesFileExist( self.path ):
      self.create( self.path, defaultContent )

  # <!-- GETTERS AND SETTERS

  @property
  def path(self): return self._path

  @path.setter
  def path( self, value: str ) -> None:
    assert isinstance( value, str )
    self._path = value

  # -->

  @staticmethod
  def doesFileExist( path: str ) -> bool:
    return os.path.isfile( path )

  @staticmethod
  def create( path: str, defaultContent: Optional[str] = '' ) -> None:
    with open( path, 'w' ) as f:
      f.write( defaultContent )

  def read( self ) -> str:
    with open( self.path, 'r' ) as f:
      return f.read()

  @staticmethod
  def write( text: str ) -> None:
    with open( self.path, 'w' ) as f:
      f.write( text )