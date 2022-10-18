# Ntrip Client
Initiated by Oscar Siu

 **Last update: 13 Sep 2022**

Ntrip client to collect network RTK GNSS data and decode to RTCM message through python.

This project is a modified version based on https://github.com/jcmb/NTRIP

Reference: (https://www.geodetic.gov.hk/sc/satref/kf_rawstream.htm) 

	Usage: NtripClient.py [options] [caster] [port] mountpoint

	Options:
	  --version             show program's version number and exit
	  -h, --help            show this help message and exit
	  -u USER, --user=USER  The Ntripcaster username.  Default: IBS
	  -p PASSWORD, --password=PASSWORD
							The Ntripcaster password. Default: IBS
	  -o ORG, --org=ORG     Use IBSS and the provided organization for the user.
							Caster and Port are not needed in this case Default:
							none
	  -b BASEORG, --baseorg=BASEORG
							The org that the base is in. IBSS Only, assumed to be
							the user org
	  -t LAT, --latitude=LAT
							Your latitude.  Default: 22.3
	  -g LON, --longitude=LON
							Your longitude.  Default: 114.18
	  -e HEIGHT, --height=HEIGHT
							Your ellipsoid height.  Default: 20
	  -v, --verbose         Verbose
	  -s, --ssl             Use SSL for the connection
	  -T, --Tell			Tell Settings
	  -H, --host            Include host header, should be on for IBSS
	  -r MAXRECONNECT, --Reconnect=MAXRECONNECT
							Number of reconnections
	  -D UDP, --UDP=UDP     Broadcast recieved data on the provided port
	  -2, --V2              Make a NTRIP V2 Connection
	  -f OUTPUTFILE, --outputFile=OUTPUTFILE
							Write to this file, instead of stdout
	  -m MAXCONNECTTIME, --maxtime=MAXCONNECTTIME
							Maximum length of the connection, in seconds
	  --Header              Write headers to stderr
	  --HeaderFile=HEADERFILE
							Write headers to this file, instead of stderr.

 #### Command: python ntrip_client.py -u hkast -p hkast941 -m 1000  -r 100 -v -D 9999  59.152.234.19 2103 HKST -f log/test.log -t 22.4264184 -g 114.2033127

Debugging log files and binary data texts can be found in the log folder.
