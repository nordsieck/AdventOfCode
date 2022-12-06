import io
import unittest
import sys

def top(input):
  maxx, curr = 0, 0
  for line in input.readlines():
    line = line.strip()
    if line == "":
      if curr > maxx:
        maxx = curr
      curr = 0
    else:
      curr += int(line)

  if curr > maxx:
    maxx = curr

  return maxx

def topn(input, n):
  curr, entries = 0, []
  for line in input.readlines():
    line = line.strip()
    if line == "":
      entries.append(curr)
      curr = 0
    else:
      curr += int(line)

  if curr > 0:
    entries.append(curr)
      
  entries.sort(reverse=True)
  return sum(entries[:n])

class TestCase(unittest.TestCase):
  def test_topn(self):
    input = [
      ("1\n1\n1", 3, 3),
      ("1\n\n1\n\n1\n\n1", 3, 3),
      ("1\n\n2\n\n3\n\n4", 3, 9),
      ("""1000
      2000
      3000

      4000

      5000
      6000

      7000
      8000
      9000

      10000""", 3, 45000),
      ("10\n\n9\n\n8\n\n7\n\n7\n\n7", 3, 27),
    ]

    for i in input:
      self.assertEqual(topn(io.StringIO(i[0]), i[1]), i[2])
  
  def test_top(self):
    input = [
      ("", 0),
      ("1\n", 1),
      ("1", 1),
      ("100\n", 100),
      ("1\n2", 3),
      ("1\n2\n3", 6),
      ("1\n2\n\n4", 4),
      ("4\n\n1\n2", 4),
      ("""1000
      2000
      3000

      4000

      5000
      6000

      7000
      8000
      9000

      10000""", 24000),
      ("10\n\n9\n\n9\n\n9\n\n9\n\n9", 10),
    ]

    for i in input:
      self.assertEqual(top(io.StringIO(i[0])), i[1])

if __name__ == '__main__':
  print(topn(sys.stdin, 3))
