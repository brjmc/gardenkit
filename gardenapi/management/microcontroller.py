import serial
import io
import time
import chardet
COM_PORT = '/dev/ttyUSB0'
BAUDRATE = 9600
MAX_BYTES = 1
SAMPLE_SIZE = 100

class MicroController:
  def __init__(self):
    self.ser = serial.Serial(COM_PORT, BAUDRATE)
    self.ser.timeout = 1

  def is_open(self):
    return self.ser.is_open

  def execute_command(self, cmd):
    result = 0

    while result < 1:
      try:
        self.ser.write(cmd.encode())
        result = (float(self.ser.readline()))
      except Exception as e:
        print('error: {}\n'.format(e))

      time.sleep(.1)

    return result


  def sensorRead(self, cmd):
    i = 0
    sum = 0
    encoded_command = cmd.encode()
    while i < SAMPLE_SIZE:
      self.ser.write(encoded_command)
      try:
        raw = self.ser.readline()
        result = (float(raw))

        if result > 0:
          sum += result
          i += 1
      except Exception as e:
        print('error: {}\n'.format(e))

      time.sleep(.1)

    return sum/SAMPLE_SIZE
