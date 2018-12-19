import RPi.GPIO as GPIO

LED_names={ 
  "collect_data" : 2,
  "autonomous" : 4,
  "shutdown_RPi" : 27,
}


switch_names={ 
  "collect_data" : 6,
  "autonomous" : 11,
  "shutdown_RPi" : 9,
}

FRAME_RATE = 40
DATA_DIR = "/home/pi/foocars/cars/greenmachine/data/"
COLLECT_DIR = DATA_DIR + "collected"
WEIGHTS_DIR = DATA_DIR + "weights/"
WEIGHTS_FILE = WEIGHTS_DIR + "weights-default.h5"
STEERSTATS_FILE = WEIGHTS_DIR + "steerstats.npz"
THR_MAX = 1604

SWITCH_ON=GPIO.LOW
SWITCH_OFF=GPIO.HIGH

LED_ON=GPIO.HIGH
LED_OFF=GPIO.LOW

#function returns dynamically created object of type 'Enum' with fields enums:
def enum(**enums):
  return type('Enum', (), enums) 

commandEnum=enum(
  NOT_ACTUAL_COMMAND=0,
  RC_SIGNAL_WAS_LOST=1, 
  RC_SIGNALED_STOP_AUTONOMOUS=2, 
  STEERING_VALUE_OUT_OF_RANGE=3, 
  THROTTLE_VALUE_OUT_OF_RANGE=4, 
  RUN_AUTONOMOUSLY=5, 
  STOP_AUTONOMOUS=6, 
  STOPPED_AUTO_COMMAND_RECIEVED=7, 
  NO_COMMAND_AVAILABLE=8, 
  GOOD_PI_COMMAND_RECEIVED=9, 
  TOO_MANY_VALUES_IN_COMMAND=10, 
  GOOD_RC_SIGNALS_RECIEVED=11)

from dropout_model import model
print("imported model")

def filter_out(nn_output, steerstats):
    str_command=nn_output[0][0]*steerstats[1]+steerstats[0]
    if str_command>2000:
        str_command=2000
    elif str_command<1000:
        str_command=1000

    thr_command=THR_MAX
    return (str_command, thr_command)



