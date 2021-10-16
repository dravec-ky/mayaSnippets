import maya.cmds as mc
import maya.api.OpenMaya as om

def OMAnalyze(*pArgs):
    Sel = mc.ls(sl=True)
    mc.select(Sel, hi=True)
    Sel = mc.ls(sl=True)
    print("\nCmds hierarchy: "+str(Sel))
    _MOSel = om.MGlobal.getActiveSelectionList()
    fnSel = []
    for x in range(int(_MOSel.length())):
        tempObject = _MOSel.getDependNode(x)
        fnSel.append(tempObject)
        tempDagNode = om.MFnDagNode().setObject(tempObject)
        print("\n"+str(x)+" - " + tempDagNode.fullPathName())
        print("Object type: " + str(tempObject.apiType()) + " - " + tempObject.apiTypeStr)
        print("No. parents: " + str(tempDagNode.parentCount()))
        if tempObject.apiType() == 110:
            print("Transform Matrix: " + str(om.MFnTransform().setObject(tempObject).transformationMatrix()))

def createUI():
    windowID = "myWindow"
    if mc.window(windowID, exists=True):
        mc.deleteUI(windowID)
    mc.window(windowID, title="OMAnalyze", widthHeight=(100,30))

    mc.columnLayout( adjustableColumn=True )
    mc.button(label = "OM Analyze", command=OMAnalyze)
    mc.showWindow()

createUI()
