command=ptz_req&req="+req+"&param="+param+"&channel="+g_viewStatu[g_clicked].nchannel+"&stream="+g_channelStatu[g_viewStatu[g_clicked].nchannel


# Control commands (reconfig for up):
import urllib2
import urllib2 as ul
cmd = 'http://10.10.10.13/?command=ptz_req&req=start&param=directionleft&channel=1&stream=0'
print cmd
http://10.10.10.13/?command=ptz_req&req=start&param=directionleft&channel=1&stream=0
cmd_stop ='http://10.10.10.13/?command=ptz_req&req=stop&param=directionleft&channel=1&stream=0' 
response = ul.urlopen(cmd)
response = ul.urlopen(cmd_stop)
cmd = 'http://10.10.10.13/?command=ptz_req&req=start&param=directionright&channel=1&stream=0'
cmd_stop ='http://10.10.10.13/?command=ptz_req&req=stop&param=directionright&channel=1&stream=0' 
response = ul.urlopen(cmd)
response = ul.urlopen(cmd_stop)

# Move right:
command=ptz_req&req=start&param=directionleft&channel=1&stream=0

# Move left:
command=ptz_req&req=start&param=directionright&channel=1&stream=0

# Look up:
command=ptz_req&req=start&param=directiondown&channel=1&stream=0

# Look down:
command=ptz_req&req=start&param=directionup&channel=1&stream=0

# Zoom in:
command=ptz_req&req=start&param=zoomtile&channel=1&stream=0

# Zoom out:
command=ptz_req&req=start&param=zoomwide&channel=1&stream=0
