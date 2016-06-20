
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/5e3e30f736e049f4a4e8b22735490279)](https://www.codacy.com/app/leicas/multicom?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ISIR-MAP/multicom&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/5e3e30f736e049f4a4e8b22735490279)](https://www.codacy.com/app/leicas/multicom?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ISIR-MAP/multicom&amp;utm_campaign=Badge_Coverage)
# multicom
Python class to communicate with usb/serial/ftdi haptic devices
## How to use
```
ìmport multicom.com as com
```
### For FTDI Devices
```
HAPTICDEV = com.HDevice("ftdi")

```
### For Serial Devices
```
HAPTICDEV = com.HDevice("COM8")

```
### Launch
```
HAPTICDEV.launch() #starts the read/write threads on a different process
```
### Usefull Read functions
#### get()
Return raw data
#### readarray(size)
Return a bytearray of desired size
#### readsep(separator, size)
Read a sequence of "float separator float separator ..." of desired size

### Usefull Write functions
#### write(tosend)
convert to send to an int and send

### Quit
```
HAPTICDEV.quit() # stops the threads
```