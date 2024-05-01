# pylint: disable=missing-module-docstring,missing-function-docstring,missing-class-docstring,line-too-long
import unittest

from src.vinted_scraper.utils import get_random_user_agent


class TestUtils(unittest.TestCase):
    def test_random_user_agent(self):
        """
        Ensure that the user agent function doesn't raise any exceptions
        """
        try:
            get_random_user_agent()
        except Exception as e:  # pylint: disable=broad-exception-caught
            self.fail(f"get_random_user_agent() raised an exception: {e}")


if __name__ == "__main__":
    unittest.main()
