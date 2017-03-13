#  pytestTutorial.py
#   - test how pytest works
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5


# group tests in a TestClass
# to call these tests:
#   $ pytest -q test_class.py       <assuming this code snippet was in a separate file called test_class.py>
class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')