#!python
import random

_chars="23456789ABDEFGHJQRTabdefghijqrt"

def alnum(l):
  return ''.join(random.sample(_chars * l, l))
