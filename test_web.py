import os
import pytest
from action_tests import ActionTests


@pytest.mark.usefixtures("setup")
class Tests:
    def test_title(self):
        self.driver.get(os.getenv('p.mrsu.ru'))
        assert self.driver.title == "Вход - ЭИОС"
