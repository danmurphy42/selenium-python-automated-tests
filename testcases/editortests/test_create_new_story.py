import unittest
from helpers.screenshot_listener import capture_screenshot
from pageobjects.editor import EditorDashboard, ComposeTab, FinalizeTab
from pageobjects.login import LoginScreen
from pageobjects.published_entry import PublishedEntry
from webdriver import Driver
from values import strings


class CreateNewStory(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.get(strings.Urls.editor_url)
        self.driver.add_cookie(strings.Cookies.editor_test_blog_password_cookie)

    @capture_screenshot
    def test_create_new_story(self):
        login_screen = LoginScreen(self.driver)
        login_screen.login(strings.LoginCredentials.editorUsername, strings.LoginCredentials.editorPassword)
        editor_dashboard = EditorDashboard(self.driver)
        editor_dashboard.create_new_story()
        compose_tab = ComposeTab(self.driver)
        compose_tab.type_headline("Article Headline")
        compose_tab.type_dek("Article Dek")
        compose_tab.click_select_art()
        lead_art_dropdown = ComposeTab.LeadArtDropdown(self.driver)
        lead_art_dropdown.upload_lead_art("assets/ah-jpg.jpg")
        add_image_modal = ComposeTab.AddImageModal(self.driver)
        add_image_modal.click_insert_image()
        compose_tab.add_story_content("This is the first line of a story.")
        editor_dashboard.saved()
        compose_tab.click_finalize()
        finalize_tab = FinalizeTab(self.driver)
        editor_dashboard.saved()
        finalize_tab.click_publish_button()
        finalize_tab.click_confirm_publish_now()
        editor_dashboard.view_published_entry("story")
        published_entry = PublishedEntry(self.driver)
        published_entry.story_items_displayed(
            "Article Headline",
            "Article Dek",
            "This is the first line of a story."
        )

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
