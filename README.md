# LoRa Payload Counter

> ⚠ NOT FUNCTIONAL YET; CURRENTLY UNDER DEVELOPMENT

This LoRa payload counter is based on [Micropython](https://micropython.org/) and a modified version of the [u‑lora](https://github.com/martynwheeler/u-lora) library by Martyn Wheeler. It is intended to work with ESP32, ESP8266 and Raspberry Pi Pico microcontrollers.

Payload counts are those as being reported by the LoRa chip.


## Installing `esptool.py` and `rshell`
```bash
$ pip install esptool rshell
```

## Installing Micropython
- For ESP32, please, [follow these instructions](https://micropython.org/download/esp32/).


## Using `pyboard.py`
The `pyboard.py` utility comes preinstalled with this repository.
Here is the official [`pyboard.py` documentation](https://docs.micropython.org/en/latest/reference/pyboard.py.html).


## Installing the Payload Counter Firmware
Here is how the firmware scripts `main.py` and `ulora.py` are copied to the device flash drive, called `:`.

```bash
$ pyboard.py --device /dev/ttyUSB2 -f cp main.py ulora.py :
```


## Using `rshell` to Access the Micropython REPL
A device running Micropython has a shell environment, called [the read–eval–print loop (REPL)](https://en.wikipedia.org/wiki/Read–eval–print_loop).
It can be accessed by running the `rshell` tool.
```bash
$ rshell -p /dev/ttyUSB2 -b 115200
repl
```

1. After typing `repl` followed by a <kbd>Return</kbd>, hit <kbd>Ctrl</kbd>+<kbd>D</kbd> to soft reboot the device.
2. You can now monitor the output of the `main.py` script running on the device.
3. Hit <kbd>Ctrl</kbd>+<kbd>X</kbd> to leave the REPL and to return to `rshell`.
4. Hit <kbd>Ctrl</kbd>+<kbd>X</kbd> to leave `rshell` and to return to the command line.
