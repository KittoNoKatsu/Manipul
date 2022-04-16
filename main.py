import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal as Signal
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QListWidget

app = QtWidgets.QApplication([])
ui = uic.loadUi("manipulator.ui")

serial = QSerialPort()
serial.setBaudRate(115200)
portList = []
ports = QSerialPortInfo().availablePorts()
for port in ports:
    portList.append(port.portName())
ui.comL.addItems(portList)
#print(portList)

#class OutputLogger(QObject):
   # emit_write = Signal(str, int)

  #  class Severity:
   #     DEBUG = 0
  #      ERROR = 1

 #   def __init__(self, io_stream, severity):
  #      super().__init__()

     #   self.io_stream = io_stream
    #    self.severity = severity

  #  def write(self, text):
  #      self.io_stream.write(text)
   #     self.emit_write.emit(text, self.severity)

   # def flush(self):
    #    self.io_stream.flush()


#OUTPUT_LOGGER_STDOUT = OutputLogger(sys.stdout, OutputLogger.Severity.DEBUG)
#OUTPUT_LOGGER_STDERR = OutputLogger(sys.stderr, OutputLogger.Severity.ERROR)

#sys.stdout = OUTPUT_LOGGER_STDOUT
#sys.stderr = OUTPUT_LOGGER_STDERR

#class MainWindow(QMainWindow):
   # def __init__(self):
    #    super().__init__()

   #     self.text_edit = QTextEdit()

   #     OUTPUT_LOGGER_STDOUT.emit_write.connect(self.append_log)
    #    OUTPUT_LOGGER_STDERR.emit_write.connect(self.append_log)

   #     Listwi = QListWidget()
   #     self.(Listwi)

    #    self.setCentralWidget(self.text_edit)

  #  def append_log(self, text, severity):
   #     text = repr(text)

   #     if severity == OutputLogger.Severity.ERROR:
    #        text = '<b>{}</b>'.format(text)

    #    self.text_edit.append(text)



def serialSend(data):
    txs = ""
    for val in data:
        txs += str(val)
        txs += ','
    txs = txs[:-1]
    txs += ';'
    #print(txs)
    #serial.write("100a")

def onRead():
    rx = serial.readLine()
    rxs = str(rx, 'utf-8').strip()
    #print(rxs)

def onOpen():
    serial.setPortName(ui.comL.currentText())
    serial.open(QIODevice.ReadWrite)
    #serial.write('90a'.encode())
    #print("rrr")


def onClose():
    serial.close()
    #serial.write('b'.encode())

def OpFile():
    #post = serial.readAll()
    #for i in post
    #print("post=", post)
    #with open("alfa_trajector.txt", "r") as file1:
        # итерация по строкам
        #for line in file1:
           # data = file1.readline()
          #  serial.write(data.encode())
          #  print(line.strip())
        #print(data.strip())
    with open("alfa_trajector.txt") as file:
        data = file.read()
        serial.write(data.encode())
        print(data)

def servoControlA(val):
    txs = ""
    txs += str(val + 5)
    txs += 'a'
    serial.write(txs.encode())
    print(txs)
    v = serial.readAll()
    print("v=", v)
    #rv = []
    #for i in v.split("\n")[-2].split(" "):
     #   ii = i.split("=")
        #print("full line =", i.strip(), "only number = ", int(ii[1]))
      #  rv.append(ii[1])
       # print("rv=", rv)

def servoControlB(val):
    txs = ""
    txs += str(val + 5)
    txs += 'b'
    serial.write(txs.encode())
    print(txs)
    v = serial.readAll()
    print("v=", v)

def servoControlC(val):
    txs = ""
    txs += str(val + 5)
    txs += 'c'
    serial.write(txs.encode())
    print(txs)
    v = serial.readAll()
    print("v=", v)

def servoControlD(val):
    txs = ""
    txs += str(val + 5)
    txs += 'd'
    serial.write(txs.encode())
    print(txs)
    v = serial.readAll()
    print("v=", v)

def servoControlE(val):
    txs = ""
    txs += str(val + 5)
    txs += 'e'
    serial.write(txs.encode())
    print(txs)
    v = serial.readAll()
    print("v=", v)

def servoControlF(val):
    txs = ""
    txs += str(val + 5)
    txs += 'f'
    serial.write(txs.encode())
    print(txs)
    v = serial.readAll()
    print("v=", v)

#def listing():
   # print("as")
#serial.readyRead.connect(onRead)
ui.openB.clicked.connect(onOpen)
ui.openFile.clicked.connect(OpFile)
ui.closeB.clicked.connect(onClose)
#serial.write('50a')
ui.servoA.valueChanged.connect(servoControlA)
ui.servoB.valueChanged.connect(servoControlB)
ui.servoC.valueChanged.connect(servoControlC)
ui.servoD.valueChanged.connect(servoControlD)
ui.servoE.valueChanged.connect(servoControlE)
ui.servoF.valueChanged.connect(servoControlF)
#ui.listA.connect(listing)
ui.show()
#print("Go")
app.exec()