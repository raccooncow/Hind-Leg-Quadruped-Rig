# Hind-Leg-Quadruped-Rig

## Demo
Demo Video: 

## GitHub Repository
GitHub Repo: https://github.com/raccooncow/Hind-Leg-Quadruped-Rig.git

## Description
This script creates a quad hind-leg IK setup in Maya by building a paw and foot-roll control, adding IK handles and a knee pole-vector control, organizing them into a clean hierarchy, zeroing transforms, and hiding the IK handles for clean animation use.

### Key Features
The following are all the things this Python code tool accomplishes.

NOTE: The user must create a joint chain that looks/is named like this: hip → knee → ankle → hock → toe

- Validates that five joints are selected in order: hip → knee → ankle → hock → toe.
- Creates a paw control and group aligned to the hock joint.
- Orients paw control flat and zeroes out transforms.
- Creates a foot roll control and positions it at the hock.
- Creates 3 IK handles:
    - toe_IKH
    - knee_IKH
    - hock_IKH
- Groups toe_IKH and hock_IKH under IKH_GRP, and parents it under the foot roll hierarchy.
- Creates a knee pole vector control and positions it in front of the knee.
- Connects the pole vector control to knee_IKH.
- Creates a group for knee_IKH and snaps its pivot to the hock.
- Freezes, transforms, and deletes history on all major controls/groups.
- Centers pivot for knee PV control and group.
- Hides all IK handles.

### File Structure
Hind-Led-Quadruped-Rig.py – Copy and Paste into Maya script editor code.

README.md – Project overview, instructions, and descriptions.
