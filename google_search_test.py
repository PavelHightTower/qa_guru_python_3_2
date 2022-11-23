from selene.support.shared import browser
from selene import be, have


class TestGoogleSearch:
    def test_selene_search(self, open_browser):
        browser.element('[name="q"]').should(be.blank).type(
            'selene python').press_enter()  # уточнил поиск, а то не выдавал из-за локации
        browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

    def test_negative_search(self, open_browser):
        browser.element('[name="q"]').set('6576575675675675675675gfhfgh').press_enter()
        browser.element('[id="center_col"]').should(
            have.text('Your search - 6576575675675675675675gfhfgh - did not match any documents.'))
