#AquaIntPhidget

# For use with Aquaresp.com
# Author: Morten Bo Soendergaard Svendsen, fishiology.dk/comparativ.com, April 2016

import sys
from Phidgets.Devices.InterfaceKit import InterfaceKit
ik = InterfaceKit()
ik.openPhidget()
ik.waitForAttach(10000)
ik.setOutputState(int(sys.argv[1]),int(sys.argv[2]))