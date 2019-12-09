import unittest
from helpers.screenshot_listener import capture_screenshot
from pageobjects.editor import EditorDashboard, ComposeTab, FinalizeTab
from pageobjects.published_entry import PublishedEntry
from pageobjects.login import LoginScreen
from webdriver import Driver
from values import strings


class AddBodyGallery(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.get(strings.Urls.editor_url)
        self.driver.add_cookie(strings.Cookies.editor_test_blog_password_cookie)

    @capture_screenshot
    def test_add_body_gallery(self):
        login_screen = LoginScreen(self.driver)
        login_screen.login(strings.LoginCredentials.editorUsername, strings.LoginCredentials.editorPassword)
        editor_dashboard = EditorDashboard(self.driver)
        editor_dashboard.create_new_story()
        compose_tab = ComposeTab(self.driver)
        compose_tab.type_headline("Article Headline")
        compose_tab.type_dek("Article Dek")
        compose_tab.click_insert_dropdown_item("Gallery")
        add_gallery_modal = ComposeTab.AddGalleryModal(self.driver)
        add_gallery_modal.click_new_gallery()
        create_gallery_menu = ComposeTab.CreateGalleryMenu(self.driver)
        create_gallery_menu.enter_gallery_title("Article Gallery")
        create_gallery_menu.click_gallery_image_dropdown()
        create_gallery_menu.upload_gallery_images("assets/ah-jpg.jpg", "assets/dc-ah-banner.jpg")
        create_gallery_menu.click_insert_gallery()
        compose_tab.body_item_displayed("gallery")
        editor_dashboard.saved()
        compose_tab.click_finalize()
        finalize_tab = FinalizeTab(self.driver)
        finalize_tab.click_publish_button()
        finalize_tab.click_confirm_publish_now()
        editor_dashboard.view_published_entry("story")
        published_entry = PublishedEntry(self.driver)
        published_entry.body_gallery_displayed()

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
