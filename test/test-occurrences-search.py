"""Tests for occurrences module - search methods"""
import os
from pygbif import occurrences

keyz = ['count', 'facets', 'results', 'endOfRecords', 'limit', 'offset']

def test_search():
    "occurrences.search - basic test"
    res = occurrences.search(taxonKey = 3329049)
    assert 'dict' == res.__class__.__name__
    assert 6 == len(res)
    assert sorted(keyz) == sorted(res.keys())

def test_search_():
    "occurrences.search - diff taxonKey"
    res = occurrences.search(taxonKey = 2431762)
    assert 'dict' == res.__class__.__name__
    assert 6 == len(res)
    assert 2431762 == res['results'][0]['taxonKey']

def test_search_():
    "occurrences.search - diff taxonKey2"
    res = occurrences.search(taxonKey = 2683264)
    assert 'dict' == res.__class__.__name__
    assert 6 == len(res)
    assert 2683264 == res['results'][0]['taxonKey']

def test_search_occurrenceID():
    "occurrences.search - diff occurrenceID"
    uuid = "a55e740b-55af-4029-9481-74e0e5049581"
    res = occurrences.search(occurrenceID = uuid)
    assert 'dict' == res.__class__.__name__
    assert 6 == len(res)
    assert uuid == res['results'][0]['occurrenceID']

