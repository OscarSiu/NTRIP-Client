#pip install pyrtcm

from pyrtcm import RTCMReader
stream = open('test.log', 'rb')
rtr = RTCMReader(stream)
for (raw_data, parsed_data) in rtr: 
	print(parsed_data)
	print('\n')
