# -*- coding: mbcs -*-
# Do not delete The following import lines
from abaqus import *
from abaqusConstants import *
from symbolicConstants import *
from odbAccess import *
import __main__
import csv
import os,sys
import numpy as np
import subprocess
# from abapy import *
import json


def Print_conter():
    import os 
    vp = session.viewports[session.currentViewportName]
    odb = session.odbs[vp.odbDisplay.name]
    p_dir_name = r"C:\Users\struct17\Desktop\T-joint_conter"
    c_dir_name = odb.name.replace('.odb','')
    try:
        os.mkdir(os.path.join(p_dir_name,c_dir_name))
    except Exception as e:
        pass
    vo = vp.viewportAnnotationOptions
    vp.viewportAnnotationOptions.setValues(triad=OFF, 
        legend=ON, title=OFF, state=OFF, annotations=OFF, compass=OFF)
    session.printOptions.setValues(compass=OFF)
    view = vp.view
    # view.setProjection(projection=PARALLEL)
    view.setValues(session.views['Front'])
    # view.setValues(session.views['User-1'])
    # view.setValues(session.views['Iso'])
    keys = [['U',NODAL,'U3',(-4,-3.5,-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1.0)],
        ['S',INTEGRATION_POINT,'S11',(-300,-200,-100,0,100,200,300,400,500,600)],
        ['S',INTEGRATION_POINT,'S22',(-300,-200,-100,0,100,200,300,400,500,600)]]
    for key in keys:
        vp.odbDisplay.setPrimaryVariable(
            variableLabel=key[0], outputPosition=key[1], refinement=(
            COMPONENT, key[2]), )
        vp.odbDisplay.display.setValues(plotState=(
            CONTOURS_ON_UNDEF, ))
        vp.odbDisplay.basicOptions.setValues(sectionResults=USE_BOTTOM_AND_TOP)
        vp.odbDisplay.contourOptions.setValues(
            intervalType=USER_DEFINED, intervalValues=key[3])
        session.printToFile(fileName=os.path.join(p_dir_name,c_dir_name,key[2]), format=PNG, canvasObjects=(vp, ))
    print 'printed'

