
def range_checker(num):
  return num if -10000 <= num <= 10000 else False

if __name__ == '__main__':
  
    try:
      # get the number of test case T
      t = int(input())

      test_cases = []
      for i in range(t):
        x1, y1, r1, x2, y2, r2 = map(int, input.split())
        test_cases.append({
          'case_id': i,
          'x1': x1,
          'y1': y1,
          'r1': r1,
          'x2': x2,
          'y2': y2,
          'r2': r2,
        })

      for case in test_cases:
        print('case %s : %s %s %s %s %s %s' % (
          case.get('case_id'),
          case.get('x1'),
          case.get('y1'),
          case.get('r1'),
          case.get('x2'),
          case.get('y2'),
          case.get('r2'),
        ))

    except ValueError as ve:
      print('%s : %s' % (ve.__class__, ve))
  

  