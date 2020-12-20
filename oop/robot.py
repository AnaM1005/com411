class Robot:

  # class attribute
  laws = "Protect, Obey and Survive"
  
  # class (constant) attribute
  MAX_ENERGY = 100

  # A static method
  def the_laws():
    print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self, name="Robot", age=0):

    # An instance attribute
    self.name = name
    self.age = age
    self.energy = Robot.MAX_ENERGY
  
  def display(self):
    print(f"I am {self.name}")
  
if (__name__=="__main__"):
  robot = Robot()
  robot.display()