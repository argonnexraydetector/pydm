from ..PyQt.QtGui import QLabel, QApplication, QColor
from ..PyQt.QtCore import pyqtSignal, pyqtSlot, pyqtProperty
from pyqtgraph import PlotWidget
from pyqtgraph import PlotCurveItem
import numpy as np
from .baseplot import BasePlot
from .channel import PyDMChannel


from addons import *


class PyDMWaveformSmartPlot(BasePlot):
  def __init__(self, parent=None, init_x_channel=None, init_y_channel=None, background='default', pyfunction=None):
    super(PyDMWaveformSmartPlot, self).__init__(parent, background)
    self._ychannel = init_x_channel
    self._xchannel = init_y_channel
    self.x_waveform = None
    self.y_waveform = None
    self._pyfunction = pyfunction
  
  @pyqtSlot(np.ndarray)
  def receiveXWaveform(self, new_waveform):
    self.x_waveform = new_waveform
    # just call redraw if y_waveform has vale
    #if self.y_waveform is not None:
    self.redrawPlot()
  
  @pyqtSlot(np.ndarray)
  def receiveYWaveform(self, new_waveform):
    self.y_waveform = new_waveform
    self.redrawPlot()

  def updateAxes(self):
    if self.y_waveform is None:
      return
    if self.x_waveform is None:
      yspan = float(np.amax(self.y_waveform)) - float(np.amin(self.y_waveform))
      self.plotItem.setLimits(xMin=0, xMax=len(self.y_waveform), yMin=float(np.amin(self.y_waveform)-yspan), yMax=float(np.amax(self.y_waveform)+yspan))
    else:
      # let the y and x shapes equals
      if self.x_waveform.shape[0] > self.y_waveform.shape[0]:
          self.x_waveform = self.x_waveform[:self.y_waveform.shape[0]]
      elif self.x_waveform.shape[0] < self.y_waveform.shape[0]:
          self.y_waveform = self.y_waveform[:self.x_waveform.shape[0]]
      self.plotItem.setLimits(xMin=np.amin(self.x_waveform), xMax=np.amax(self.x_waveform), yMin=np.amin(self.y_waveform), yMax=np.amax(self.y_waveform))
  
  def redrawPlot(self):

    self.pycall ="(self.newwavex,self.newwavey) = %s(self.x_waveform, self.y_waveform)"%(self._pyfunction)
    
    #print self.pycall

    exec(self.pycall)

    self.updateAxes()
    self.curve.setData(x=self.newwavex, y=self.newwavey)
  
  # -2 to +2, -2 is LOLO, -1 is LOW, 0 is OK, etc.  
  @pyqtSlot(int)
  def alarmStatusChanged(self, new_alarm_state):
    pass
  
  #0 = NO_ALARM, 1 = MINOR, 2 = MAJOR, 3 = INVALID  
  @pyqtSlot(int)
  def alarmSeverityChanged(self, new_alarm_severity):
    pass
    
  #false = disconnected, true = connected
  @pyqtSlot(bool)
  def connectionStateChanged(self, connected):
    pass
  
  def getYChannel(self):
    return str(self._ychannel)
  
  def setYChannel(self, value):
    if self._ychannel != value:
      self._ychannel = str(value)

  def resetYChannel(self):
    if self._ychannel != None:
      self._ychannel = None
    
  yChannel = pyqtProperty(str, getYChannel, setYChannel, resetYChannel)
  
  def getXChannel(self):
    return str(self._xchannel)
  
  def setXChannel(self, value):
    if self._xchannel != value:
      self._xchannel = str(value)

  def resetXChannel(self):
    if self._xchannel != None:
      self._xchannel = None
    
  xChannel = pyqtProperty(str, getXChannel, setXChannel, resetXChannel)
 
  def getPyFunction(self):
    return str(self._pyfunction)
  
  def setPyFunction(self, value):
    if self._pyfunction != value:
      self._pyfunction = str(value)

  def resetPyFunction(self):
    if self._pyfunction != None:
      self._pyfunction = None

  
  pyFunction = pyqtProperty(str, getPyFunction, setPyFunction, resetPyFunction)
  

  def channels(self):
    return [PyDMChannel(address=self.yChannel, connection_slot=self.connectionStateChanged, waveform_slot=self.receiveYWaveform, severity_slot=self.alarmSeverityChanged), PyDMChannel(address=self.xChannel, connection_slot=self.connectionStateChanged, waveform_slot=self.receiveXWaveform, severity_slot=self.alarmSeverityChanged)]
