import maya.cmds as cmds

# User selects all properly named leg JNTs
# Get currently selected objects
# Confirm all five joints are selected
# Assign joints in order:
# hip, knee, ankle, hock, toe
selection = cmds.ls(sl=True)
if len(selection) != 5:
    cmds.error("Please select these joints in this order: hip → knee → ankle → hock → toe")
hip, knee, ankle, hock, toe = selection

# Create paw con + grp
# Create NURBS circle for paw con
paw_CON = cmds.circle(name='paw_CON', normal=[1,0,0], radius=1.5)[0]
# Group paw con
paw_GRP = cmds.group(paw_CON, name='paw_GRP')
# Snap paw grp to hock jnt
hock_pos = cmds.xform(hock, q=True, ws=True, t=True)
paw_grp_pos = [hock_pos[0], 0, hock_pos[2]]
cmds.xform(paw_GRP, ws=True, t=paw_grp_pos)
# Rotate paw con so its flat
cmds.setAttr(paw_CON + ".rotateZ", 90)
# Freeze transforms + clean history
cmds.makeIdentity(paw_CON, apply=True, t=1, r=1, s=1, n=0)
cmds.delete(paw_CON, ch=True)
cmds.makeIdentity(paw_GRP, apply=True, t=1, r=1, s=1, n=0)
cmds.delete(paw_GRP, ch=True)


# footRoll con + grp
# Create smaller NURBS circle for footRoll con
footRoll_CON = cmds.circle(name='footRoll_CON', normal=[1,0,0], radius=1.0)[0]
# Group footRoll con
footRoll_GRP = cmds.group(empty=True, name='footRoll_GRP')
# Snap con + grp to hock jnt
cmds.xform(footRoll_CON, ws=True, t=hock_pos)
cmds.xform(footRoll_GRP, ws=True, t=hock_pos)
# Rotate footRoll con so its flat
cmds.setAttr(footRoll_CON + ".rotateZ", 90)
# Freeze transforms + clean history
cmds.makeIdentity(footRoll_CON, apply=True, t=1, r=1, s=1, n=0)
cmds.delete(footRoll_CON, ch=True)
cmds.makeIdentity(footRoll_GRP, apply=True, t=1, r=1, s=1, n=0)
cmds.delete(footRoll_GRP, ch=True)


# IKH
# toe IKH (hock --> toe)
toe_IKH = cmds.ikHandle(sj=hock, ee=toe, sol='ikSCsolver', name='toe_IKH')[0]
# main leg IKH (hip --> ankle)
knee_IKH = cmds.ikHandle(sj=hip, ee=ankle, sol='ikRPsolver', name='knee_IKH')[0]
# hock IKH (ankle --> hock)
hock_IKH = cmds.ikHandle(sj=ankle, ee=hock, sol='ikSCsolver', name='hock_IKH')[0]
# GRP toe + hock IKH together
IKH_GRP = cmds.group([toe_IKH, hock_IKH], name='IKH_GRP')
# Freeze transforms on IKH group
cmds.makeIdentity(IKH_GRP, apply=True, t=1, r=1, s=1, n=0)
cmds.delete(IKH_GRP, ch=True)

# footRoll hierarchy
# Parent IKH under footRoll con
# Build hierarchy:
# paw_GRP, paw_CON, footRoll_GRP, footRoll_CON, IKH_GRP

# Knee PV con + grp
# Create triangle con knee PV
# Group PV con
# Rotate PV con con so its flat
# Freeze transforms + clean history
# PV con in front of knee

# Connect PV con to knee IKH
# Parent PV group under paw con
# Group knee IKH
# Parent it under paw con
# Move grp PV to hock jnt

# Cleanup freeze transform + delete history
# Cons have 0 transforms
# Pivots are centered
# Hide IKH from hierarchy