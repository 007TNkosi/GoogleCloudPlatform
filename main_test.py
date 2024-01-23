from hello import *

def test_hello():
    msg = "Goodbye"
test_hello()

def setup_function(function):
    print("Running Setup: %s" % {function.__name__})
    function.x = 10

def teardown_function(function):
    print("Running Teardown: %s" % {function.__name__})
    del function.x

def test_hello_subtract():
    assert subtract(test_hello_subtract.x) == 9

## -_-_ Test for failure -_-_ ##
# def test_hello_add():
#   assert add(test_hello_add.x) == 12