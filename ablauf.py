import serial
import time

port = "COM3"
ser = serial.Serial(port, baudrate = 57600)



def readLine(port):
    read = port.readline()
    return read
""" 
print("starting")
while True:
    time.sleep(1)
    send1 = "Servo SetTrigger 90\n"
    send2 = "ServoGetTrigger\n"
    a = send1.encode('utf-8')
    b = send2.encode('utf-8')

    print("sending")
    ser.write(a)
    ser.write(b)

    rcv = readLine(ser)
    print("recieved: ", rcv)
"""



def main():
    print("Main Program")

    command = "Servo SetCam 80\n"
    sendcommand = command.encode('utf-8')
    ser.write(sendcommand)
    #just testings
    command = "Servo GetCam\n"
    sendcommand = command.encode('utf-8')
    ser.write(sendcommand)
    rcv = readLine(ser)
    print("Cam Position: ", rcv)

    # enable usensors
    #"""
    command = "USens Init\n"
    sendcommand = command.encode('utf-8')
    ser.write(sendcommand)

    command = "USens SetUSEnableFront 1\n"
    sendcommand = command.encode('utf-8')
    ser.write(sendcommand)

    command = "USens SetUSEnableBottom 1\n"
    sendcommand = command.encode('utf-8')
    ser.write(sendcommand)
    #"""
    time.sleep(3)
    pictogramfound = 1
    while pictogramfound == 0:
        pictogramfound = objectdetectionbottom()
    #Piktogramm wurde gefunden

    #Treppe suchen


    spring()
    print("Sprung beendet")

    #time.sleep(2)
    setcamtop()
    print("setcamtop beendet")

    searchpictogramtop()
    print("Programm beendet")



def objectdetectionbottom():
    #object Detection Code
    pictogramfound = 0

    return pictogramfound


def spring():
    command = "Servo SetTrigger 90\n"
    sendcommand = command.encode('utf-8')
    ser.write(sendcommand)

    # just testings
    command = "Servo GetTrigger\n"
    sendcommand = command.encode('utf-8')
    ser.write(sendcommand)
    rcv = readLine(ser)
    print("Trigger Position: ", rcv)

    return

def setcamtop():
    print("start setcamtop")
    command = "USens GetDistanceBottom\n"
    sendcommand = command.encode('utf-8')
    ser.write(sendcommand)
    rcv = readLine(ser)
    time.sleep(2)
    rcv = str(rcv, 'utf-8')
    rcv = int(rcv)
    print("distance Sensor Bottom: ", rcv)
    if rcv < 100:
        command = "Servo SetCam 80\n"
        sendcommand = command.encode('utf-8')
        ser.write(sendcommand)
        print("cam nach oben setzen")
    else:
        command = "Servo SetCam 70\n"
        sendcommand = command.encode('utf-8')
        ser.write(sendcommand)
        print("cam nach unten setzen")

    return

def objectdetectiontop():
    #object Detection Code


    return 0

def searchpictogramtop():

    pictogramfound = objectdetectiontop()
    pictogramfound = 0
    while pictogramfound < 2:
        command = "Mot Angle 30, 10\n"
        sendcommand = command.encode('utf-8')
        ser.write(sendcommand)
        time.sleep(1)
        pictogramfound = pictogramfound + 1
        print("motor hat sich gedreht")

        #pictogramfound = objectdetectiontop()



    distancefront = getdistancefront()


    while distancefront > 60:
        command = "Mot Dis 20,10\n"
        sendcommand = command.encode('utf-8')
        ser.write(sendcommand)
        time.sleep(2)
        print("fährt vorwärts")
        distancefront = getdistancefront()


    command = "led set 1\n"
    sendcommand = command.encode('utf-8')
    ser.write(sendcommand)
    print("led läuchtet hell yea >.<")

    return

def getdistancefront():
    command = "USens GetDistanceFront\n"
    sendcommand = command.encode('utf-8')
    ser.write(sendcommand)
    rcv = readLine(ser)
    time.sleep(2)
    rcv = str(rcv, 'utf-8')
    rcv = int(rcv)
    return rcv

main()