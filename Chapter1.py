import pytest
 
@pytest.mark.gui_test()
def test_gui():
    print ("GUI Test")
    pass
 
@pytest.mark.api_test()
def test_api():
    print ("API Test")
    pass
