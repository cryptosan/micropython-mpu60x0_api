## MPU-6000, and MPU-6050 API for micro-python
This library is for using MPU-60X0 chip on micro-python

## Quick-ref
Code 1 (Inherit):
```python
from api6050.mpuapi import MPU6050_API as mpuAPI
...

class my_mpu_class(mpuAPI):
  def __init__(self, ...):
    mpuAPI.__init__(self)   # using default settings
    ...
    
```

Code 2 (Interpreter):
```python
>> from api6050.mpuapi import MPU6050_API as mpuAPI
>> mpu = mpuAPI()    # using default settings
>> # mpu = mpuAPI(0x42, bus=False, mode=False)  # Access to port 2, mode is SLAVE, and
                                                # the slave device has 0x42 address
>> mpu.is_device_ready()
True
>> mpu.get_addr()
104
```

## Class
### Don't touch this values directly
|Attributes | Description |
|:---------:|:-----------:|
| _BUS      | Selects the device bus, 1 (X9, X10), or 2 (Y9, Y10) |
| _MODE     | Selects the device mode, MASTER, or SLAVE |
| _TIMEOUT  | Timeout value to wait for the read, and write |
| _ERROR    | Error code |
| _ADDR     | The address variable to set, get the I2C Master device |

### Methods
| Name | Return |Parameters|
|:----:|:------:|:--------:|
|\__init__|None|addr=reg.I2C_ADDRESS, bus=True, mode=True|
|_dev_init|None|mode, addr=0x12, baudrate=400000, gencall=False|
|_dev_rm|None|None|
|is_device_ready|Boolean|None|
|get_addr|int|None|
|set_addr|None|addr|
|get_timeout|int|None|
|set_timeout|None|timeout|
|_read|bytes|buf, memaddr, timeout=5000, addr_size=8|
|_write|None|buf, memaddr, timeout=5000, addr_size=8|

## API
####``MPU6050_API(addr=reg.I2C_ADDRESS, bus=True, mode=True)``   
#####this is a constructor
``'addr'`` is the address of I2C device, default is 0x68 = regMap.I2C_ADDRESS   
``'bus'`` is that can select the I2C bus, ``True`` is X9/X10, ``False`` is Y9/Y10  
``'mode'`` is that can select the I2C mode, ``True`` is MASTER, ``False`` is SLAVE  

--------------
####``_dev_init(mode, addr=0x12, baudrate=400000, gencall=False)``
#####Init I2C object manually  
``'mode'`` is that can select I2C device mode, MASTER, or SLAVE  
``'addr'`` is 7-bit address (only sensible for a slave)  
``'baudrate'`` is the scl clock rate (only sensible for a master)   
``'gencall'`` is whether to support general call mode 

--------------
####``_dev_rm()``   
#####De-init I2C object  

--------------
####``is_device_ready()``   
#####Check the connection between pyBoard and MPU60X0 chip   
return is ``True``, or ``False``  

--------------
####``get_addr()``  
#####Get the address of the MPU60X0 chip   
return is ``int`` (The address of the device)   

--------------
####``set_addr(addr)``  
#####Set the address of the MPU60X0 chip   
#####* Be careful using this method  
``'addr'`` is the address to set  

--------------
####``get_timeout()``   
#####Get the timeout value   
return is ``int`` (The timeout value)   

--------------
####``set_timeout(timeout)``  
#####Set the timeout value   
``'timeout'`` is the timeout value to set   

--------------
####``_read(buf, memaddr, timeout=5000, addr_size=8)``  
#####Read from the memory of a MPU60X0 chip  
``'buf'`` is size of bytes to read from memory address  
``'memaddr'`` is the memory address of the device   
``'timeout'`` is miliseconds to wait for the read	
``'addr_size'`` is that can select width of memory address size: 8 or 16 bits  
return is ``bytes`` (The read data)   

--------------
####``_write(buf, memaddr, timeout=5000, addr_size=8)``   
#####Write to the memory of a MPU60X0 chip   
``'buf'`` is size of bytes to write to memory address   
``'memaddr'`` is the memory address of the device   
``'timeout'`` is miliseconds to wait for the write  
``'addr_size'`` is that can select width of memory address size: 8 or 16 bits  