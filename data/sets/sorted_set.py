def observed():
  observations = []
  for count in range(5):
    print("Please enter an observation:")
    observation = input()
    observations.append(observation)
  return observations

def remove_observations(observations):
  is_running = True
  while (is_running):
    print("Do you wish to remove an observation (yes/no)?")
    response = input()

    if (response == "yes"):
      print("What observation would you like to remove?")
      observation = input()
      observations.remove(observation)
    else:
      is_running = False

def run():
  observations = observed()
  remove_observations(observations)

  observations_set = set()

  for observation in observations:
    data = (observation, observations.count(observation))
    observations_set.add(data)
  
  for observation, count in sorted(observations_set):
    print(f"{observation} observed {count} times.")

run()