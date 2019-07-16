import serial
import io
import time

COM_PORT = '/dev/cu.usbserial-1420'
BAUDRATE = 9600
MAX_BYTES = 1
SAMPLE_SIZE = 10

class MicroController:
  def __init__(self):
    self.ser = serial.Serial(COM_PORT, BAUDRATE)
    self.ser.timeout = 1

  def is_open(self):
    return self.ser.is_open

  def sensorRead(self, cmd):
    i = 0
    sum = 0
    while i < SAMPLE_SIZE:
      self.ser.write(cmd.encode())
      try:
        result = (float(self.ser.readline()))
        if result > 0:
          sum += result
          i += 1
      except Exception as e:
        print('error: {}\n'.format(e))

      time.sleep(.1)

    return sum/SAMPLE_SIZE


# m = 1000
# i = 0
# sum = 0
# ser = serial.Serial(COM_PORT, 9600) # Establish the connection on a specific port
# ser.timeout = 1
# errors = 0
# counter = 32 # Below 32 everything in ASCII is gibberish
# while i < m:

#   ser.write('1'.encode())


#   try:
#     result = ser.readline()
#     reading = (float(result))
#     if(reading > 1):
#       sum += reading
#       i += 1
#       # print('avg: {}'.format(sum/(1000-i)))
#       print('{}'.format(reading))
#     # else:
#       # print('DAMN: {}'.format(reading))
#   except Exception as e:
#     # print('crap: {}\n'.format(e))
#     errors += 1
#     # print('error number: {}'.format(errors))

#   time.sleep(.1)

# print('avg: {}'.format(sum/(m)))
# print('error number: {}'.format(errors))



