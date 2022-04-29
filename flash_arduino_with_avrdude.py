import argparse
import os
from distutils.util import strtobool

import serial


def main(args):
    # 检查avrdude是否存在
    avrdude_path = os.popen("which avrdude").read()
    if avrdude_path == "":
        print("avrdude not found, Please use 'sudo apt-get install avrdude' to install it")
        exit()
    else:
        print("avrdude path: {}".format(avrdude_path))

    # 如果未指定串口设备名称，则检查/dev/下的ttyACM*和ttyUSB*
    if args.portNo is None:
        deviceList = [' '.join([i.strip() for i in price.strip().split('\t')]) for price in
                      os.popen("ls /dev/ | grep -E 'ttyACM|ttyUSB'").readlines()]
        if len(deviceList) != 1:
            portNo = input(
                "The Serial port is None, Found {} in /dev/. \nPlease input your Serial port: ".format(deviceList))
            while True:
                if portNo not in deviceList:
                    portNo = input("{} not in {}. Please check your input: ".format(portNo, deviceList))
                else:
                    break
        else:
            portNo = deviceList[0]
            print("Serial device name not entered, use {}".format(portNo))
    else:
        portNo = args.portNo

    # 连接测试
    baud_rate = args.baudRate
    try:
        serial.Serial(portNo, baud_rate)
        print("Successful link Arduino, port: {}, baud rate: {}".format(portNo, baud_rate))
    except:
        while True:
            try:
                portNo = input("Can't link Arduino, please re-input port name: ")
                baud_rate = int(input("Can't link Arduino, please re-input baud rate: "))
            except:
                pass
            try:
                serial.Serial(portNo, baud_rate)
                print("Successful link Arduino, port: {}, baud rate: {}".format(portNo, baud_rate))
                break
            except:
                pass

    # 检查”avrdude.conf文件路径“
    if not os.path.isfile(args.confPath):
        conf_path = input("Please input the path to avrdude.conf: ")
        while True:
            if not os.path.isfile(conf_path):
                conf_path = input("{} does not exist, please re-input: ".format(conf_path))
            else:
                break
    else:
        conf_path = args.confPath

    # 检查”.hex“文件位置
    if not os.path.isfile(args.hexPath):
        hex_path = input("Please input the path to avrdude.conf: ")
        while True:
            if not os.path.isfile(hex_path):
                hex_path = input("{} does not exist, please re-input: ".format(conf_path))
            else:
                break
    else:
        hex_path = args.hexPath

    # 检查微处理器名称是否合法
    if args.boardName is not None:
        if args.boardName == "Uno":
            uP_name = "atmega328p"
        elif args.boardName == "Leonardo":
            uP_name = "atmega32u4"
        else:
            if args.uP is not None:
                uP_name = args.uP
            else:
                uP_name = input("Please input your board's microprocessor name: ")

    if strtobool(input(
            "Please check the parameters: \n\tconf path: {} \n\tuP name: {} \n\tserial port: {}\n\tbaud rate: {}\n\t.hex file path: {}\ninput 'yes' to confirm this parameters: ".format(
                conf_path, uP_name, portNo, baud_rate, hex_path))) == 1:
        # 拼接命令
        common = "avrdude -C {} -v -p {} -c arduino -P {} -b {} -D -U flash:w:{}:i".format(conf_path, uP_name, portNo,
                                                                                           baud_rate, hex_path)
        os.system(common)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Flashing Arduino with avrdude on Jetson Nano.')
    parser.add_argument('--confPath', type=str, default="avrdude.conf", help='avrdude.conf path. default:avrdude.conf')
    parser.add_argument('--uP', type=str, default=None, help='Microprocessor name. such as: atmega328p')
    parser.add_argument('--boardName', type=str, default=None, help='Arduino board name. Uno/Leonardo')
    parser.add_argument('--portNo', type=str, default=None, help='Serial device name. such as "/dev/ttyACM0')
    parser.add_argument('--baudRate', type=int, default=115200,
                        help='Port used to communicate with Arduino. default: 115200')
    parser.add_argument('--hexPath', type=str, default=None, help='path to hex file.')
    args = parser.parse_args()
    main(args)
