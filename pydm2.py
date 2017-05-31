#!/usr/bin/env python
import sys
import argparse
from pydm import PyDMApplication
import json



def runPyDM(ui=None, disp_args = [], pfmon=None, mcro=None):

    app = PyDMApplication(
        ui_file=ui, 
        command_line_args=disp_args, 
        perfmon=pfmon, 
        macros=mcro)
    app.exec_()


