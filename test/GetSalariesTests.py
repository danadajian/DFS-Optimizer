import unittest
from main.GetSalaries import *
from main.GetStats import finalPlayerList


def chars_in_common(s1, s2):
    ind_matches = [(i, j) for i in range(len(s1)) for j in range(len(s2)) if s1[i] == s2[j]]
    if not ind_matches:
        return 0
    consec_list = []
    for (i, j) in ind_matches:
        consec_count = 1
        while i+1 < len(s1) and j+1 < len(s2):
            if s1[i+1] == s2[j+1]:
                i += 1
                j += 1
                consec_count += 1
            else:
                break
        consec_list.append(consec_count)
    return max(consec_list)


class GetSalariesTests(unittest.TestCase):

    def test_http_response_200(self):
        self.assertEqual(str(dfsReq), '<Response [200]>')

    def test_player_check(self):
        self.assertEqual('Patriots D/ST', player_check('New England D'))
        self.assertEqual('Raiders D/ST', player_check('Oakland'))
        self.assertEqual('Saquon Barkley', player_check('Saquon Barkley'))

    def test_chars_is_common(self):
        self.assertEqual(5, chars_in_common('Saquon Barkley', 'n Bar'))

    def test_valid_dk_player_names(self):
        self.assertTrue(siteSalaries[0].keys())
        for player in siteSalaries[0].keys():
            self.assertTrue(player.isalpha() or any(x in player for x in [' ', '.', "'", 'D/ST']))
            self.assertTrue(player == p for p in finalPlayerList if chars_in_common(player, p) > len(p) - 3)

    def test_valid_fd_player_names(self):
        self.assertTrue(siteSalaries[1].keys())
        for player in siteSalaries[1].keys():
            self.assertTrue(player.isalpha() or any(x in player for x in [' ', '.', "'", 'D/ST']))
            self.assertTrue(player == p for p in finalPlayerList if chars_in_common(player, p) > len(p) - 3)

    def test_valid__dk_salaries(self):
        self.assertTrue(siteSalaries[0].values())
        for salary in siteSalaries[0].values():
            self.assertTrue(str(salary).isnumeric())
            self.assertTrue(len(str(salary)) in [4, 5])

    def test_valid__fd_salaries(self):
        self.assertTrue(siteSalaries[0].values())
        for salary in siteSalaries[1].values():
            self.assertTrue(str(salary).isnumeric())


