# User selects all properly named leg JNTs
# Get currently selected objects
# Confirm all five joints are selected
# Assign joints in order:
# hip, knee, ankle, hock, toe

# Create paw con + grp
# Create NURBS circle for paw con
# Group paw con
# Snap paw grp to hock jnt
# Rotate paw con so its flat
# Freeze transforms + clean history

# footRoll con + grp
# Create smaller NURBS circle for footRoll con
# Group footRoll con
# Snap con + grp to hock jnt
# Rotate footRoll con so its flat
# Freeze transforms + clean history

# IKH
# toe IKH (hock --> toe)
# main leg IKH (hip --> ankle)
# hock IKH (ankle --> hock)
# GRP toe + hock IKH together
# Freeze transforms on IKH group

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