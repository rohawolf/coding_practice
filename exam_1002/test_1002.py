import math

# validate pos value
def num_checker(pos_values):
  false_value_cnt = 0

  for value in pos_values:
    if not -10000 <= value <= 10000:
      false_value_cnt += 1
  
  return True if false_value_cnt == 0 else False

# validate distance value
def r_checker(distance_values):
  false_value_cnt = 0

  for value in distance_values:
    if not 0 <= value <= 10000:
      false_value_cnt += 1

  return True if false_value_cnt == 0 else False

# get the count of intersecting points
def intersect_cnt(x1, y1, r1, x2, y2, r2):
  dx = x1 - x2
  dy = y1 - y2
  between_distance = math.sqrt( (dx * dx) +  (dy * dy ))
  
  if between_distance == 0:
    cnt = -1 if r1 == r2 else 0
  
  else:
    if between_distance == (r1 + r2):
      cnt = 1
    elif between_distance > (r1 + r2):
      cnt = 0
    elif between_distance < (r1 + r2):
      cnt = 2

  return cnt

if __name__ == '__main__':
  
    try:
      # get the number of test case T
      t = int(input())

      test_cases = []
      for i in range(t):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())

        if num_checker([x1, y1, x2, y2]) and r_checker([r1, r2]):
          test_cases.append({
            'case_id': i + 1,
            'x1': x1,
            'y1': y1,
            'r1': r1,
            'x2': x2,
            'y2': y2,
            'r2': r2,
          })
        
        else:
          print('x1, y1, x2, y2 must be between -10000 and 10000, r1, r2 must be between 0 and 10000.')
          

      for case in test_cases:
        x1 = case.get('x1')
        y1 = case.get('y1')
        r1 = case.get('r1')
        x2 = case.get('x2')
        y2 = case.get('y2')
        r2 = case.get('r2')

        print('case %s : %s %s %s %s %s %s - the number of intersecting points : %s' % (
          case.get('case_id'),
          x1, y1, r1, x2, y2, r2,
          intersect_cnt(x1, y1, r1, x2, y2, r2),
        ))
        

    except ValueError as ve:
      print('%s : %s' % (ve.__class__, ve))
  

  