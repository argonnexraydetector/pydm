from ..PyQt.QtGui import QPushButton
from ..PyQt.QtCore import pyqtSlot, pyqtProperty
import shlex, subprocess

class PyDMPythonCommand(QPushButton):
  def __init__(self, parent=None, command=None):
    super(PyDMPythonCommand, self).__init__(parent)
    self._command = command
    self.process = None

  def getCommand(self):
    return str(self._command)

  def setCommand(self, value):
    if self._command != value:
      self._command = str(value)

  def resetCommand(self):
    if self._command is not None:
      self._command = None

  def mouseReleaseEvent(self, mouse_event):
    self.execute_command()
    super(PyDMPythonCommand, self).mouseReleaseEvent(mouse_event)

  @pyqtSlot()
  def execute_command(self):
  
    exec(self._command)

  command = pyqtProperty(str, getCommand, setCommand, resetCommand)
