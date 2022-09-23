from stanfordkarel import *


class ktools:
  def m(self):
    """shorthand for move"""
    move()
    
  def tl(self):
    """Turn Left"""
    turn_left()

  def tr(self):
    """Turn Right"""
    self.tl()
    self.tl()
    self.tl()

  def ta(self):
    """Turn Around"""
    self.tl()
    self.tl()

  def pick(self):
    """Pick Beeper"""
    pick_beeper()

  def pick3(self):
    self.pick()
    self.m()
    self.pick()
    self.m()
    self.pick()
    

  def put(self):
    """Put Beeper"""
    put_beeper()

  def put2(self):
    """Put 2 beepers in a line"""
    self.put()
    self.m()
    self.put()

  def put5(self):
    """Put 5 beepers in a line"""
    self.put2()
    self.m()
    self.put2()
    self.m()
    self.put()

  def put3(self):
    self.put2()
    self.m()
    self.put()

  def h(self):
    """Print H using beepers"""
    self.tl()
    self.put5()
    self.tr()
    self.m()
    self.m()
    self.m()
    self.tr()
    self.put5()
    self.ta()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.put2()
    self.tl()
    self.m()
    self.m()
    self.tl()
    self.m()
    self.m()
    self.m()
    self.m()

  def m2(self):
    """Move 2"""
    self.m()
    self.m()

  def m5(self):
    """Move 5"""
    self.m2()
    self.m2()
    self.m()

  def fic(self):
    """Front is Clear"""
    return front_is_clear()

  def fib(self):
    """Front is Blocked"""
    return not self.fic()

  def ric(self): 
    """Right is Clear"""
    self.tr()
    if self.fic():
      self.tl()
      return True 
    self.tl()
    return False
  
  def rib(self):
    """Right is Blocked"""
    return not self.ric()

  def mazemove(self):
    """Maze Move"""
    if self.fib():
      self.tl()
    else:
      self.m()
      if self.ric():
        self.tr()
        self.m()
        if self.ric():
          self.tr()
          self.m()
    pass
        

  
    

    
    
def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.m2()
    kt.tl()
    kt.m2()
    kt.pick()
    kt.m()
    kt.pick3()
    kt.tr()
    kt.m()
    kt.pick3()
    kt.tr()
    kt.m()
    kt.pick3()
    kt.tr()
    kt.m()
    kt.pick3()
    kt.tr()

    pass


if __name__ == "__main__":
    run_karel_program()