from lib.present import *

# When we wrap an item
# We get it back when unwrapping

def test_present():
    p = Present()

    p.wrap("contents")

    assert p.unwrap() == "contents"