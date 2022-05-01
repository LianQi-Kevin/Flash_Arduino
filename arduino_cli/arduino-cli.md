## arduino-cli installation and basic operation

### Step - 1 下载并安装 arduino-cli

#### 1. 下载`arduino-cli`的可执行文件

[arduino-cli_0.21.1_Linux_ARM64.tar.gz](https://downloads.arduino.cc/arduino-cli/arduino-cli_0.21.1_Linux_ARM64.tar.gz)
> 其余版本自行下载：[Download arduino-cli](https://arduino.github.io/arduino-cli/0.21/installation/#download)

#### 2. 解压并赋予管理员权限

```
unzip arduino-cli_0.21.1_Linux_ARM64.tar.gz
cd arduino-cli_0.21.1_Linux_ARM64
sudo chmod 777 arduino-cli
```

#### 3. 将文件置于`/bin/`并重启

```
sudo cp arduino-cli /bin/
sudo reboot
```

#### 4. 检查安装

```
$ arduino-cli help

Arduino Command Line Interface (arduino-cli).

Usage:
  arduino-cli [command]

Examples:
  arduino-cli <command> [flags...]

Available Commands:
  board           Arduino board commands.
  burn-bootloader Upload the bootloader.
  cache           Arduino cache commands.
  compile         Compiles Arduino sketches.
  completion      Generates completion scripts
  config          Arduino configuration commands.
  core            Arduino core operations.
  daemon          Run as a daemon on port: 50051
  debug           Debug Arduino sketches.
  help            Help about any command
  lib             Arduino commands about libraries.
  monitor         Open a communication port with a board.
  outdated        Lists cores and libraries that can be upgraded
  sketch          Arduino CLI sketch commands.
  update          Updates the index of cores and libraries
  upgrade         Upgrades installed cores and libraries.
  upload          Upload Arduino sketches.
  version         Shows version number of Arduino CLI.

Flags:
      --additional-urls strings   Comma-separated list of additional URLs for the Boards Manager.
      --config-file string        The custom config file (if not specified the default will be used).
      --format string             The output format for the logs, can be: text, json, jsonmini, yaml (default "text")
  -h, --help                      help for arduino-cli
      --log-file string           Path to the file where logs will be written.
      --log-format string         The output format for the logs, can be: text, json
      --log-level string          Messages with this level and above will be logged. Valid levels are: trace, debug, info, warn, error, fatal, panic
      --no-color                  Disable colored output.
  -v, --verbose                   Print the logs on the standard output.

Use "arduino-cli [command] --help" for more information about a command.
```

### Step - 2 arduino-cli 基本操作

#### 1. 创建配置文件

```
arduino-cli config init
```

默认的配置文件生成位置是`~/.arduino15/arduino-cli.yaml` \
参照[Arduino CLI 0.21 Configuration](https://arduino.github.io/arduino-cli/0.21/configuration/) 进行配置

#### 2. 创建一个新项目

1. 创建新项目

```
$ arduino-cli sketch new ~/MyFirstSketch
Sketch created in: ~/MyFirstSketch
```

2. 查看并编辑

```
$ vim ~/MyFirstSketch/MyFirstSketch.ino
void setup() {
}

void loop() {
}
```

#### 3. 更新缓存并连接Arduino

1. 更新可用平台和库的本地缓存

```
arduino-cli core update-index
```

2. 使用USB线连接Arduino和PC后检查是否被识别

```
$ arduino-cli board list

Port         Protocol Type              Board Name       FQBN                 Core       
/dev/ttyACM0 serial   Serial Port (USB) Arduino Leonardo arduino:avr:leonardo arduino:avr
/dev/ttyACM1 serial   Serial Port (USB) Arduino Uno      arduino:avr:uno      arduino:avr
```

3. 安装内核

```
# 对于arduino:avr内核
arduino-cli core install arduino:avr
```

#### 4. 安装库

1. 搜索库

```
$ arduino-cli lib search pinchange
Updating index: library_index.json.gz downloaded                                                                                                              
Updating index: library_index.json.sig downloaded                                                                                                             
Name: "EasyButtonAtInt01"
  Author: Armin Joachimsmeyer
  Maintainer: Armin Joachimsmeyer <armin.arduino@gmail.com>
  Sentence: Small and easy to use Arduino library for using push buttons at INT0/pin2 and / or any PinChangeInterrupt pin.<br/>Functions for long and double press detection are included.<br/><br/>Just connect buttons between ground and any pin of your Arduino - that's it<br/><br/><b>No call</b> of begin() or polling function like update() required. No blocking debouncing delay.<br/>
  Paragraph: <br/>Define an EasyButtonIn in you main program and use <i>ButtonStateIsActive</i> or <i>ButtonToggleState</i> to determine your action.<br/>Or use a <b>callback function</b> which will be called once on every button press or release.<br/><br/>Usage:<pre>#define USE_BUTTON_0<br/>#include "EasyButtonAtInt01.hpp"<br/>EasyButton Button0AtPin2;<br/><br/>void setup() {}<br/>void loop() {<br/>...<br/>    digitalWrite(LED_BUILTIN, Button0AtPin2.ButtonToggleState);<br/>...<br/>}</pre><br/><br/><b>New: </b>Avoid mistakenly double press detection after boot.</b><br/>
  Website: https://github.com/ArminJo/EasyButtonAtInt01
  Category: Signal Input/Output
  Architecture: avr
  Types: Contributed
  Versions: [1.0.0, 2.0.0, 2.1.0, 3.0.0, 3.1.0, 3.2.0, 3.3.0, 3.3.1]
  Provides includes: Arduino.h
Name: "IRLremote"
  Author: NicoHood
  Maintainer: NicoHood <blog@NicoHood.de>
  Sentence: Lightweight Infrared library for Arduino
  Paragraph: IRLremote implements a fast and compact way to analyze IR signals with PinInterrupts and PinChangeInterrupts.
  Website: https://github.com/NicoHood/IRLremote
  Category: Signal Input/Output
  Architecture: avr, esp8266
  Types: Contributed
  Versions: [1.7.4, 1.8.0, 1.9.0, 2.0.0, 2.0.1, 2.0.2]
Name: "PinChangeInterrupt"
  Author: NicoHood
  Maintainer: NicoHood <blog@NicoHood.de>
  Sentence: A simple & compact PinChangeInterrupt library for Arduino.
  Paragraph: PinChangeInterrupt library with a resource friendly implementation (API and LowLevel). PinChangeInterrupts are different than normal Interrupts. See readme for more information.
  Website: https://github.com/NicoHood/PinChangeInterrupt
  Category: Signal Input/Output
  Architecture: avr
  Types: Contributed
  Versions: [1.2.0, 1.2.1, 1.2.2, 1.2.4, 1.2.6, 1.2.7, 1.2.8, 1.2.9]
```

2. 安装库

```
$ arduino-cli lib install PinChangeInterrupt
Downloading PinChangeInterrupt@1.2.9...
PinChangeInterrupt@1.2.9 downloaded
Installing PinChangeInterrupt@1.2.9...
Installed PinChangeInterrupt@1.2.9
```

#### 5. 编译并上传项目到Arduino开发板

1. 编译项目

```
arduino-cli compile -b arduino:avr:uno ~/MyFirstSketch
```

> --build-cache-path 保存编译后文件的位置 (指定位置将生成一个`core`文件夹)\
> -b 限定板型 即FQBN \
> -p 指定编译后上传的端口 e.g.: COM3 或 /dev/ttyACM0 \
> 注: 通过为`compile`命令指定`-u`参数来执行编译后上传
> ```
> arduino-cli compile -b arduino:avr:uno -p /dev/ttyACM0 -u ~/MyFirstSketch 
> ```

* https://arduino.github.io/arduino-cli/0.21/commands/arduino-cli_compile/

2. 上传项目

```
arduino-cli upload -b arduino:avr:uno  -p /dev/ttyACM1 ~/MyFirstSketch
```

> -b 限定板型 即FQBN \
> -p 指定编译后上传的端口 e.g.: COM3 或 /dev/ttyACM0 \
> -i 指定要用于上传的二进制文件 \
> -t 上传后验证

* https://arduino.github.io/arduino-cli/0.21/commands/arduino-cli_upload/

### Step - 3 使用本地文件

#### 1. 将本地`arduino`项目文件夹上传到`Jetson Nano`

#### 2. 使用`arduino-cli`编译并上传

```
arduino-cli compile -b arduino:avr:uno -p /dev/ttyACM0 -u -t 项目文件夹
```

---

#### 参考资料

* [arduino-cli 官方网站 快速入门](https://arduino.github.io/arduino-cli/0.21/getting-started/)
* [arduino-cli github官网](https://github.com/arduino/arduino-cli/)