import argparse
import os


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
    else:
        portNo = args.portNo

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
        hex_path = args.confPath

    # 拼接命令
    basic_common = "avrdude -C avrdude.conf -v -p atmega328p -c arduino -P /dev/ttyACM0 -b 115200 -D -U flash:w:efi_davide_nano.ino.hex:i"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Flashing Arduino with avrdude on Jetson Nano.')
    parser.add_argument('--confPath', type=str, default="avrdude.conf", help='avrdude.conf path. default:avrdude.conf')
    parser.add_argument('--uP', type=str, default="atmega328p", help='Microprocessor name. default:atmega328p')
    parser.add_argument('--boardName', type=str, default=None, help='Arduino board name. UNO/Leonardo')
    parser.add_argument('--portNo', type=str, default=None, help='Serial device name.')
    parser.add_argument('--baudRate', type=int, default=115200,
                        help='Port used to communicate with Arduino. default: 115200')
    parser.add_argument('--hexPath', type=str, default=None, help='path to hex file.')
    args = parser.parse_args()
    main(args)
