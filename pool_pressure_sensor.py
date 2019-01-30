import time
from gpiozero import MCP3304

MCP3304(channel=0, device=0)
mcp = MCP3304(channel=0, device=0)

values = []
for x in range(0, 10):
   values.append(float(mcp.value))
   time.sleep(.1)

#print values
#values.sort()
#print values
#value = values[len(values)/2]
value = sum(values)/len(values)
#print value


print '{{ "raw":"{0}", "psi":"{1}"}}'.format(value, round(float(value) * 85.322921661613  - 8.6354168622984, 2))
