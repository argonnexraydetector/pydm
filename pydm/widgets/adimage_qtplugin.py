from .qtplugin_base import qtplugin_factory
from .adimage import PyDMADImageView

print "adimage plugin "


PyDMADImageViewPlugin = qtplugin_factory(PyDMADImageView)

