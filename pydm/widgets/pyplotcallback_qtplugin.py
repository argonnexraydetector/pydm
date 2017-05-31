from .qtplugin_base import qtplugin_factory
from .pyplotcallback import PyDMPyplotCallback

print "PyDMPyplotCallback plugin "


PyDMPyplotCallbackPlugin = qtplugin_factory(PyDMPyplotCallback)

