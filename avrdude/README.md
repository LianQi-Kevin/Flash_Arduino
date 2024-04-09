### Use Jetson Nano flash Arduino

#### 1. 设置`Arduino IDE`首选项, 确保勾选`compilation`和`upload`

![](https://www.monocilindro.com/wp-content/uploads/2017/03/Arduino_flashing_Raspberry_01.png)

#### 2. 使用PC上的`Arduino IDE`编译项目

检查编译输出的日志, 寻找`.hex`文件的位置
> eg: C:\Users\Kishi\AppData\Local\Temp\arduino_build_521698/efi_davide_nano.ino.hex

![](https://www.monocilindro.com/wp-content/uploads/2017/03/Arduino_flashing_Raspberry_02-1024x556.png)

#### 3. 下载`avrdude.conf`文件

[avrdude.conf](avrdude.conf)

#### 4. 将`avrdude.conf`和`.hex`文件上传到`Jetson Nano`

#### 5. 将`Arduino`通过USB线连接到`Jetson Nano`

在`/dev/`下检查`Arduino`所属的USB串行设备名称，一般为`ttyACM0`

#### 6. 安装`avrdude`

```
sudo apt-get install avrdude
```

#### 7. 创建一个目录，并将`avrdude.conf`和`.hex`文件上传到其中

#### 8. 使用python脚本刷写`Arduino`

> [或者也可以直接使用avrdude刷写Arduino](#直接使用avrdude刷写Arduino)

1. 安装`pyserial`库（连接测试）

    ```
    pip3 install pyserial
    ```

2. 刷写 `Arduino`

    ```
    $ python3 flash_arduino_with_avrdude.py -h
    usage: flash_arduino_with_avrdude.py [-h] [--confPath CONFPATH] [--uP UP]
                                         [--boardName BOARDNAME] [--portNo PORTNO]
                                         [--baudRate BAUDRATE] [--hexPath HEXPATH]
    
    Flashing Arduino with avrdude on Jetson Nano.
    
    optional arguments:
      -h, --help            show this help message and exit
      --confPath CONFPATH   avrdude.conf path. default:avrdude.conf
      --uP UP               Microprocessor name. such as: atmega328p
      --boardName BOARDNAME Arduino board name. Uno/Leonardo
      --portNo PORTNO       Serial device name. such as "/dev/ttyACM0
      --baudRate BAUDRATE   Port used to communicate with Arduino. default: 115200
      --hexPath HEXPATH     path to hex file.
    ```

   > 至少需要给定`boardName`, `hexPath`两个参数 \
   > `--boardName`暂时只接受`Uno`或`Leonardo`，其余版型请指定`--uP`参数 \
   > `--portNo` 在未指定的情况下 会自动寻找`/dev/`下包含`ttyACM`或`ttyUSB`的项，如果多于一个将会列出以供选择 \
   > `--confPath`默认使用当前目录下的`avrdude.conf`文件，如不存在则需手动输入 \
   > `--baudRate`默认使用115200, 如刷写不成功请测试其他波特率
   > ```
    > python3 flash_arduino_with_avrdude.py --confPath avrdude.conf --uP atmega328p --portNo /dev/ACM0 --baudRate 115200 --hexPath All_color_loop_LED.ino.hex
    > python3 flash_arduino_with_avrdude.py --confPath avrdude.conf --boardName Uno --portNo /dev/ACM0 --baudRate 115200 --hexPath All_color_loop_LED.ino.hex
    > ```
   如果正常写入, 您将看到如下内容

   ![](https://www.monocilindro.com/wp-content/uploads/2017/03/Arduino_flashing_Raspberry_07-1024x556.png)
   ![](https://www.monocilindro.com/wp-content/uploads/2017/03/Arduino_flashing_Raspberry_08-1024x555.png)
    
   ---

#### 直接使用avrdude刷写Arduino

```
avrdude -C avrdude.conf -v -p atmega328p -c arduino -P /dev/ttyACM0 -b 115200 -D -U flash:w:efi_davide_nano.ino.hex:i
```

> `-C`参数指定了`avrdude.conf`的位置 \
> `-p`参数指定了Arduino所属的微处理器名称，即`atmega328p`,`atmega32u4`等 \
> `-P`参数指定了串口设备的名称 即`/dev/ttyACM0`\
> `-U`参数制定了`.hex`文件的路径 范式为`flash:w:<hex_filename>:i`

---

##### 参考资料

* https://www.monocilindro.com/2017/03/20/flashing-arduino-using-raspberry-pi-shell/
* https://forum.arduino.cc/t/arduino-1-8-6-error-with-programming-with-usbasp-solution-option/542975

> 不采用原链接查找`avrdude.conf`的原因是当前`Arduino IDE`默认使用的`avrdude.conf`过新，无法正常兼容\
> 可通过调整IDE的`Arduino AVR Boards by Arduino`库的版本到`1.6.21`并使用其`avrdude.conf`文件