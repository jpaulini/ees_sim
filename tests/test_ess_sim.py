#!/bin/python
# -*- coding: utf-8 -*-
import sys, json
import requests
import unittest

# sys.path.append("../app")
# from app import ees_sim_v1

# class TestFunction(unittest.TestCase):
#     """Test for ees_sim_v1 request"""
#     def test_ees_sim_v1(self):
#         out = ees_sim_v1()
#         self.assertEqual(out, '{ "message": "I\'m alive in eesSim!"}')
class TestEesSim(unittest.TestCase):
    def setUp(self):
        self.data_in = {
                "cluster": ["DW1001", "DW1005", "DW1006", "DW1007"],
                "simulacion": {
                               "x": -60.7439430569999,
                               "y": -32.7657464119999 }
            }
    
    def test_basic_found(self):
        r = requests.post('http://127.0.0.1:5000/eesSim', data = self.data_in)
        self.assertEqual(r.status_code, 200)
    
    def test_json_exists(self):
        r = requests.post('http://127.0.0.1:5000/eesSim', data = self.data_in)
        json_out = r.json()
        self.assertNotEqual(json_out, None)

    def test_json_contains_cluster(self):
        r = requests.post('http://127.0.0.1:5000/eesSim', data = self.data_in)
        json_out = r.json()
        self.assertNotEqual(json_out['result']['cluster'], None)

    def test_json_contains_cluster_length(self):
        r = requests.post('http://127.0.0.1:5000/eesSim', data = self.data_in)
        json_out = r.json()
        cluster = json_out['result']['cluster']
        self.assertEqual(json_out['result']['cluster_length'], len(cluster))

    def test_json_contains_simulacion(self):
        r = requests.post('http://127.0.0.1:5000/eesSim', data = self.data_in)
        json_out = r.json()
        self.assertNotEqual(json_out['result']['simulacion'], None)

if __name__ == '__main__':
    unittest.main()