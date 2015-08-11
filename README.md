# tessel-python

We're authoring a Python library for Tessel. 

* Goal: be the low-level interface for Tessel's high speed GPIO interfaces, on which other modules can build.
* The bulk of this work is porting [tessel.js](https://github.com/tessel/t2-firmware/blob/master/node/tessel.js) to equivalent Python interfaces.
* Eventually this will be merged into `t2-firmware`.
* Currently Tessel ships Python 2, but goal would be Python 2 and 3 compatibility via `six`.
* Get involved by submitting PRs, issues, or contacting [@timcameronryan](https://twitter.com/timcameronryan).

## totally-barebones example!

```py
import time
import tessel

while True:
    for led in tessel.led:
        led.write(1)
    time.sleep(.2)
    for led in tessel.led:
        led.write(0)
    time.sleep(.2)
```

## license

MIT/ASL2
