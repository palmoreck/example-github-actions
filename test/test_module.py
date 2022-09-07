from ..src.module import myfunc

def test_module():
    assert myfunc() == "Hello World!"
    
def test_main():
    return test_module()
