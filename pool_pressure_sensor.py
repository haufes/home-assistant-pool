import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
values = []
#take 30 measurements and average to even out the jitter
for x in range(0, 30):
   values.append(float(mcp.read_adc(0)))
   time.sleep(.3)

#print values
#values.sort()
#print values
#value = values[len(values)/2]
value = sum(values)/len(values)
#print value


print '{{ "raw":"{0}", "psi":"{1}" }}'.format(value, round(float(value) * 5/22  - 260/11, 2))
