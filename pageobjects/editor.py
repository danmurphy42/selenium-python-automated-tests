import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pageobjects.base_page import BasePage


class EditorDashboard(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.element_visible(By.CLASS_NAME, "m-dashboard__content")  # Editor Dashboard loaded.

    def create_new_story(self):
        self.click_element(By.LINK_TEXT, "New story")

    def search_for_article(self, article_name):
        self.type(By.XPATH, "//input[@type='search']", article_name)
        self.press_key(By.XPATH, "//input[@type='search']", Keys.ENTER)
        self.element_visible(By.XPATH, f"//div[@class='m-dashboard__sub-head m-dashboard__sub-head__summary'][text()='{article_name}']")

    def click_existing_article(self, article_name):
        self.click_element(By.XPATH, f"//a/span[text()='{article_name}']")

    def click_entry_type_dropdown(self):
        self.click_element(By.CLASS_NAME, "res-split-button__toggle")

    def saved(self):
        self.element_visible(By.XPATH, "//res-icon[@title='Saved']")

    def view_published_entry(self, entry_type):
        self.click_element(By.XPATH, "//a[text()='" + entry_type + "']")

    def click_entry_type(self, entry_type):
        self.click_element(By.XPATH, "//res-dropdown/ul/li/a/span[text()='" + entry_type + "']")


class ComposeTab(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.compose_tab_present = self.element_visible(By.CLASS_NAME, "is-story")

    def type_headline(self, text):
        self.clear_and_type(By.CSS_SELECTOR, "#r-21 > div.ql-editor", text)

    def type_dek(self, text):
        self.type(By.CSS_SELECTOR, "#r-25 > div.ql-editor.ql-blank", text)

    def add_story_content(self, text):
        self.type(By.XPATH, "//div[@class='ql-container']/div[1]", text)

    def add_new_story_content(self, text):
        """
        Adds a timestamp to your text and returns the full text string, so later in the test we can use
            get_and_match_text to ensure our edit was posted successfully.
        """
        time = f"{datetime.datetime.now():%Y-%m-%d_%H:%M:%S}"
        updated_text = text + time
        self.clear_and_type(By.XPATH, "//div[@class='ql-container']/div[1]", updated_text)
        return updated_text

    def click_select_art(self):
        self.click_element(By.XPATH, "//button[@title='Choose art']")

    def body_item_displayed(self, item_class_name):
        self.scroll_to_element(By.CLASS_NAME, item_class_name + "-object")
        self.element_visible(By.CLASS_NAME, item_class_name + "-object")

    def click_insert_dropdown_item(self, item_title):
        self.click_element(By.XPATH, "//div[@id='toolbar']//button[text()='Insert']")
        self.scroll_to_element(By.XPATH, "//res-dropdown[@for='r-93']//button[@title='" + item_title + "']")
        self.click_element(By.XPATH, "//res-dropdown[@for='r-93']//button[@title='" + item_title + "']")

    class LeadArtDropdown(BasePage):

        def __init__(self, driver):
            super().__init__(driver)

        def click_search(self):
            self.click_element(By.XPATH, "//res-dropdown[@for='main-lead-art-picker-text']/div/button[1]")

        def upload_lead_art(self, file_path):
            self.upload_file(By.XPATH, "//res-dropdown[@for='main-lead-art-picker-text']//input", file_path)

    class ImageSearch(BasePage):

        def __init__(self, driver):
            super().__init__(driver)
            self.tile_container = self.element_visible(By.CLASS_NAME, "p-tile__container")

        def tile_container_reload(self):
            self.element_visible(By.CLASS_NAME, "p-tile__container")

        def enter_image_search_text(self, text):
            self.type(By.ID, "query", text)

        def select_source(self, text):
            self.type(By.XPATH, "//select[@name='source']", text)

        def select_image(self):
            self.click_element(By.XPATH, "//div[@class='p-tile__container']/div[1]")

    class AddImageModal(BasePage):

        def __init__(self, driver):
            super().__init__(driver)

        def click_insert_image(self):
            self.click_element(By.XPATH, "//*[@id='modal']//button[@type='submit']")

    class AddGalleryModal(BasePage):

        def __init__(self, driver):
            super().__init__(driver)

        def click_new_gallery(self):
            self.click_element(By.XPATH, "//*[@id='modal']//button[text()='gallery']")

    class CreateGalleryMenu(BasePage):

        def __init__(self, driver):
            super().__init__(driver)

        def enter_gallery_title(self, text):
            self.clear_input(By.XPATH, "//div[@class='m-overlay__nav']//div[@class='m-quill-input res-input__input ql-container']/div[@class='ql-editor']")
            self.type(By.XPATH, "//div[@class='m-overlay__nav']//div[@class='m-quill-input res-input__input ql-container']/div[@class='ql-editor ql-blank']", text)

        def click_gallery_image_dropdown(self):
            self.click_element(By.XPATH, "//div[@class='m-overlay__main m-gallery ']//button[@title='Choose art']")

        def upload_gallery_images(self, first_image, second_image):
            self.upload_files(By.ID, "image-upload-add-gallery-images-grid-picker-text", [first_image, second_image])
            self.elements_visible(By.XPATH, [
                    "//div[@class='p-tile__container']//div[@class='m-gallery__image'][1]",
                    "//div[@class='p-tile__container']//div[@class='m-gallery__image'][2]"
            ])

        def click_insert_gallery(self):
            self.click_element(By.XPATH, "//button[text()='gallery']")

    def click_preview(self):
        self.click_element(By.LINK_TEXT, "Preview")

    def click_finalize(self):
        self.click_element(By.LINK_TEXT, "Finalize")


class FinalizeTab(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.finalize_tab_present = self.element_visible(By.CLASS_NAME, "m-field-group")

    def click_publish_button(self):
        self.element_enabled(By.XPATH, "//button[text()='Publish now']")
        self.click_element(By.XPATH, "//button[text()='Publish now']")

    def click_confirm_publish_now(self):
        self.element_enabled(By.XPATH, "//button[text()='Confirm publish now']")
        self.click_element(By.XPATH, "//button[text()='Confirm publish now']")

    def click_publish_changes(self):
        self.element_enabled(By.XPATH, "//button[text()='Publish changes']")
        self.click_element(By.XPATH, "//button[text()='Publish changes']")

    def click_confirm_publish_changes(self):
        self.element_enabled(By.XPATH, "//button[text()='Confirm publish changes']")
        self.click_element(By.XPATH, "//button[text()='Confirm publish changes']")
