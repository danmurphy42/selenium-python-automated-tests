import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def element_visible(self, locator_method, locator, wait_time=10):
        """
        element_visible checks if an element is present in the DOM and has width and height.

        :param locator_method: (obj) a By. statement to determine locator strategy. (e.g. By.CLASS_NAME)
        :param locator: (str) the locator in the DOM.
        :param wait_time: (int) number of seconds the test will wait for the element to become visible before failing.
            Defaults to 10.

        Locator strategies:
            https://selenium-python.readthedocs.io/api.html#locate-elements-by
        """
        WebDriverWait(self.driver.instance, wait_time).until(EC.visibility_of_element_located((
            locator_method, locator)))
        print(f"✅ Element '{locator}' was visible.")

    def element_present(self, locator_method, locator, wait_time=10):
        """
        element_present differs with element_visible in that it simply checks if the element is present in the DOM,
            whereas element_visible also checks if it has width and height.

        :param locator_method: (obj) a By. statement to determine locator strategy. (e.g. By.CLASS_NAME)
        :param locator: (str) the locator in the DOM.
        :param wait_time: (int) number of seconds the test will wait for the element to become visible before failing.
            Defaults to 10.
        """
        WebDriverWait(self.driver.instance, wait_time).until(EC.presence_of_element_located((
            locator_method, locator)))
        print(f"✅ Element '{locator}' was present.")

    def element_enabled(self, locator_method, locator, wait_time=10):
        """
        element_enabled finds an element in the DOM and ensures it's clickable.

        :param locator_method: (obj) a By. statement to determine locator strategy. (e.g. By.CLASS_NAME)
        :param locator: (str) the locator in the DOM.
        :param wait_time: (int) number of seconds the test will wait for the element to become visible before failing.
            Defaults to 10.
        """
        WebDriverWait(self.driver.instance, wait_time).until(EC.element_to_be_clickable((
            locator_method, locator)))
        print(f"✅ Element '{locator}' was enabled.")

    def elements_visible(self, locator_method, locator_list, wait_time=10):
        """
        elements_visible accepts a list of elements to find on a page.
        """
        for locator in locator_list:
            WebDriverWait(self.driver.instance, wait_time).until(EC.visibility_of_element_located((
                locator_method, locator)))
        print(f"✅ Elements '" + "', '".join(locator_list) + "' were visible.")

    def click_element(self, locator_method, locator, wait_time=10):
        """
        click_element finds an element and simulates a click on it.
        """
        WebDriverWait(self.driver.instance, wait_time).until(EC.visibility_of_element_located((
            locator_method, locator))).click()
        print(f"✅ Clicked element '{locator}'.")

    def clear_and_type(self, locator_method, locator, text, wait_time=10):
        """
        clear_and_type finds an input in the DOM, clears any placeholder text, and types text into it.

        :param text: (str) the text to be typed into the input.
        """
        WebDriverWait(self.driver.instance, wait_time).until(EC.visibility_of_element_located((
            locator_method, locator))).clear()
        WebDriverWait(self.driver.instance, wait_time).until(EC.visibility_of_element_located((
            locator_method, locator))).send_keys(text)
        print(f"✅ Cleared element '{locator}' and typed '{text}'.")

    def clear_input(self, locator_method, locator, wait_time=10):
        """
        clear_input removes placeholder text from an input. Useful for when clearing an input changes the locator.
            Otherwise, use clear_and_type.
        """
        WebDriverWait(self.driver.instance, wait_time).until(EC.presence_of_element_located((
            locator_method, locator))).clear()
        print(f"✅ Cleared text from element '{locator}'.")

    def type(self, locator_method, locator, text, wait_time=10):
        """
        type finds an input in the DOM and sends keys to it.

        :param text: (str) the text to be typed into the input.
        """
        WebDriverWait(self.driver.instance, wait_time).until(EC.presence_of_element_located((
            locator_method, locator))).send_keys(text)
        print(f"✅ Typed '{text}' into element '{locator}'.")

    def upload_file(self, locator_method, locator, file_path, wait_time=10):
        """
        upload_file finds a file input in the DOM and sends a file path to it, thus uploading the file.

        :param file_path: (str) the RELATIVE path to the file being uploaded. There is embedded logic to convert it to
            the real file path.
        """
        WebDriverWait(self.driver.instance, wait_time).until(EC.presence_of_element_located((
            locator_method, locator))).send_keys(os.path.abspath(file_path))
        print(f"✅ Uploaded file '{file_path}' to element '{locator}'.")

    def upload_files(self, locator_method, locator, file_paths_list, wait_time=10):
        """
        upload_files accepts a list of file paths to send to a file input, allowing us to upload multiple files at once.

        :param file_paths_list: a LIST of relative file path strings. Like upload_file, there is embedded logic to
            convert the relative file paths to their real file paths.
        """
        real_file_paths_list = map(lambda i: os.path.abspath(i), file_paths_list)
        combined_file_path = " \n ".join(real_file_paths_list)
        WebDriverWait(self.driver.instance, wait_time).until(EC.presence_of_element_located((
            locator_method, locator))).send_keys(combined_file_path)
        print(f"✅ Uploaded files '" + "', '".join(file_paths_list) + f"' to element '{locator}'.")

    def press_key(self, locator_method, locator, key, wait_time=10):
        """
        press_key sends a keystroke, like ENTER or DELETE, to an element.

        :param key: (ojb) a Key. statement to determine the keystroke you want to send. (e.g. Keys.ENTER)

        Special keys:
            https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.keys
        """
        WebDriverWait(self.driver.instance, wait_time).until(EC.visibility_of_element_located((
            locator_method, locator))).send_keys(key)
        print(f"✅ Pressed key '{str(key)}' in element '{locator}'.")

    def scroll_to_element(self, locator_method, locator, wait_time=10):
        """
        scroll_to_element finds an element in the DOM and scrolls the window to it. Useful in situations where another
            element is interfering with a click.
        """
        element = WebDriverWait(self.driver.instance, wait_time).until(EC.visibility_of_element_located((
            locator_method, locator)))
        self.driver.instance.execute_script("arguments[0].scrollIntoView(true);", element)

    def get_and_match_text(self, locator_method, locator, text, wait_time=10):
        """
        get_and_match_text accepts element info like the other methods, gets the text content of that element, and
            determines if it matches the text content you passed in.

        :param text: (str) the text you're matching against. The test will fail if this does not match the text Selenium
            retrieves from the element.
        """
        element_text = WebDriverWait(self.driver.instance, wait_time).until(EC.visibility_of_element_located((
            locator_method, locator))).text
        if element_text is text:
            raise Exception(f"Text of {locator} did not match provided text.")
        else:
            print(f"✅ Text of '{locator}' matched '{text}'.")
