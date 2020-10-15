from typing import Optional, Any

import eel
from copy import deepcopy

from Libs import File, ConfigManager#, VideoManager, TestsManager, HealthNotebookManager

class App:

  def __init__( self, configPath: str, defaultConfig: str ) -> None:
    self._configManager = ConfigManager( configPath, defaultConfig )
    #self._videoManager = VideoManager()
    #self._testsManager = TestsManager()
    #self._healthNotebookManager = HealthNotebookManager()

  # <!-- GETTERS AND SETTERS

  @property
  def configManager( self ): return deepcopy( self._configManager )

  @configManager.setter
  def configManager( self, value: configManager ):
    assert isinstance( value, configManager )
    self._configManager = value

  """

  @property
  def videoManager( self ): return deepcopy( self._videoManager )

  @videoManager.setter
  def videoManager( self, value: videoManager ):
    assert isinstance( value, videoManager )
    self._videoManager = value

  @property
  def testsManager( self ): return deepcopy( self._testsManager )

  @testsManager.setter
  def testsManager( self, value: testsManager ):
    assert isinstance( value, testsManager )
    self._testsManager = value

  @property
  def healthNotebookManager( self ): return deepcopy( self._healthNotebookManager )

  @healthNotebookManager.setter
  def healthNotebookManager( self, value: healthNotebookManager ):
    assert isinstance( value, healthNotebookManager )
    self._healthNotebookManager = value

  """

  # -->

  def start( self, webFolderPath: str, startPageName: str ) -> None:
    eel.init( webFolderPath )
    eel.start( startPageName, port = 0 )

  def electronToPython( self, command: str ) -> None:
    eval( command )
    
if __name__ == '__main__':

  configPath = 'config.json'
  defaultConfig = {

    'name': None,
    'sport': None,
    'faculty': None,
    'studyGroup': None,
    'course': None,
    'attentionDays': None,
    'healthGroup': None,
    'youtubeAPIKey': None,
    'moodleAPIKey': None,
    'lastVideoPath': None,
    'lastHealthNotebookPath': None

  }

  webFolderPath = 'Web'
  startPageName = 'index.html'

  app = App( configPath, defaultConfig )
  app.start( webFolderPath, startPageName )