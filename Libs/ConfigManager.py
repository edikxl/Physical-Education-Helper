from typing import Optional, Any

import json
from copy import deepcopy

from Libs import File

class ConfigManager:

  def __init__( self, configPath: str, defaultConfig: dict ) -> None:
    self._defaultConfig = defaultConfig
    self._config = {}

    self._file = File( configPath, json.dumps( self.defaultConfig ) )
    self.load()

  # <!-- GETTERS AND SETTER

  @property
  def defaultConfig( self ): return self._defaultConfig.copy()

  @defaultConfig.setter
  def defaultConfig( self, value: dict ) -> None:
    assert isinstance( value, dict ) 
    self._defaultConfig = value

  @property
  def file( self ): return deepcopy( self._file )

  @file.setter
  def file( self, value: File ) -> None:
    assert isinstance( value, File )
    self._file = value

  @property
  def config( self ): return self._config.copy()

  @config.setter
  def config( self, value: dict ) -> None:
    assert isinstance( value, dict ) 
    self._config = value

  # -->

  def load( self ) -> None:
    self.config = json.loads( self.file.read() )

  def save( self ) -> None:
    self.file.write( json.dumps( self.config ) )

  def field( self, key: Any, value: Optional[Any] = None ) -> Any:
    if value is None:
      return self.config[key]
    else:
      self.config[key] = value

  def reset( self ) -> None:
    path = self.file.path
    self.file = File( path, json.dumps( self.defaultConfig ) )