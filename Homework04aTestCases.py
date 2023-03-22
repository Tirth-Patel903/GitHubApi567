import unittest
from unittest.mock import patch
from Homework04a import get_repo_commits

class TestGetRepoCommits(unittest.TestCase):

    @patch('Homework04a.requests.get')
    def test_user_has_repos(self, mock_get):
        mock_get.return_value.json.return_value = [{'commit': 'commit1'}, {'commit': 'commit2'}]
        result = get_repo_commits("Tirth-Patel903")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        mock_get.assert_called_once()

    @patch('Homework04a.requests.get')
    def test_user_does_not_exist(self, mock_get):
        mock_get.return_value.status_code = 404
        result = get_repo_commits("thisusernamedoesnotexist")
        self.assertIsNone(result)
        mock_get.assert_called_once()

if __name__ == '__main__':
    unittest.main()
