from mcculw import ul
from mcculw.enums import DigitalIODirection,DigitalPortType
from mcculw.ul import ULError
import os,sys



board_num = 0
channel = int(sys.argv[3])
do =int(sys.argv[1])
try:
	ul.d_config_port(board_num, DigitalPortType.FIRSTPORTA, DigitalIODirection.OUT)
except:
	pass
ul.d_out(board_num, DigitalPortType.FIRSTPORTA, do)
