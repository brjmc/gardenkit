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
