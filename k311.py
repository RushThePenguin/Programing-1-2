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

  def m4(self):
    """Move 4 times"""
    self.m()
    self.m()
    self.m()
    self.m()

  def m3(self):
    """Move 3 times"""
    self.m()
    self.m()
    self.m()

 

def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.m4()   
    kt.tl()
    kt.m4()
    kt.put()
    kt.tl()
    kt.m3()
    kt.tr()
    kt.m()
    kt.tr()
    kt.m3()
    kt.put()
    kt.tl()
    kt.m3()
    kt.tr()
    kt.m()
    kt.tr()
    kt.m3()
    kt.put()
    kt.tl()
    kt.m3()
    kt.tr()
    kt.m()
    kt.tr()
    kt.m3()
    kt.put()
    kt.tl()
    kt.m3()
    kt.tr()
    kt.m4()
    kt.tl()
    
    pass


if __name__ == "__main__":
    run_karel_program()