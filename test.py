import unittest
from spotifytest import gatherInput, build_url, build_dataframe


class TestFileName(unittest.TestCase):
    def test_gather_input(self):
        user_input = gatherInput()
        self.assertNotEqual(user_input, "")
        self.assertEqual(function1(1), 0)

    def test_get_json(self):
        json_1, json_2 = build_url("dummy_id")
        self.assertTrue(len(json_1) > 0)
        self.assertTrue(len(json_2) > 0)
        
if __name__ == '__main__':
    unittest.main()