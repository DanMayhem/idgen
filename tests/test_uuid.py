import idgen
import pytest

def test_generate_uuid():
  assert idgen.uuid() is not None
