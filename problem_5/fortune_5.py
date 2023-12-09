fn = lambda a, b: [a, b]

def cons(a, b):
  def pair(f):
    return f(a, b)
  return pair

def car(pair):
  return pair(fn)[0]

def cdr(pair):
  return pair(fn)[1]

print(car(cons(3, 4))) # 3
print(cdr(cons(3, 4))) # 4
