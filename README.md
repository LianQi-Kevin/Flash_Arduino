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
#### 8. 使用命令行刷写`Arduino`
```
avrdude -C avrdude.conf -v -p atmega328p -c arduino -P /dev/ttyACM0 -b 115200 -D -U flash:w:efi_davide_nano.ino.hex:i
```
> `-C`参数指定了`avrdude.conf`的位置 \
> `-p`参数指定了Arduino所属的微处理器名称，即`atmega328p`,`atmega32u4`等 \
> `-P`参数指定了串口设备的名称 即`/dev/ttyACM0`\
> `-U`参数制定了`.hex`文件的路径 范式为`flash:w:<hex_filename>:i`

如果正常写入, 您将看到如下内容
![](https://www.monocilindro.com/wp-content/uploads/2017/03/Arduino_flashing_Raspberry_07-1024x556.png)
![](https://www.monocilindro.com/wp-content/uploads/2017/03/Arduino_flashing_Raspberry_08-1024x555.png)

---
##### 参考资料
* https://www.monocilindro.com/2017/03/20/flashing-arduino-using-raspberry-pi-shell/
* https://forum.arduino.cc/t/arduino-1-8-6-error-with-programming-with-usbasp-solution-option/542975

> 不采用原链接查找`avrdude.conf`的原因是当前`Arduino IDE`默认使用的`avrdude.conf`过新，无法正常兼容\
> 可通过调整IDE的`Arduino AVR Boards by Arduino`库的版本到`1.6.21`并使用其`avrdude.conf`文件