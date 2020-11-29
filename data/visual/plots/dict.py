import matplotlib.pyplot as plt
import random as rnd

def data():
  paths = {}

  print("What type of line would you like (:, -- or -)?")
  line_style = input()

  print("What colour would you like (r, g or b)?")
  colour = input()

  print("What style of marker would you like (o, s or ^)?")
  marker_style = input()

  paths['line_style'] = line_style
  paths['colour'] = colour
  paths['marker_style'] = marker_style
  
  return paths

def generate():
  print("How many lines would you like to display?")
  num_lines = int(input())
  
  for num_lines in range(num_lines):
    values = data()

    x = [0, rnd.randrange(1, 10)]
    y = [0, rnd.randrange(1, 10)]

    plt.plot(x, y, f"{values['colour']}{values['line_style']}{values['marker_style']}")

  plt.show()


def run():
  print("Running...")
  generate ()
  print("Done!")
  
run()

