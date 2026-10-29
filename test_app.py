"""
Automated Endpoint and Algorithm Test Suite
Tests all OS algorithms and Flask API routes.
"""
import json
import unittest
from app import app

class OsExplainerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        res = self.app.get('/')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Jeevika S', res.data)
        self.assertIn(b'Operating Systems Concepts Explainer Pack', res.data)
        print("[PASS] Home page renders with Jeevika S metadata")

    def test_health(self):
        res = self.app.get('/api/health')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data['status'], 'healthy')
        self.assertEqual(data['author'], 'Jeevika S')
        print("[PASS] Health API check passed")

    def test_cpu_scheduling(self):
        payload = {
            "algorithm": "FCFS",
            "processes": [
                {"id": "P1", "at": 0, "bt": 4, "priority": 1},
                {"id": "P2", "at": 1, "bt": 3, "priority": 2}
            ],
            "quantum": 2
        }
        res = self.app.post('/api/cpu-scheduling', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(len(data['data']['processes']), 2)
        print("[PASS] CPU Scheduling API check passed (FCFS)")

    def test_banker_algorithm(self):
        payload = {
            "available": [3, 3, 2],
            "alloc_matrix": [
                [0, 1, 0],
                [2, 0, 0],
                [3, 0, 2],
                [2, 1, 1],
                [0, 0, 2]
            ],
            "max_matrix": [
                [7, 5, 3],
                [3, 2, 2],
                [9, 0, 2],
                [2, 2, 2],
                [4, 3, 3]
            ]
        }
        res = self.app.post('/api/bankers-algorithm', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        self.assertTrue(data['data']['is_safe'])
        print(f"[PASS] Banker's Algorithm check passed (Safe sequence: {data['data']['safe_sequence']})")

    def test_page_replacement(self):
        payload = {
            "algorithm": "FIFO",
            "pages": "7, 0, 1, 2, 0, 3",
            "num_frames": 3
        }
        res = self.app.post('/api/page-replacement', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        self.assertGreater(data['data']['summary']['page_faults'], 0)
        print("[PASS] Page Replacement API check passed (FIFO)")

    def test_disk_scheduling(self):
        payload = {
            "algorithm": "SCAN",
            "requests": "98, 183, 37, 122, 14",
            "initial_head": 50,
            "disk_size": 200,
            "direction": "right"
        }
        res = self.app.post('/api/disk-scheduling', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data['success'])
        self.assertGreater(data['data']['total_head_movements'], 0)
        print("[PASS] Disk Scheduling API check passed (SCAN)")

    def test_quiz_and_cheatsheet(self):
        res_q = self.app.get('/api/quiz')
        self.assertEqual(res_q.status_code, 200)
        self.assertEqual(len(res_q.get_json()['questions']), 10)

        res_c = self.app.get('/api/cheatsheet')
        self.assertEqual(res_c.status_code, 200)
        self.assertGreater(len(res_c.get_json()['topics']), 0)
        print("[PASS] Quiz and Cheatsheet APIs passed")

if __name__ == '__main__':
    unittest.main()
