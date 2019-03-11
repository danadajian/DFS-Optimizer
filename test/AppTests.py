import unittest
from main.GetStats import *
from main.GetSalaries import *
from main.Optimizer import optimize


class GetStatsTests(unittest.TestCase):

    def test_http_response_200(self):
        self.assertEqual(str(playerReq), '<Response [200]>')

    def test_valid_dk_player_names(self):
        self.assertTrue(playerList)
        for dude in playerList:
            self.assertTrue(dude.isalpha() or any(x in dude for x in [' ', '.', "'", 'D/ST']))


def chars_in_common(s1, s2):
    ind_matches = [(i, j) for i in range(len(s1)) for j in range(len(s2)) if s1[i] == s2[j]]
    if not ind_matches:
        return 0
    consec_list = []
    for (i, j) in ind_matches:
        consec_count = 1
        while i + 1 < len(s1) and j + 1 < len(s2):
            if s1[i + 1] == s2[j + 1]:
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


class OptimizerTests(unittest.TestCase):

    def test_best_team_no_cap(self):
        test_scores = {'qb1': 5, 'rb1': 15, 'rb2': 10, 'rb3': 5, 'wr1': 20, 'wr2': 15, 'wr3': 10, 'wr4': 5, 'te1': 10,
                       'te2': 5, 'dst1': 5}
        test_salaries = {'qb1': 5, 'rb1': 15, 'rb2': 10, 'rb3': 5, 'wr1': 20, 'wr2': 15, 'wr3': 10, 'wr4': 5, 'te1': 10,
                         'te2': 5, 'dst1': 5}
        test_qbs = ['qb1']
        test_rbs = ['rb1', 'rb2', 'rb3']
        test_wrs = ['wr1', 'wr2', 'wr3', 'wr4']
        test_tes = ['te1', 'te2']
        test_dst = ['dst1']
        cap = 10000  # cap is irrelevant
        test_lineup = optimize(test_scores, test_salaries, cap, test_qbs, test_rbs, test_wrs, test_tes, test_dst)
        self.assertEqual(['qb1', 'rb1', 'rb2', 'wr1', 'wr2', 'wr3', 'te1', 'rb3', 'dst1'], test_lineup)

    def test_detect_value_player_no_cap(self):
        # increase wr4 score to 50
        test_scores = {'qb1': 5, 'rb1': 15, 'rb2': 10, 'rb3': 5, 'wr1': 20, 'wr2': 15, 'wr3': 10, 'wr4': 50, 'te1': 10,
                       'te2': 5, 'dst1': 5}
        test_salaries = {'qb1': 5, 'rb1': 15, 'rb2': 10, 'rb3': 5, 'wr1': 20, 'wr2': 15, 'wr3': 10, 'wr4': 5, 'te1': 10,
                         'te2': 5, 'dst1': 5}
        test_qbs = ['qb1']
        test_rbs = ['rb1', 'rb2', 'rb3']
        test_wrs = ['wr1', 'wr2', 'wr3', 'wr4']
        test_tes = ['te1', 'te2']
        test_dst = ['dst1']
        cap = 10000  # cap is irrelevant
        test_lineup = optimize(test_scores, test_salaries, cap, test_qbs, test_rbs, test_wrs, test_tes, test_dst)
        self.assertEqual(['qb1', 'rb1', 'rb2', 'wr1', 'wr2', 'wr3', 'te1', 'wr4', 'dst1'], test_lineup)

    def test_value_player_exceeds_cap(self):
        test_scores = {'qb1': 5, 'rb1': 15, 'rb2': 10, 'rb3': 5, 'wr1': 20, 'wr2': 15, 'wr3': 10, 'wr4': 50, 'te1': 10,
                       'te2': 5, 'dst1': 5}
        # increase wr4 salary to 50
        test_salaries = {'qb1': 5, 'rb1': 15, 'rb2': 10, 'rb3': 5, 'wr1': 20, 'wr2': 15, 'wr3': 10, 'wr4': 50,
                         'te1': 10, 'te2': 5, 'dst1': 5}
        test_qbs = ['qb1']
        test_rbs = ['rb1', 'rb2', 'rb3']
        test_wrs = ['wr1', 'wr2', 'wr3', 'wr4']
        test_tes = ['te1', 'te2']
        test_dst = ['dst1']
        cap = 100  # salary cap now in play and should prevent wr4 from being taken
        test_lineup = optimize(test_scores, test_salaries, cap, test_qbs, test_rbs, test_wrs, test_tes, test_dst)
        self.assertEqual(['qb1', 'rb1', 'rb2', 'wr1', 'wr2', 'wr3', 'te1', 'rb3', 'dst1'], test_lineup)
