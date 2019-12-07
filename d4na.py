from sys import stdin
from d4n import parse_input
from d4n import is_increasing
from d4n import has_double

for password in parse_input(stdin):
 if is_increasing(password) and has_double(password):
  print(password)

