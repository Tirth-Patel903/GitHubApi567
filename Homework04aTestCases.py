import unittest
from Homework04a import get_repo_commits

class TestGetRepoCommits(unittest.TestCase):

    def test_user_has_repos(self):
        result = get_repo_commits("Tirth-Patel903")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_user_does_not_exist(self):
        result = get_repo_commits("thisusernamedoesnotexist")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
