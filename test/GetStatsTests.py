import unittest
from main.GetStats import *


class GetSalariesTests(unittest.TestCase):

    def test_http_response_200(self):
        self.assertEqual(str(playerReq), '<Response [200]>')

    def test_valid_dk_player_names(self):
        self.assertTrue(playerList)
        for dude in playerList:
            self.assertTrue(dude.isalpha() or any(x in dude for x in [' ', '.', "'", 'D/ST']))
