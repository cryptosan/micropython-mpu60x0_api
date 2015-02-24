"""
	MPU-60X0 Register Map by stanleyhuangyc.

	stanleyhuangyc's github: 
		https://github.com/stanleyhuangyc/ArduinoOBD/blob/master/libraries/MPU6050/MPU6050.h

	This library was ported from C/C++ to Python by Yi Soo, An

	Yi Soo, An's github: https://github.com/yisoo/micropython-mpu60x0_api

	Removed prefix 'MPU6050' for using easily
"""


# Register names according to the datasheet.
# According to the InvenSense document 
# "MPU-6000 and MPU-6050 Register Map 
# and Descriptions Revision 3.2", there are no registers
# at = 0x02 ... = 0x18, but according other information 
# the registers in that unknown area are for gain 
# and offsets.
# 
AUX_VDDIO          = 0x01   # R/W
SMPLRT_DIV         = 0x19   # R/W
CONFIG             = 0x1A   # R/W
GYRO_CONFIG        = 0x1B   # R/W
ACCEL_CONFIG       = 0x1C   # R/W
FF_THR             = 0x1D   # R/W
FF_DUR             = 0x1E   # R/W
MOT_THR            = 0x1F   # R/W
MOT_DUR            = 0x20   # R/W
ZRMOT_THR          = 0x21   # R/W
ZRMOT_DUR          = 0x22   # R/W
FIFO_EN            = 0x23   # R/W
I2C_MST_CTRL       = 0x24   # R/W
I2C_SLV0_ADDR      = 0x25   # R/W
I2C_SLV0_REG       = 0x26   # R/W
I2C_SLV0_CTRL      = 0x27   # R/W
I2C_SLV1_ADDR      = 0x28   # R/W
I2C_SLV1_REG       = 0x29   # R/W
I2C_SLV1_CTRL      = 0x2A   # R/W
I2C_SLV2_ADDR      = 0x2B   # R/W
I2C_SLV2_REG       = 0x2C   # R/W
I2C_SLV2_CTRL      = 0x2D   # R/W
I2C_SLV3_ADDR      = 0x2E   # R/W
I2C_SLV3_REG       = 0x2F   # R/W
I2C_SLV3_CTRL      = 0x30   # R/W
I2C_SLV4_ADDR      = 0x31   # R/W
I2C_SLV4_REG       = 0x32   # R/W
I2C_SLV4_DO        = 0x33   # R/W
I2C_SLV4_CTRL      = 0x34   # R/W
I2C_SLV4_DI        = 0x35   # R  
I2C_MST_STATUS     = 0x36   # R
INT_PIN_CFG        = 0x37   # R/W
INT_ENABLE         = 0x38   # R/W
INT_STATUS         = 0x3A   # R  
ACCEL_XOUT_H       = 0x3B   # R  
ACCEL_XOUT_L       = 0x3C   # R  
ACCEL_YOUT_H       = 0x3D   # R  
ACCEL_YOUT_L       = 0x3E   # R  
ACCEL_ZOUT_H       = 0x3F   # R  
ACCEL_ZOUT_L       = 0x40   # R  
TEMP_OUT_H         = 0x41   # R  
TEMP_OUT_L         = 0x42   # R  
GYRO_XOUT_H        = 0x43   # R  
GYRO_XOUT_L        = 0x44   # R  
GYRO_YOUT_H        = 0x45   # R  
GYRO_YOUT_L        = 0x46   # R  
GYRO_ZOUT_H        = 0x47   # R  
GYRO_ZOUT_L        = 0x48   # R  
EXT_SENS_DATA_00   = 0x49   # R  
EXT_SENS_DATA_01   = 0x4A   # R  
EXT_SENS_DATA_02   = 0x4B   # R  
EXT_SENS_DATA_03   = 0x4C   # R  
EXT_SENS_DATA_04   = 0x4D   # R  
EXT_SENS_DATA_05   = 0x4E   # R  
EXT_SENS_DATA_06   = 0x4F   # R  
EXT_SENS_DATA_07   = 0x50   # R  
EXT_SENS_DATA_08   = 0x51   # R  
EXT_SENS_DATA_09   = 0x52   # R  
EXT_SENS_DATA_10   = 0x53   # R  
EXT_SENS_DATA_11   = 0x54   # R  
EXT_SENS_DATA_12   = 0x55   # R  
EXT_SENS_DATA_13   = 0x56   # R  
EXT_SENS_DATA_14   = 0x57   # R  
EXT_SENS_DATA_15   = 0x58   # R  
EXT_SENS_DATA_16   = 0x59   # R  
EXT_SENS_DATA_17   = 0x5A   # R  
EXT_SENS_DATA_18   = 0x5B   # R  
EXT_SENS_DATA_19   = 0x5C   # R  
EXT_SENS_DATA_20   = 0x5D   # R  
EXT_SENS_DATA_21   = 0x5E   # R  
EXT_SENS_DATA_22   = 0x5F   # R  
EXT_SENS_DATA_23   = 0x60   # R  
MOT_DETECT_STATUS  = 0x61   # R  
I2C_SLV0_DO        = 0x63   # R/W
I2C_SLV1_DO        = 0x64   # R/W
I2C_SLV2_DO        = 0x65   # R/W
I2C_SLV3_DO        = 0x66   # R/W
I2C_MST_DELAY_CTRL = 0x67   # R/W
SIGNAL_PATH_RESET  = 0x68   # R/W
MOT_DETECT_CTRL    = 0x69   # R/W
USER_CTRL          = 0x6A   # R/W
PWR_MGMT_1         = 0x6B   # R/W
PWR_MGMT_2         = 0x6C   # R/W
FIFO_COUNTH        = 0x72   # R/W
FIFO_COUNTL        = 0x73   # R/W
FIFO_R_W           = 0x74   # R/W
WHO_AM_I           = 0x75   # R


# Defines for the bits, to be able to change 
# between bit number and binary definition.
# By using the bit number, programming the sensor 
# is like programming the AVR microcontroller.
# But instead of using "(1<<X)", or "_BV(X)", 
# the Arduino "int(X)" is used.
D0 = 0
D1 = 1
D2 = 2
D3 = 3
D4 = 4
D5 = 5
D6 = 6
D7 = 7

# AUX_VDDIO Register
AUX_VDDIO = D7  # I2C high: 1=VDD, 0=VLOGIC

# CONFIG Register
# DLPF is Digital Low Pass Filter for both gyro and accelerometers.
# These are the names for the bits.
# Use these only with the int() macro.
DLPF_CFG0     = D0
DLPF_CFG1     = D1
DLPF_CFG2     = D2
EXT_SYNC_SET0 = D3
EXT_SYNC_SET1 = D4
EXT_SYNC_SET2 = D5

# Combined definitions for the EXT_SYNC_SET values
EXT_SYNC_SET_0 = (0)
EXT_SYNC_SET_1 = (int(EXT_SYNC_SET0))
EXT_SYNC_SET_2 = (int(EXT_SYNC_SET1))
EXT_SYNC_SET_3 = (int(EXT_SYNC_SET1)|int(EXT_SYNC_SET0))
EXT_SYNC_SET_4 = (int(EXT_SYNC_SET2))
EXT_SYNC_SET_5 = (int(EXT_SYNC_SET2)|int(EXT_SYNC_SET0))
EXT_SYNC_SET_6 = (int(EXT_SYNC_SET2)|int(EXT_SYNC_SET1))
EXT_SYNC_SET_7 = (int(EXT_SYNC_SET2)|int(EXT_SYNC_SET1)|int(EXT_SYNC_SET0))

# Alternative names for the combined definitions.
EXT_SYNC_DISABLED     = EXT_SYNC_SET_0
EXT_SYNC_TEMP_OUT_L   = EXT_SYNC_SET_1
EXT_SYNC_GYRO_XOUT_L  = EXT_SYNC_SET_2
EXT_SYNC_GYRO_YOUT_L  = EXT_SYNC_SET_3
EXT_SYNC_GYRO_ZOUT_L  = EXT_SYNC_SET_4
EXT_SYNC_ACCEL_XOUT_L = EXT_SYNC_SET_5
EXT_SYNC_ACCEL_YOUT_L = EXT_SYNC_SET_6
EXT_SYNC_ACCEL_ZOUT_L = EXT_SYNC_SET_7

# Combined definitions for the DLPF_CFG values
DLPF_CFG_0 = (0)
DLPF_CFG_1 = (int(DLPF_CFG0))
DLPF_CFG_2 = (int(DLPF_CFG1))
DLPF_CFG_3 = (int(DLPF_CFG1)|int(DLPF_CFG0))
DLPF_CFG_4 = (int(DLPF_CFG2))
DLPF_CFG_5 = (int(DLPF_CFG2)|int(DLPF_CFG0))
DLPF_CFG_6 = (int(DLPF_CFG2)|int(DLPF_CFG1))
DLPF_CFG_7 = (int(DLPF_CFG2)|int(DLPF_CFG1)|int(DLPF_CFG0))

# Alternative names for the combined definitions
# This name uses the bandwidth (Hz) for the accelometer,
# for the gyro the bandwidth is almost the same.
DLPF_260HZ    = DLPF_CFG_0
DLPF_184HZ    = DLPF_CFG_1
DLPF_94HZ     = DLPF_CFG_2
DLPF_44HZ     = DLPF_CFG_3
DLPF_21HZ     = DLPF_CFG_4
DLPF_10HZ     = DLPF_CFG_5
DLPF_5HZ      = DLPF_CFG_6
DLPF_RESERVED = DLPF_CFG_7

# GYRO_CONFIG Register
# The XG_ST, YG_ST, ZG_ST are bits for selftest.
# The FS_SEL sets the range for the gyro.
# These are the names for the bits.
# Use these only with the int() macro.
FS_SEL0 = D3
FS_SEL1 = D4
ZG_ST   = D5
YG_ST   = D6
XG_ST   = D7

# Combined definitions for the FS_SEL values
FS_SEL_0 = (0)
FS_SEL_1 = (int(FS_SEL0))
FS_SEL_2 = (int(FS_SEL1))
FS_SEL_3 = (int(FS_SEL1)|int(FS_SEL0))

# Alternative names for the combined definitions
# The name uses the range in degrees per second.
FS_SEL_250  = FS_SEL_0
FS_SEL_500  = FS_SEL_1
FS_SEL_1000 = FS_SEL_2
FS_SEL_2000 = FS_SEL_3

# ACCEL_CONFIG Register
# The XA_ST, YA_ST, ZA_ST are bits for selftest.
# The AFS_SEL sets the range for the accelerometer.
# These are the names for the bits.
# Use these only with the int() macro.
ACCEL_HPF0 = D0
ACCEL_HPF1 = D1
ACCEL_HPF2 = D2
AFS_SEL0   = D3
AFS_SEL1   = D4
ZA_ST      = D5
YA_ST      = D6
XA_ST      = D7

# Combined definitions for the ACCEL_HPF values
ACCEL_HPF_0 = (0)
ACCEL_HPF_1 = (int(ACCEL_HPF0))
ACCEL_HPF_2 = (int(ACCEL_HPF1))
ACCEL_HPF_3 = (int(ACCEL_HPF1)|int(ACCEL_HPF0))
ACCEL_HPF_4 = (int(ACCEL_HPF2))
ACCEL_HPF_7 = (int(ACCEL_HPF2)|int(ACCEL_HPF1)|int(ACCEL_HPF0))

# Alternative names for the combined definitions
# The name uses the Cut-off frequency.
ACCEL_HPF_RESET  = ACCEL_HPF_0
ACCEL_HPF_5HZ    = ACCEL_HPF_1
ACCEL_HPF_2_5HZ  = ACCEL_HPF_2
ACCEL_HPF_1_25HZ = ACCEL_HPF_3
ACCEL_HPF_0_63HZ = ACCEL_HPF_4
ACCEL_HPF_HOLD   = ACCEL_HPF_7

# Combined definitions for the AFS_SEL values
AFS_SEL_0 = (0)
AFS_SEL_1 = (int(AFS_SEL0))
AFS_SEL_2 = (int(AFS_SEL1))
AFS_SEL_3 = (int(AFS_SEL1)|int(AFS_SEL0))

# Alternative names for the combined definitions
# The name uses the full scale range for the accelerometer.
AFS_SEL_2G  = AFS_SEL_0
AFS_SEL_4G  = AFS_SEL_1
AFS_SEL_8G  = AFS_SEL_2
AFS_SEL_16G = AFS_SEL_3

# FIFO_EN Register
# These are the names for the bits.
# Use these only with the int() macro.
SLV0_FIFO_EN  = D0
SLV1_FIFO_EN  = D1
SLV2_FIFO_EN  = D2
ACCEL_FIFO_EN = D3
ZG_FIFO_EN    = D4
YG_FIFO_EN    = D5
XG_FIFO_EN    = D6
TEMP_FIFO_EN  = D7

# I2C_MST_CTRL Register
# These are the names for the bits.
# Use these only with the int() macro.
I2C_MST_CLK0  = D0
I2C_MST_CLK1  = D1
I2C_MST_CLK2  = D2
I2C_MST_CLK3  = D3
I2C_MST_P_NSR = D4
SLV_3_FIFO_EN = D5
WAIT_FOR_ES   = D6
MULT_MST_EN   = D7

# Combined definitions for the I2C_MST_CLK
I2C_MST_CLK_0  = (0)
I2C_MST_CLK_1  = (int(I2C_MST_CLK0))
I2C_MST_CLK_2  = (int(I2C_MST_CLK1))
I2C_MST_CLK_3  = (int(I2C_MST_CLK1)|int(I2C_MST_CLK0))
I2C_MST_CLK_4  = (int(I2C_MST_CLK2))
I2C_MST_CLK_5  = (int(I2C_MST_CLK2)|int(I2C_MST_CLK0))
I2C_MST_CLK_6  = (int(I2C_MST_CLK2)|int(I2C_MST_CLK1))
I2C_MST_CLK_7  = (int(I2C_MST_CLK2)|int(I2C_MST_CLK1)|int(I2C_MST_CLK0))
I2C_MST_CLK_8  = (int(I2C_MST_CLK3))
I2C_MST_CLK_9  = (int(I2C_MST_CLK3)|int(I2C_MST_CLK0))
I2C_MST_CLK_10 = (int(I2C_MST_CLK3)|int(I2C_MST_CLK1))
I2C_MST_CLK_11 = (int(I2C_MST_CLK3)|int(I2C_MST_CLK1)|int(I2C_MST_CLK0))
I2C_MST_CLK_12 = (int(I2C_MST_CLK3)|int(I2C_MST_CLK2))
I2C_MST_CLK_13 = (int(I2C_MST_CLK3)|int(I2C_MST_CLK2)|int(I2C_MST_CLK0))
I2C_MST_CLK_14 = (int(I2C_MST_CLK3)|int(I2C_MST_CLK2)|int(I2C_MST_CLK1))
I2C_MST_CLK_15 = (int(I2C_MST_CLK3)|int(I2C_MST_CLK2)|int(I2C_MST_CLK1)|int(I2C_MST_CLK0))

# Alternative names for the combined definitions
# The names uses I2C Master Clock Speed in kHz.
I2C_MST_CLK_348KHZ = I2C_MST_CLK_0
I2C_MST_CLK_333KHZ = I2C_MST_CLK_1
I2C_MST_CLK_320KHZ = I2C_MST_CLK_2
I2C_MST_CLK_308KHZ = I2C_MST_CLK_3
I2C_MST_CLK_296KHZ = I2C_MST_CLK_4
I2C_MST_CLK_286KHZ = I2C_MST_CLK_5
I2C_MST_CLK_276KHZ = I2C_MST_CLK_6
I2C_MST_CLK_267KHZ = I2C_MST_CLK_7
I2C_MST_CLK_258KHZ = I2C_MST_CLK_8
I2C_MST_CLK_500KHZ = I2C_MST_CLK_9
I2C_MST_CLK_471KHZ = I2C_MST_CLK_10
I2C_MST_CLK_444KHZ = I2C_MST_CLK_11
I2C_MST_CLK_421KHZ = I2C_MST_CLK_12
I2C_MST_CLK_400KHZ = I2C_MST_CLK_13
I2C_MST_CLK_381KHZ = I2C_MST_CLK_14
I2C_MST_CLK_364KHZ = I2C_MST_CLK_15

# I2C_SLV0_ADDR Register
# These are the names for the bits.
# Use these only with the int() macro.
I2C_SLV0_RW = D7

# I2C_SLV0_CTRL Register
# These are the names for the bits.
# Use these only with the int() macro.
I2C_SLV0_LEN0    = D0
I2C_SLV0_LEN1    = D1
I2C_SLV0_LEN2    = D2
I2C_SLV0_LEN3    = D3
I2C_SLV0_GRP     = D4
I2C_SLV0_REG_DIS = D5
I2C_SLV0_BYTE_SW = D6
I2C_SLV0_EN      = D7

# A mask for the length
I2C_SLV0_LEN_MASK = 0x0F

# I2C_SLV1_ADDR Register
# These are the names for the bits.
# Use these only with the int() macro.
I2C_SLV1_RW = D7

# I2C_SLV1_CTRL Register
# These are the names for the bits.
# Use these only with the int() macro.
I2C_SLV1_LEN0    = D0
I2C_SLV1_LEN1    = D1
I2C_SLV1_LEN2    = D2
I2C_SLV1_LEN3    = D3
I2C_SLV1_GRP     = D4
I2C_SLV1_REG_DIS = D5
I2C_SLV1_BYTE_SW = D6
I2C_SLV1_EN      = D7

# A mask for the length
I2C_SLV1_LEN_MASK = 0x0F

# I2C_SLV2_ADDR Register
# These are the names for the bits.
# Use these only with the int() macro.
I2C_SLV2_RW = D7

# I2C_SLV2_CTRL Register
# These are the names for the bits.
# Use these only with the int() macro.
I2C_SLV2_LEN0    = D0
I2C_SLV2_LEN1    = D1
I2C_SLV2_LEN2    = D2
I2C_SLV2_LEN3    = D3
I2C_SLV2_GRP     = D4
I2C_SLV2_REG_DIS = D5
I2C_SLV2_BYTE_SW = D6
I2C_SLV2_EN      = D7

# A mask for the length
I2C_SLV2_LEN_MASK = 0x0F

# I2C_SLV3_ADDR Register
# These are the names for the bits.
# Use these only with the int() macro.
I2C_SLV3_RW = D7

# I2C_SLV3_CTRL Register
# These are the names for the bits.
# Use these only with the int() macro.
I2C_SLV3_LEN0    = D0
I2C_SLV3_LEN1    = D1
I2C_SLV3_LEN2    = D2
I2C_SLV3_LEN3    = D3
I2C_SLV3_GRP     = D4
I2C_SLV3_REG_DIS = D5
I2C_SLV3_BYTE_SW = D6
I2C_SLV3_EN      = D7

# A mask for the length
I2C_SLV3_LEN_MASK = 0x0F

# I2C_SLV4_ADDR Register
# These are the names for the bits.
# Use these only with the int() macro.
I2C_SLV4_RW = D7

# I2C_SLV4_CTRL Register
# These are the names for the bits.
# Use these only with the int() macro.
I2C_MST_DLY0     = D0
I2C_MST_DLY1     = D1
I2C_MST_DLY2     = D2
I2C_MST_DLY3     = D3
I2C_MST_DLY4     = D4
I2C_SLV4_REG_DIS = D5
I2C_SLV4_INT_EN  = D6
I2C_SLV4_EN      = D7

# A mask for the delay
I2C_MST_DLY_MASK = 0x1F

# I2C_MST_STATUS Register
# These are the names for the bits.
# Use these only with the int() macro.
I2C_SLV0_NACK = D0
I2C_SLV1_NACK = D1
I2C_SLV2_NACK = D2
I2C_SLV3_NACK = D3
I2C_SLV4_NACK = D4
I2C_LOST_ARB  = D5
I2C_SLV4_DONE = D6
PASS_THROUGH  = D7

# I2C_PIN_CFG Register
# These are the names for the bits.
# Use these only with the int() macro.
CLKOUT_EN       = D0
I2C_BYPASS_EN   = D1
FSYNC_INT_EN    = D2
FSYNC_INT_LEVEL = D3
INT_RD_CLEAR    = D4
LATCH_INT_EN    = D5
INT_OPEN        = D6
INT_LEVEL       = D7

# INT_ENABLE Register
# These are the names for the bits.
# Use these only with the int() macro.
DATA_RDY_EN    = D0
I2C_MST_INT_EN = D3
FIFO_OFLOW_EN  = D4
ZMOT_EN        = D5
MOT_EN         = D6
FF_EN          = D7

# INT_STATUS Register
# These are the names for the bits.
# Use these only with the int() macro.
DATA_RDY_INT   = D0
I2C_MST_INT    = D3
FIFO_OFLOW_INT = D4
ZMOT_INT       = D5
MOT_INT        = D6
FF_INT         = D7

# MOT_DETECT_STATUS Register
# These are the names for the bits.
# Use these only with the int() macro.
MOT_ZRMOT = D0
MOT_ZPOS  = D2
MOT_ZNEG  = D3
MOT_YPOS  = D4
MOT_YNEG  = D5
MOT_XPOS  = D6
MOT_XNEG  = D7

# IC2_MST_DELAY_CTRL Register
# These are the names for the bits.
# Use these only with the int() macro.
I2C_SLV0_DLY_EN = D0
I2C_SLV1_DLY_EN = D1
I2C_SLV2_DLY_EN = D2
I2C_SLV3_DLY_EN = D3
I2C_SLV4_DLY_EN = D4
DELAY_ES_SHADOW = D7

# SIGNAL_PATH_RESET Register
# These are the names for the bits.
# Use these only with the int() macro.
TEMP_RESET  = D0
ACCEL_RESET = D1
GYRO_RESET  = D2

# MOT_DETECT_CTRL Register
# These are the names for the bits.
# Use these only with the int() macro.
MOT_COUNT0      = D0
MOT_COUNT1      = D1
FF_COUNT0       = D2
FF_COUNT1       = D3
ACCEL_ON_DELAY0 = D4
ACCEL_ON_DELAY1 = D5

# Combined definitions for the MOT_COUNT
MOT_COUNT_0 = (0)
MOT_COUNT_1 = (int(MOT_COUNT0))
MOT_COUNT_2 = (int(MOT_COUNT1))
MOT_COUNT_3 = (int(MOT_COUNT1)|int(MOT_COUNT0))

# Alternative names for the combined definitions
MOT_COUNT_RESET = MOT_COUNT_0

# Combined definitions for the FF_COUNT
FF_COUNT_0 = (0)
FF_COUNT_1 = (int(FF_COUNT0))
FF_COUNT_2 = (int(FF_COUNT1))
FF_COUNT_3 = (int(FF_COUNT1)|int(FF_COUNT0))

# Alternative names for the combined definitions
FF_COUNT_RESET = FF_COUNT_0

# Combined definitions for the ACCEL_ON_DELAY
ACCEL_ON_DELAY_0 = (0)
ACCEL_ON_DELAY_1 = (int(ACCEL_ON_DELAY0))
ACCEL_ON_DELAY_2 = (int(ACCEL_ON_DELAY1))
ACCEL_ON_DELAY_3 = (int(ACCEL_ON_DELAY1)|int(ACCEL_ON_DELAY0))

# Alternative names for the ACCEL_ON_DELAY
ACCEL_ON_DELAY_0MS = ACCEL_ON_DELAY_0
ACCEL_ON_DELAY_1MS = ACCEL_ON_DELAY_1
ACCEL_ON_DELAY_2MS = ACCEL_ON_DELAY_2
ACCEL_ON_DELAY_3MS = ACCEL_ON_DELAY_3

# USER_CTRL Register
# These are the names for the bits.
# Use these only with the int() macro.
SIG_COND_RESET = D0
I2C_MST_RESET  = D1
FIFO_RESET     = D2
I2C_IF_DIS     = D4   # must be 0 for MPU-6050
I2C_MST_EN     = D5
FIFO_EN        = D6

# PWR_MGMT_1 Register
# These are the names for the bits.
# Use these only with the int() macro.
CLKSEL0      = D0
CLKSEL1      = D1
CLKSEL2      = D2
TEMP_DIS     = D3    # 1: disable temperature sensor
CYCLE        = D5    # 1: sample and sleep
SLEEP        = D6    # 1: sleep mode
DEVICE_RESET = D7    # 1: reset to default values

# Combined definitions for the CLKSEL
CLKSEL_0 = (0)
CLKSEL_1 = (int(CLKSEL0))
CLKSEL_2 = (int(CLKSEL1))
CLKSEL_3 = (int(CLKSEL1)|int(CLKSEL0))
CLKSEL_4 = (int(CLKSEL2))
CLKSEL_5 = (int(CLKSEL2)|int(CLKSEL0))
CLKSEL_6 = (int(CLKSEL2)|int(CLKSEL1))
CLKSEL_7 = (int(CLKSEL2)|int(CLKSEL1)|int(CLKSEL0))

# Alternative names for the combined definitions
CLKSEL_INTERNAL    = CLKSEL_0
CLKSEL_X           = CLKSEL_1
CLKSEL_Y           = CLKSEL_2
CLKSEL_Z           = CLKSEL_3
CLKSEL_EXT_32KHZ   = CLKSEL_4
CLKSEL_EXT_19_2MHZ = CLKSEL_5
CLKSEL_RESERVED    = CLKSEL_6
CLKSEL_STOP        = CLKSEL_7

# PWR_MGMT_2 Register
# These are the names for the bits.
# Use these only with the int() macro.
STBY_ZG       = D0
STBY_YG       = D1
STBY_XG       = D2
STBY_ZA       = D3
STBY_YA       = D4
STBY_XA       = D5
LP_WAKE_CTRL0 = D6
LP_WAKE_CTRL1 = D7

# Combined definitions for the LP_WAKE_CTRL
LP_WAKE_CTRL_0 = (0)
LP_WAKE_CTRL_1 = (int(LP_WAKE_CTRL0))
LP_WAKE_CTRL_2 = (int(LP_WAKE_CTRL1))
LP_WAKE_CTRL_3 = (int(LP_WAKE_CTRL1)|int(LP_WAKE_CTRL0))

# Alternative names for the combined definitions
# The names uses the Wake-up Frequency.
LP_WAKE_1_25HZ = LP_WAKE_CTRL_0
LP_WAKE_2_5HZ  = LP_WAKE_CTRL_1
LP_WAKE_5HZ    = LP_WAKE_CTRL_2
LP_WAKE_10HZ   = LP_WAKE_CTRL_3


# Default I2C address for the MPU-6050 is = 0x68.
# But only if the AD0 pin is low.
# Some sensor boards have AD0 high, and the
# I2C address thus becomes = 0x69.
I2C_ADDRESS = 0x68