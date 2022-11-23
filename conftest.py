import pytest
from selene.support.shared import browser


@pytest.fixture(scope="class")
def open_browser():
    browser.config.window_height = 950
    browser.config._window_width = 1600
    browser.open('https://google.com/ncr')
    browser.element("[id='L2AGLb']").click()  # убрал окно куки

    yield

    browser.quit()
