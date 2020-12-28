def findEnd(snk, moves, end):
  x = snk[0]
  y = snk[1]
  for move in moves:
    if move == 'left':
      x -= 1
    elif move == 'right':
      x += 1
    elif move == 'up':
      y += 1
    elif move == 'down':
      y -= 1
    if x == end['x'] and y == end['y']:
      return True
  return False

def valid(snk, body, size, moves):
  x = snk[0]
  y = snk[1]
  for move in moves:
    if move == 'left':
      x -= 1
    elif move == 'right':
      x += 1
    elif move == 'up':
      y += 1
    elif move == 'down':
      y -= 1
    
    if not(0 <= x < size and 0 <= y < size):
      return False
    # elif () #use this to determine if the body is there
  
  return True

def queue_alg(snk, body, size, food):
  #Breadth First Search Algorithm
  if len(food) >= 1:
    food = food[0]
  nums = queue.Queue()
  nums.put("")
  add = ""
  snk = [snk['x'], snk['y']]
  print("Start Loop")
  while not findEnd(snk, add, food):
    add = nums.get()
    for j in ['left', 'right', 'up', 'down']:
      put = add + j
      if valid(snk, body, size, put):
        nums.put(put)
  print("finished loop", add)
  return add