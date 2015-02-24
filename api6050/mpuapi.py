"""
	micropython-mpu60x0_api
	---------------------------------------------
	This is a MPU60X0 API for micro-python board by Yi Soo, An
	
	Compatibility
		* MPU6000 chip
		* MPU6050 chip

	Github : https://github.com/yisoo/micropython-mpu60x0_api
"""
from api6050 import regMap as reg
from pyb import I2C


class MPU6050_API():
	_BUS = (1, 2)
	_MODE = (I2C.MASTER, I2C.SLAVE)
	_TIMEOUT = 5000
	_ERROR = -1
	_ADDR = 0x00


	def __init__(self, addr=reg.I2C_ADDRESS, bus=True, mode=True):
		"""
		Init I2C object
		:param addr: An address of I2C Device, default is 0x68
		:param bus: Select the RX/TX bus of micro-python board
					True is (X9|SCL, X10|SDA), False is (Y9|SCL, Y10|SDA)
		:param mode: Select the I2C device mode, MASTER or SLAVE
		:return: None
		"""

		self._ADDR = addr
		if bus:
			self._mpu = I2C(self._BUS[0])
		else:
			self._mpu = I2C(self._BUS[1])

		# Init I2C object
		if mode:
			self._dev_init(self._MODE[0])
		else:
			self._dev_init(self._MODE[1])


	def _dev_init(self, mode, addr=0x12, baudrate=400000, gencall=False):
		"""
		Manually init I2C object 
		:param mode: Select I2C device mode, MASTER or SLAVE
		:param addr: 7-bit address (only sensible for a slave)
		:param baudrate: The SCL clock rate (only sensible for a master)
		:param gencall: Whether to support general call mode
		:return: None
		"""

		self._mpu.init(mode, addr=addr, baudrate=baudrate, gencall=gencall)


	def _dev_rm(self):
		"""
		De-init I2C object
		:return: None
		"""

		self._mpu.deinit()


	def is_device_ready(self):
		"""
		Check the connection between pyBoard and MPU60X0 Chip
		:return: Boolean
		"""

		return self._mpu.is_ready(self._ADDR)
	
	
	def get_addr(self):
		"""
		Get the address of the MPU60X0 chip
		:return: The address of the device
		"""
		return self._ADDR
	
	
	def set_addr(self, addr):
		"""
		Set the address of the MPU60X0 chip
		* Be careful for using this method!
		:param addr: The address to set
		:return: None
		"""
		self._ADDR = addr
		
		
	def get_timeout(self):
		"""
		Get the timeout value
		:return: The timeout value
		"""
		return self._TIMEOUT
	
	
	def set_timeout(self, timeout):
		"""
		Set the timeout value
		:param timeout: The timeout value to set
		:return: None
		"""
		self._TIMEOUT = timeout


	def _read(self, buf, memaddr, timeout=5000, addr_size=8):
		"""
		Read from the memory of a MPU60X0 chip
		:param buf: Size of bytes to read from memory address
		:param memaddr: The memory address of the device
		:param timeout: Miliseconds to wait for the read
		:param addr_size: Selects width of memory address size: 8 or 16 bits
		:return: The read data
		"""
		
		result = _ERROR
		
		# Check state of the device.
		# If it's false, it will return the _ERROR code.
		if self.is_device_ready():
			result = self._mpu.mem_read(buf, 
										self.get_addr(), 
										memaddr, 
										timeout=timeout, 
										addr_size=addr_size)

		return result


	def _write(self, buf, memaddr, timeout=5000, addr_size=8):
		"""
		Write to the memory of a MPU60X0 chip
		:param buf: Size of bytes to write to memory address
		:param memaddr: The memory address of the device
		:param timeout: Miliseconds to wait for the write
		:param addr_size: Selects width of memory address size: 8 or 16 bits
		:return: None
		"""

		# Check state of the device.
		# If it's false, this login won't do anything
		if self.is_device_ready():
			self._mpu.mem_write(buf, 
								self.get_addr(), 
								memaddr, 
								timeout=timeout, 
								addr_size=addr_size)