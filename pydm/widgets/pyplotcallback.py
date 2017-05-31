from ..PyQt.QtGui import QLabel, QApplication, QColor, QActionGroup,QWidget
from ..PyQt.QtCore import pyqtSignal, pyqtSlot, pyqtProperty

import numpy as np

import matplotlib.pyplot as mpl
mpl.rcParams['backend.qt4']='PyQt4'

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure



from .channel import PyDMChannel
from .colormaps import cmaps
import epics


from addons import *


class PyDMPyplotCallback(QWidget):
  
  # when mon channel changes, we call a pyfunction defined in the string pyfunction. arg chennel is another PV , an int that gets sent as arg to the py function
  #pyfucntion is a global function that is def function(intarg,figure):
  #figure is the Figure obj of this widget, passed to the py function, so it can plot to this widget.
  def __init__(self, parent=None, mon_channel = None, arg_channel = None,  pyfunction = None):
        
        
    super(PyDMPyplotCallback, self).__init__(parent)
  
    self._monchannel = mon_channel
    self._argchannel = arg_channel
    self._pyfunction = pyfunction

      # Create the mpl Figure and FigCanvas objects. 
    self.dpi = 100
    
    
    self.fig = Figure((8, 5), dpi=self.dpi)
    self.canvas = FigureCanvas(self.fig)

    self.canvas.setParent(self)
    self.axes0 = self.fig.add_subplot(121)
    self.axes1 = self.fig.add_subplot(122)
    #self.axes1.set_ylabel('hello')
    #cid=self.canvas.mpl_connect('button_press_event', self.plotClick)

      
  
  
  
  @pyqtSlot(int)
  @pyqtSlot(float)
  @pyqtSlot(str)
  def receivePlotUpdate(self, new_counter):
    if new_counter is None:
      return
    
    
    print "receivePlotUpdate %s"%new_counter
    
 
    
    self.pyarg = int(epics.caget(self._argchannel[5:]))
   
    self.pycall ="%s(%d,self.axes0)"%(self._pyfunction,self.pyarg)
    
    print self.pycall

    exec(self.pycall)
    self.canvas.draw()
  
 
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


 

  
  def getMonChannel(self):
    return str(self._monchannel)
  
  def setMonChannel(self, value):
    if self._monchannel != value:
      self._monchannel = str(value)

  def resetMonChannel(self):
    if self._monchannel != None:
      self._monchannel = None

  
  monChannel = pyqtProperty(str, getMonChannel, setMonChannel, resetMonChannel)
  
  
  
  
  def getArgChannel(self):
    return str(self._argchannel)
  
  def setArgChannel(self, value):
    if self._argchannel != value:
      self._argchannel = str(value)

  def resetArgChannel(self):
    if self._argchannel != None:
      self._argchannel = None

  
  argChannel = pyqtProperty(str, getArgChannel, setArgChannel, resetArgChannel)
  
  
  
  
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
    return [PyDMChannel(
        address=self.monChannel, 
        connection_slot=self.connectionStateChanged, 
        value_slot=self.receivePlotUpdate, 
        severity_slot=self.alarmSeverityChanged)]
