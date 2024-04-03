from lib.gratitudes import *

def test_things_to_be_grateful_for():
    gratitude = Gratitudes()
    gratitude.add("my family")
    gratitude.add("good health")
    gratitude.add("my husband")
    gratitude.add("my children")
    assert gratitude.format() == "Be grateful for: my family, good health, my husband, my children"
    