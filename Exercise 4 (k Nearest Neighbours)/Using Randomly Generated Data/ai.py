# YOUR CODE HERE
import random, math

def common_function(input_data):
    result = []
    output_value = -1
    for value in input_data:
        remainder = value % 3
        if remainder == 0:
            output_value += 1
        result.append(output_value)

    print (result)

distances = {}

num_points = random.randint(10, 60)

data = []

color_categories = ['Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple']

for point_number_a in range(num_points):
    x = random.randint(0, 12)
    y = random.randint(0, 12)
    random_color_category = random.choice(color_categories)
    data.append((random_color_category, (x, y)))

print("Number of points:", num_points, '\n')
print("Coordinates and their colours:", data, '\n')

x = random.randint(0, 12)
y = random.randint(0, 12)

point_of_interest = (x, y)

for point_number_b in range(num_points):
  squared_distance = 0
  for axis in range(len(point_of_interest)):
        squared_distance += (point_of_interest[axis] - data[point_number_b][1][axis]) ** 2
  distances[data[point_number_b]] = math.sqrt(squared_distance)

sorted_dict = dict(sorted(distances.items(), key=lambda item: item[1]))

ordered_points = sorted_dict.keys()
print("Points in order of distance from the point of interest:", ordered_points, '\n')

k = int(input("Input k: "))

shortlisted_points = list(ordered_points)[:k]

print("k points based on distance:", shortlisted_points, '\n')

scores = {}

for element in shortlisted_points:
  colour = element[0]
  if colour not in scores:
    scores[colour] = 1
  else:
    scores[colour] += 1

print(scores, '\n')

if len(scores) > 1:
  sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))

  print("Sorted Scores:", sorted_scores, '\n')

else:
  sorted_scores = scores

num_of_scores = len(sorted_scores)

first_key = list(sorted_scores.keys())[:1]
first_value = sorted_scores[first_key[0]]
if num_of_scores > 1:
  first_key, second_key = list(sorted_scores.keys())[:2]
  second_value = sorted_scores[second_key]
  if first_value > second_value:
      print(f"The value of {first_key} is the highest. Hence, our point of interest is {first_key}")
  elif first_value == second_value and second_value:
      print(f"The value of {first_key} is equal to the value of {second_key}, hence our point of interest can be either {first_key} or {second_key}. \n")
  if num_of_scores > 2:
    first_key, second_key, third_key = list(sorted_scores.keys())[:3]
    third_value = sorted_scores[third_key]
    if first_value == second_value and second_value == third_value:
          print ("More than 2 answers possible. Choose another value of k.")
else:
  print(f"Since {first_key[0]} is the only colour nearby, our point of interest is also {first_key[0]}")