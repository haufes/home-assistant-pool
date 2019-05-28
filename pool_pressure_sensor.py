import time
from gpiozero import MCP3304

MCP3304(channel=0, device=0)
mcp = MCP3304(channel=0, device=0)

values = []
for x in range(0, 40):
   values.append(float(mcp.value))
   time.sleep(.2)

#print values
#values.sort()
#print values
#value = values[len(values)/2]
value = sum(values)/len(values)
#print value

psi =  round(float(value) * 231.86680571671 - 23.506555422694, 2)


print ("{{ \"raw\":\"{}\", \"psi\":\"{}\"}}".format(value, psi))

#https://keisan.casio.com/exec/system/1223508685

#MCP3304
#0 PSI = 0.101379562935 
#4.75 PSI = 0.121865462093