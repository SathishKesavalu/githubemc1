class Bird:
  def __init__(self):
    print("Bird is ready")

  def who(self):
    print("bird")

  def swim(self):
    print("Swim Faster")

class Penquin(Bird):
  def __init__(self):
    super().__init__()
    print("Penquin is ready")

  def who(self):
    print ("penquin")

  def run(self):
    print ("Run Faster")

test1 = Penquin()
test1.who()
test1.swim()