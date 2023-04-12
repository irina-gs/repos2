import os
import pytest


@pytest.mark.usefixtures("setup")
class Tests:
    def test_title(self):
        self.driver.get(os.getenv('https://p.mrsu.ru'))
        assert self.driver.title == "Вход - ЭИОС"
