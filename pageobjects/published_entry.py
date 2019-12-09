from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage
from values.strings import EntryTypeClasses


class PublishedEntry(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.article_body = self.element_visible(By.XPATH, "//body")

    def entry_type_check(self, entry_type_class):
        self.element_visible(By.CLASS_NAME, entry_type_class)

    def lead_image_visible(self):
        self.element_visible(By.CLASS_NAME, "c-picture")

    def body_text_present(self, text):
        self.get_and_match_text(By.XPATH, "//*[@class='c-entry-content ']/p", text)

    def body_gallery_displayed(self):
        self.element_visible(By.CLASS_NAME, "c-image-gallery__body")

    def story_items_displayed(self, headline, dek, entry_content):
        story_item_xpath_locators = [
            f"//h1[text()='{headline}']",
            f"//p[@class='c-entry-summary p-dek'][text()='{dek}']",
            f"//p[text()='{entry_content}']"
        ]
        self.entry_type_check(EntryTypeClasses.standard)
        self.lead_image_visible()
        self.elements_visible(By.XPATH, story_item_xpath_locators)
