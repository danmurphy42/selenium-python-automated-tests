import unittest
from helpers.screenshot_listener import capture_screenshot
from pageobjects.editor import EditorDashboard, ComposeTab, FinalizeTab
from pageobjects.published_entry import PublishedEntry
from pageobjects.login import LoginScreen
from webdriver import Driver
from values import strings


class AddToGroup(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.get(strings.Urls.editor_url)
        self.driver.add_cookie(strings.Cookies.editor_test_blog_password_cookie)

    @capture_screenshot
    def test_edit_existing_article(self):
        login_screen = LoginScreen(self.driver)
        login_screen.login(strings.LoginCredentials.editorUsername, strings.LoginCredentials.editorPassword)
        editor_dashboard = EditorDashboard(self.driver)
        editor_dashboard.search_for_article("Editable Article (DO NOT DELETE)")
        editor_dashboard.click_existing_article("Editable Article (DO NOT DELETE)")
        compose_tab = ComposeTab(self.driver)
        updated_text = compose_tab.add_new_story_content("THIS IS AN EDIT. ")
        editor_dashboard.saved()
        compose_tab.click_finalize()
        finalize_tab = FinalizeTab(self.driver)
        editor_dashboard.saved()
        finalize_tab.click_publish_changes()
        finalize_tab.click_confirm_publish_changes()
        editor_dashboard.view_published_entry("story")
        published_entry = PublishedEntry(self.driver)
        published_entry.body_text_present(updated_text)

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
