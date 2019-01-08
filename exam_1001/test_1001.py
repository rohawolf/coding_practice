

def range_checker(num):
  return num if 0 < num < 10 else False

if __name__ == '__main__':
  a, b = map(int, input().split())

  print('A : %s' % a)
  print('B : %s' % b)

  if not range_checker(a) or not range_checker(b):
    print("the range of input must be between 0 and 10.")

  else:
    print('A - B = %s' % (a - b))