import serial
#https://drive.google.com/file/d/1xrfK9bAEncgFQYjvT_c6vwSEH0ZhzaUZ/view
ser = serial.Serial(
    port='COM8',
    baudrate=19200)

def parseTime(s):
    # print(s)
    rtn = []
    for i in range(0,len(s)-12,4):
        rtn.append(int(s[i:i+4],16))
    return rtn
def parseAcceleration(s):
    pass
def parseAngularV(s):
    pass
def parseAngle(s):
    rtn = []
    for i in range(0,24,8):
        rtn.append(((int(s[i+4:i+8],16)<<8)|int(s[i:i+4],16))/32768*180)
    return rtn
def parseMagneticF(s):
    pass

types = {"0x50":["Time",parseTime],"0x51":["Acceleration",parseAcceleration],"0x52":["Angular velocity",parseAngularV],"0x53":["Angle",parseAngle],"0x54":["Magnetic field",parseMagneticF]}

if __name__ == "__main__":
    sentence = ""
    while True:
        inp = hex(int.from_bytes(ser.read(),byteorder='little'))
        if len(inp) == 3:
            inp = inp[0:2] + "0" + inp[-1]
        if str(inp) == "0x55":
            if sentence != "":
                parse = types.get(sentence[0:4])
                if parse and len(sentence[4:]) == 36:
                    parse = parse[1](sentence[4:])
                print(parse)
            sentence = ""
        else:
            sentence+= inp