import maya.cmds as cmds

selection = cmds.ls(sl=True)
if len(selection) != 5:
    cmds.error("Please select these joints in this order: hip → knee → ankle → hock → toe")
hip, knee, ankle, hock, toe = selection

paw_CON = cmds.circle(name='paw_CON', normal=[1,0,0], radius=1.5)[0]
paw_GRP = cmds.group(paw_CON, name='paw_GRP')
hock_pos = cmds.xform(hock, q=True, ws=True, t=True)
paw_grp_pos = [hock_pos[0], 0, hock_pos[2]]
cmds.xform(paw_GRP, ws=True, t=paw_grp_pos)
cmds.setAttr(paw_CON + ".rotateZ", 90)
cmds.makeIdentity(paw_CON, apply=True, t=1, r=1, s=1, n=0)
cmds.delete(paw_CON, ch=True)
cmds.makeIdentity(paw_GRP, apply=True, t=1, r=1, s=1, n=0)
cmds.delete(paw_GRP, ch=True)


footRoll_CON = cmds.circle(name='footRoll_CON', normal=[1,0,0], radius=1.0)[0]
footRoll_GRP = cmds.group(empty=True, name='footRoll_GRP')
cmds.xform(footRoll_CON, ws=True, t=hock_pos)
cmds.xform(footRoll_GRP, ws=True, t=hock_pos)
cmds.setAttr(footRoll_CON + ".rotateZ", 90)
cmds.makeIdentity(footRoll_CON, apply=True, t=1, r=1, s=1, n=0)
cmds.delete(footRoll_CON, ch=True)
cmds.makeIdentity(footRoll_GRP, apply=True, t=1, r=1, s=1, n=0)
cmds.delete(footRoll_GRP, ch=True)


toe_IKH = cmds.ikHandle(sj=hock, ee=toe, sol='ikSCsolver', name='toe_IKH')[0]
knee_IKH = cmds.ikHandle(sj=hip, ee=ankle, sol='ikRPsolver', name='knee_IKH')[0]
hock_IKH = cmds.ikHandle(sj=ankle, ee=hock, sol='ikSCsolver', name='hock_IKH')[0]
IKH_GRP = cmds.group([toe_IKH, hock_IKH], name='IKH_GRP')
cmds.makeIdentity(IKH_GRP, apply=True, t=1, r=1, s=1, n=0)
cmds.delete(IKH_GRP, ch=True)


cmds.parent(IKH_GRP, footRoll_CON)
cmds.parent(footRoll_CON, footRoll_GRP)
cmds.parent(footRoll_GRP, paw_CON)


knee_PV_CON = cmds.curve(
    name='knee_PV_CON',
    d=1,
    p=[(0,0,0),(1,2,0),(-1,2,0),(0,0,0)]
)
knee_PV_GRP = cmds.group(knee_PV_CON, name='knee_PV_GRP')
cmds.setAttr(knee_PV_CON + ".rotateX", 90)
cmds.setAttr(knee_PV_CON + ".rotateY", 90)
cmds.makeIdentity(knee_PV_CON, apply=True, t=1, r=1, s=1, n=0)
cmds.delete(knee_PV_CON, ch=True)
knee_pos = cmds.xform(knee, q=True, ws=True, t=True)
pv_offset = 5.0
pv_pos = [knee_pos[0] + pv_offset, knee_pos[1], knee_pos[2]]
cmds.xform(knee_PV_GRP, ws=True, t=pv_pos)
cmds.makeIdentity(knee_PV_GRP, apply=True, t=1, r=1, s=1, n=0)
cmds.delete(knee_PV_GRP, ch=True)


cmds.poleVectorConstraint(knee_PV_CON, knee_IKH)
cmds.parent(knee_PV_GRP, paw_CON)
knee_IKH_GRP = cmds.group(knee_IKH, name='knee_IKH_GRP')
cmds.parent(knee_IKH_GRP, paw_CON)
cmds.xform(knee_IKH_GRP, ws=True, rp=hock_pos)
cmds.makeIdentity(knee_IKH_GRP, apply=True, t=1, r=1, s=1, n=0)
cmds.delete(knee_IKH_GRP, ch=True)


cmds.setAttr(toe_IKH + ".visibility", 0)
cmds.setAttr(hock_IKH + ".visibility", 0)
cmds.setAttr(knee_IKH + ".visibility", 0)