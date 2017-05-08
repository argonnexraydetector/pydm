# pydm: Python Display Manager
pydm is a PyQt-based framework for building user interfaces for control systems.  The goal is to provide a no-code, drag-and-drop system to make simple screens, as well as a straightforward python framework to build complex applications.

# Prerequisites
* Python 2.7 or 3.5
* Qt 4.8 or higher
* PyQt4 >=4.11 or PyQt5 >= 5.7
If you'd like to use Qt Designer (drag-and-drop tool to build interfaces) you'll need to make sure you have the PyQt plugin for Designer installed.  This usually happens automatically when you install PyQt from source, but if you install it from a package manager, it may be left out.

Python package requirements are listed in the requirements.txt file, which can be used to install all requirements from pip: 'pip install -r requirements.txt'

# PyQt4 and PyQt5
PyDM can use either version of PyQt.  By default, it will first try to use PyQt4, and if that fails to import, it will try to use PyQt5.  If you'd like to force PyDM to use one or the other, you can set an environment variable named PYDM_QT_LIB to either 'PyQt4' or 'PyQt5'.  If you force a particular PyQt version, you will also have to force pyqtgraph to use the same version as PyDM, which you can do with its own environment variable: PYQTGRAPH_QT_LIB.

# Running the Examples
There are various examples of some of the features of the display manager.
To launch a particular display run 'python pydm.py <filename>'.

There is a 'home' display in the examples directory with buttons to launch all the examples:
run 'python pydm.py examples/home.ui'

There isn't any documentation yet, hopefully looking at the examples can get you started.

#Widget Designer Plugins
pydm widgets are written in Python, and are loaded into Qt Designer via the PyQt Designer Plugin.
If you want to use the pydm widgets in Qt Designer, add the pydm directory (which holds designer_plugin.py) to your PYQTDESIGNERPATH environment variable.  Eventually, this will happen automatically in some kind of setup script.

================================================================================

APS setup for linux anaconda


How to set up:
1) git clone the pydm into your local area. 
    mkdir pyDM
    git clone https://github.com/argonnexraydetector/pydm.git
    YOu then get a new dir pydm
    
    
2) YOu need a python with all proper modules. anaconda python has most of them. PyQt4 works fine.
3) install needed modules. You will need to get py qtgraph from MIT. http://www.pyqtgraph.org/
    download the tar ball.
    tar -xvf pyqtgraph-0.10.0.tar.gz
    
    no build or install necessary. You just add the path to the py files, pyqtgraph/pyqtgraph, into your Python path
    
4) add pydm into your python path. also pyqtgraph.
   setenv PYTHONPATH /home/beams/TMADDEN/ROACH/pyqtgraph:/home/beams/TMADDEN/swWork/pyDM/pydm
 
5) Run a ui screen.   
I am running anaconda python here:
How to run some files:
cd /home/beams0/TMADDEN/swWork/pyDM/pydm
/APSshare/anaconda/x86_64/bin/python pydm.py maddog/simdet.ui


pydm can run either py files, or ui files. It is easiest to run the ui files so you don't have to ever
run pyuic4, to convert ui to py.



To use QTDesigner:
You must use the QTdesigner that comes with PyQT. if you are a QT programmer, you may have instlled QTCreator
somewhere on your sustem. Do not use this, as it was robably built w/ wrong c compiler, and won't know about your
python, QT install. Anaconada includes designer when PyQT is installed:
You run QTDesigner like this:

export PYTHONHOME=/APSshare/anaconda/x86_64
export PYQTDESIGNERPATH=/home/beams/TMADDEN/swWork/pyDM/pydm
/APSshare/anaconda/x86_64/bin/designer


When you start QTDesigner you should see the pyDM widgets.

To Draw a screen:
Take a screen that already works, like indicators.ui from the exampols. Rename and make a new file.
For some reason, I cannot start  a new Mainwindow. it ends up being the wrong class,  but needs to be a PyDM main window.
A QMainwindow will not work. Easisiet to start w/ example ui file that works. 

Open in QTDesigner. 
You should see the pyDM widgets.
Add widgets to your screen. 
Save into pydm/maddog/myfile.ui

You do NOT have to convert the ui file to py. pydm does it for you. No need to manually run pyuic4.

run the screen:
/APSshare/anaconda/x86_64/bin/python pydm.py maddog/myfile.ui


Creating a new Widget:
Goto pydm/widgets
1) Copy a widget to new filename. copy the  oldwidget.py and oldwidget_plugin.py to new file names.
2) IN new_widget.py, rename class and constructor. 
3) In the newwidget_plugin.py, edit the import and factory line to match new widget.
4)Edit pydm/designer_plugin.py to add a new line for your widget.

5) Restart QTDesigner, you should see new widget.

To make your widget do something:

In the widget.py code you can edit the slots to do new things. 
To add fields to QTDesigner, or propertuies, add a qtproperties line. 
To add channels that get connected, and monitored, add a line to getchannels function at bottom.
All connected channels are monitored. To get non-monitored channel,. like AD image, add the property to add the channel,
but do not add to getchannels, so it is not connected. you do a local caget to get the data.






