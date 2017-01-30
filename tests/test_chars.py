import pytest
import idgen

def test_generate_alnum_id():
  assert idgen.alnum(5) is not None

def test_alnum_length():
  assert len(idgen.alnum(5))==5
  assert len(idgen.alnum(4))==4

def test_multiple_alnum_calls_are_unique():
  assert idgen.alnum(5)!=idgen.alnum(5)
