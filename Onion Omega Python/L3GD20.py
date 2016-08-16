# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# L3GD20
# This code is designed to work with the L3GD20_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/products

from OmegaExpansion import onionI2C
import time

# Get I2C bus
i2c = onionI2C.OnionI2C()

# L3GD20 address, 0x6A(106)
# Select Control register1, 0x20(32)
#		0x0F(15)	Normal mode, X, Y, Z-Axis enabled
i2c.writeByte(0x6A, 0x20, 0x0F)
# L3GD20 address, 0x6A(106)
# Select Control register4, 0x23(35)
#		0x30(48)	Continous update, Data LSB at lower address
#					FSR 2000dps, Self test disabled, 4-wire interface
i2c.writeByte(0x6A, 0x23, 0x30)

time.sleep(0.5)

# L3GD20 address, 0x6A(106)
# Read data back from 0x28(40), 2 bytes, X-Axis LSB first
data0 = i2c.readBytes(0x6A, 0x28, 1)
data1 = i2c.readBytes(0x6A, 0x29, 1)

# Convert the data
xGyro = data1 * 256 + data0
if xGyro > 32767 :
	xGyro -= 65536

# L3GD20 address, 0x6A(106)
# Read data back from 0x2A(42), 2 bytes, Y-Axis LSB first
data0 = i2c.readBytes(0x6A, 0x2A, 1)
data1 = i2c.readBytes(0x6A, 0x2B, 1)

# Convert the data
yGyro = data1 * 256 + data0
if yGyro > 32767 :
	yGyro -= 65536

# L3GD20 address, 0x6A(106)
# Read data back from 0x2C(44), 2 bytes, Z-Axis LSB first
data0 = i2c.readBytes(0x6A, 0x2C, 1)
data1 = i2c.readBytes(0x6A, 0x2D, 1)

# Convert the data
zGyro = data1 * 256 + data0
if zGyro > 32767 :
	zGyro -= 65536

# Output data to screen
print "Rotation in X-Axis : %d" %xGyro
print "Rotation in Y-Axis : %d" %yGyro
print "Rotation in Z-Axis : %d" %zGyro
