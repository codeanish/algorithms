
from src import binary_search


def test_binary_search_single_element():
    assert binary_search.binary_search_blind_implementation([1],1) == 0
    assert binary_search.binary_search_blind_implementation([1],2) == None

def test_binary_search_less_verbose_single_element():
    assert binary_search.binary_search_proper_implementation([1],1) == 0
    assert binary_search.binary_search_proper_implementation([1],2) == None

def test_binary_search_single_element_missing_search_value():
    assert binary_search.binary_search_blind_implementation([1], 2) == None

def test_binary_search_two_elements():
    assert binary_search.binary_search_blind_implementation([1,2],1) == 0
    assert binary_search.binary_search_blind_implementation([1,2],2) == 1
    assert binary_search.binary_search_blind_implementation([1,2],3) == None
    assert binary_search.binary_search_blind_implementation([1,3],2) == None

def test_binary_search_less_verbose_two_elements():
    assert binary_search.binary_search_proper_implementation([1,2],1) == 0
    assert binary_search.binary_search_proper_implementation([1,2],2) == 1
    assert binary_search.binary_search_proper_implementation([1,2],3) == None
    assert binary_search.binary_search_proper_implementation([1,3],2) == None

def test_binary_search_3_elements():
    assert binary_search.binary_search_blind_implementation([1,2,3],1) == 0
    assert binary_search.binary_search_blind_implementation([1,2,3],2) == 1
    assert binary_search.binary_search_blind_implementation([1,2,3],3) == 2

def test_binary_search_less_versbose_3_elements():
    assert binary_search.binary_search_proper_implementation([1,2,3],1) == 0
    assert binary_search.binary_search_proper_implementation([1,2,3],2) == 1
    assert binary_search.binary_search_proper_implementation([1,2,3],3) == 2

def test_binary_search_4_elements():
    assert binary_search.binary_search_blind_implementation([1,2,3,4],1) == 0
    assert binary_search.binary_search_blind_implementation([1,2,3,4],2) == 1
    assert binary_search.binary_search_blind_implementation([1,2,3,4],3) == 2
    assert binary_search.binary_search_blind_implementation([1,2,3,4],4) == 3
    assert binary_search.binary_search_blind_implementation([1,2,3,4],5) == None

def test_binary_search_less_verbose_4_elements():
    assert binary_search.binary_search_proper_implementation([1,2,3,4],1) == 0
    assert binary_search.binary_search_proper_implementation([1,2,3,4],2) == 1
    assert binary_search.binary_search_proper_implementation([1,2,3,4],3) == 2
    assert binary_search.binary_search_proper_implementation([1,2,3,4],4) == 3
    assert binary_search.binary_search_proper_implementation([1,2,3,4],5) == None

def test_binary_search_5_elements():
    assert binary_search.binary_search_blind_implementation([1,2,3,4,5], 1) == 0
    assert binary_search.binary_search_blind_implementation([1,2,3,4,5], 2) == 1
    assert binary_search.binary_search_blind_implementation([1,2,3,4,5], 3) == 2
    assert binary_search.binary_search_blind_implementation([1,2,3,4,5], 4) == 3
    assert binary_search.binary_search_blind_implementation([1,2,3,4,5], 5) == 4
    assert binary_search.binary_search_blind_implementation([1,2,3,4,5], 6) == None
    assert binary_search.binary_search_blind_implementation([1,2,3,5,6], 4) == None

def test_binary_search_less_verbose_5_elements():
    assert binary_search.binary_search_proper_implementation([1,2,3,4,5], 1) == 0
    assert binary_search.binary_search_proper_implementation([1,2,3,4,5], 2) == 1
    assert binary_search.binary_search_proper_implementation([1,2,3,4,5], 3) == 2
    assert binary_search.binary_search_proper_implementation([1,2,3,4,5], 4) == 3
    assert binary_search.binary_search_proper_implementation([1,2,3,4,5], 5) == 4
    assert binary_search.binary_search_proper_implementation([1,2,3,4,5], 6) == None
    assert binary_search.binary_search_proper_implementation([1,2,3,5,6], 4) == None