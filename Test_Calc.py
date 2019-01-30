import pytest
from Calculation import *

@pytest.mark.skip
def test_add_1():
	assert add(100,300) == 400,"failed"

@pytest.mark.skip
def test_add_2():
	assert add(100,200) == 300,"failed"

@pytest.mark.xfail
def test_add_3():
	assert 15+13 == 28,"failed"

@pytest.mark.xfail
def test_add_4():
	assert 15+13 == 100,"failed"

def test_add_5():
	assert 3+2 == 5,"failed"

def test_div_6():
	assert div(3,1) == 1,"failed"
	
def test_div_Error():
	assert div(3,0) == "error: EDIV","failed"


def test_sub():
	assert sub(3,2) == 1,"failed"