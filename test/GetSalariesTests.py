import unittest
from main.GetSalaries import *
from main.GetStats import finalPlayerList


def chars_in_common(s1, s2):
    s1_matches = [i for i in range(len(s1)) if s1[i] in s2]
    s2_matches = [j for j in range(len(s2)) if s2[j] in [s1[i] for i in s1_matches]]
    if not s1_matches:
        return 0
    consec_list = []


    for i in matching_chars:
        consec_count = 1
        for j in s2[s2.index(s1[i])+1:]:
            if s1[i+1] == j:
                consec_count += 1
        consec_list.append(consec_count)
    return max(consec_list)


print(chars_in_common('gobbledy gook baby', 'ohdledy ghe'))


class GetSalariesTests(unittest.TestCase):

    def test_http_response_200(self):
        self.assertEqual(str(dfsReq), '<Response [200]>')

    def test_player_check(self):
        self.assertEqual('Patriots D/ST', player_check('New England D'))
        self.assertEqual('Raiders D/ST', player_check('Oakland'))
        self.assertEqual('Saquon Barkley', player_check('Saquon Barkley'))

    def test_chars_is_common(self):
        self.assertEqual(3, chars_in_common('danny', 'ann'))

    def test_valid_dk_player_names(self):
        for player in siteSalaries[0].keys():
            self.assertTrue(player.isalpha() or any(x in player for x in [' ', '.', "'", 'D/ST']))

    def test_valid_fd_player_names(self):
        for player in siteSalaries[1].keys():
            self.assertTrue(player.isalpha() or any(x in player for x in [' ', '.', "'", 'D/ST']))
            # self.assertTrue(player in finalPlayerList)

    def test_valid__dk_salaries(self):
        for salary in siteSalaries[0].values():
            self.assertTrue(str(salary).isnumeric())
            self.assertTrue(len(str(salary)) in [4, 5])

    def test_valid__fd_salaries(self):
        for salary in siteSalaries[1].values():
            self.assertTrue(str(salary).isnumeric())


