```
python3 install -r requirements.txt
```


nano conf.toml
```
[device]
port = "/dev/ttyUSB0"
baud = "921600"

[firmware]
path = "./firmwares/esp32c3-20220117-v1.18.bin"
```

```
python3 flash.py
```

ref:

[firmwares](https://micropython.org/download/esp32c3/)