# stopwatch
an insanely simple stopwatch library

### Installation:
`pip install stpwch`

### Usage:
```python
from main import StopWatch,utils
import time

s = StopWatch()
s.start()
time.sleep(5)

print(str(s.duration))
print("bef pause ^")
s.pause()
time.sleep(5)
print(str(s.duration))
print("while pause ^")
s.unpause()
time.sleep(5)
print(str(s.duration))
print("after pause ^")
s.stop()
s.reset()
time.sleep(2)
print(str(s.duration))
print("after reset ^")
print("now starting..")
s.start()
print("running: " + str(s.running))
time.sleep(1)
print(str(s.duration))
print("bef restart ^")
s.restart()
time.sleep(3)
print(str(s.duration))
print("after restart ^")
```

### Development:
Install buildproj:

`pip install buildproj`

`build --build`

In case of the binary not working:

`python buildbinary.py --build`

All processes are automated except for the sign in for pip, please be sure to also change the version and name in `setup.py`






