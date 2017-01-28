import idgen
import pytest
import uuid

def test_generate_uuid():
  assert idgen.uuid() is not None

def test_generate_uuid_is_valid_uuid():
  assert uuid.UUID(idgen.uuid())

def test_subsequent_uuids_are_not_the_same():
  assert idgen.uuid() != idgen.uuid()
