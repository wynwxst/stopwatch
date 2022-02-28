import time
class utils:
  def gettime():
    current = time.asctime( time.localtime(time.time()))
    current = current.split()
    current = current[3]
    current = current.replace(":"," ")
    current = current.split()
    hours = current[0]
    minutes = current[1]
    sec = current[2]
    return current

  def getsecs():
    current = utils.gettime()
    hours = current[0]
    minutes = current[1]
    sec = current[2]
    sec = int(sec)
    e = int(hours)*360
    sec += int(e)
    f = int(minutes)*60

    sec += int(f)
    return sec

  def roundcd(seconds):
    sec = utils.getsecs()
    if int(sec) > int(seconds):
      return
    sec = int(seconds) - int(sec)
    if sec < 60:
      return f"{round(sec)} second(s)"
    if sec < 360:
      return f"{round(sec/60)} minute(s)"
    if sec < 21600:
      return f"{round(sec/360)} hour(s)"
    if sec < 86400:
      return f"{round(sec/21600)} day(s)"

class StopWatch:
  def __init__(self):
    # ok
    self.strt = None
    self.tick = None
    self.pse = None
    self.end = None
    self.pseval = None
    self.paused = None
    self.running = False
    print("initalized stopwatch!")
  def start(self):

    self.running = True
    if self.pse == True:
      return
    if self.end == True:
      return
    self.strt = utils.getsecs()
  def pause(self):
    self.pse = True
    self.tick = utils.getsecs() - self.strt
    self.pseval = utils.getsecs()
    self.paused = True
    self.running = False
  def stop(self):
    self.end = True
    self.tick = utils.getsecs() - self.strt
    self.running = False
  def unpause(self):
    if self.end == True:
      return
    self.paused = None
    self.pse = None
    self.running = True

  def reset(self):
    self.tick = None
    self.pse = None
    self.end = None
    self.pseval = None
    self.paused = None
    self.running = False
    self.strt = None
  def restart(self):
    
    self.tick = None
    self.pse = None
    self.end = None
    self.pseval = None
    self.paused = None
    self.running = None
    self.running = True
    self.strt = utils.getsecs()
    
  @property
  def duration(self):
    if self.running == False and self.paused == False:
      return None
    if self.pse == True:
      return self.tick
    if self.end == True:
      return self.tick
    if self.paused != None:
      self.tick = self.pseval - self.strt
    elif self.pseval != None:
      tm = self.pseval - self.strt
      self.tick = utils.getsecs() - self.strt
      tm = self.pseval - self.strt
      self.tick -= tm
    elif self.tick == None:
      self.tick = utils.getsecs() - self.strt

    return str(self.tick)
  