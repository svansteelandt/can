import can

bus = can.interface.Bus(channel='can0', bustype='socketcan_native')

while True:
	notifier = can.Notifier(bus, [can.Printer()])